# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2020 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Webhook connection and channel"""

import asyncio
import json
import logging
from asyncio import CancelledError
from typing import Optional, Union, cast

from aiohttp import web  # type: ignore

from aea.configurations.base import ConnectionConfig, PublicId
from aea.connections.base import Connection
from aea.mail.base import Address, Envelope, EnvelopeContext, URI

from packages.fetchai.protocols.http.message import HttpMessage
from packages.fetchai.protocols.http.serialization import HttpSerializer

SUCCESS = 200
NOT_FOUND = 404
REQUEST_TIMEOUT = 408
SERVER_ERROR = 500
PUBLIC_ID = PublicId.from_str("fetchai/webhook:0.1.0")

logger = logging.getLogger("aea.packages.fetchai.connections.webhook")

RequestId = str


class WebhookChannel:
    """A wrapper for a Webhook."""

    def __init__(
        self,
        agent_address: Address,
        webhook_address: Address,
        webhook_port: int,
        webhook_url_path: str,
        connection_id: PublicId,
    ):
        """
        Initialize a webhook channel.

        :param agent_address: the address of the agent
        :param webhook_address: webhook hostname / IP address
        :param webhook_port: webhook port number
        :param webhook_url_path: the url path to receive webhooks from
        :param connection_id: the connection id
        """
        self.agent_address = agent_address

        self.webhook_address = webhook_address
        self.webhook_port = webhook_port
        self.webhook_url_path = webhook_url_path

        self.webhook_site = None  # type: Optional[web.TCPSite]
        self.runner = None  # type: Optional[web.AppRunner]
        self.app = None  # type: Optional[web.Application]

        self.is_stopped = True

        self.connection_id = connection_id
        self.in_queue = None  # type: Optional[asyncio.Queue]  # pragma: no cover
        logger.info("Initialised a webhook channel")

    async def connect(self) -> None:
        """
        Connect the webhook

        Connects the webhook via the webhook_address and webhook_port parameters
        :return: None
        """
        if self.is_stopped:
            self.app = web.Application()
            self.app.add_routes(
                [web.post(self.webhook_url_path, self._receive_webhook)]
            )
            self.runner = web.AppRunner(self.app)
            await self.runner.setup()
            self.webhook_site = web.TCPSite(
                self.runner, self.webhook_address, self.webhook_port
            )
            await self.webhook_site.start()
            self.is_stopped = False

    async def disconnect(self) -> None:
        """
        Disconnect.

        Shut-off and cleanup the webhook site, the runner and the web app, then stop the channel.

        :return: None
        """
        assert (
            self.webhook_site is not None
            and self.runner is not None
            and self.app is not None
        ), "Application not connected, call connect first!"

        if not self.is_stopped:
            await self.webhook_site.stop()
            await self.runner.shutdown()
            await self.runner.cleanup()
            await self.app.shutdown()
            await self.app.cleanup()
            logger.info("Webhook app is shutdown.")
            self.is_stopped = True

    async def _receive_webhook(self, request: web.Request) -> web.Response:
        """
        Receive a webhook request

        Get webhook request, turn it to envelop and send it to the agent to be picked up.

        :param request: the webhook request
        :return: Http response with a 200 code
        """
        webhook_envelop = await self.to_envelope(request)
        self.in_queue.put_nowait(webhook_envelop)  # type: ignore
        return web.Response(status=200)

    def send(self, request_envelope: Envelope) -> None:
        pass

    async def to_envelope(self, request: web.Request) -> Envelope:
        """
        Convert a webhook request object into an Envelope containing an HttpMessage (from the 'http' Protocol).

        :param request: the webhook request
        :return: The envelop representing the webhook request
        """

        payload_bytes = await request.read()
        version = str(request.version[0]) + "." + str(request.version[1])

        context = EnvelopeContext(uri=URI("aea/mail/base.py"))
        http_message = HttpMessage(
            performative=HttpMessage.Performative.REQUEST,
            method=request.method,
            url=str(request.url),
            version=version,
            headers=json.dumps(dict(request.headers)),
            bodyy=payload_bytes if payload_bytes is not None else b"",
        )
        envelope = Envelope(
            to=self.agent_address,
            sender=request.remote,
            protocol_id=PublicId.from_str("fetchai/http:0.1.0"),
            context=context,
            message=HttpSerializer().encode(http_message),
        )
        return envelope


class WebhookConnection(Connection):
    """Proxy to the functionality of a webhook."""

    def __init__(
        self, webhook_address: str, webhook_port: int, webhook_url_path: str, **kwargs,
    ):
        """
        Initialize a connection.

        :param webhook_address: the webhook hostname / IP address
        :param webhook_port: the webhook port number
        :param webhook_url_path: the url path to receive webhooks from
        """
        if kwargs.get("configuration") is None and kwargs.get("connection_id") is None:
            kwargs["connection_id"] = PUBLIC_ID

        super().__init__(**kwargs)

        self.channel = WebhookChannel(
            agent_address=self.address,
            webhook_address=webhook_address,
            webhook_port=webhook_port,
            webhook_url_path=webhook_url_path,
            connection_id=self.connection_id,
        )

    async def connect(self) -> None:
        """
        Connect to a HTTP server.

        :return: None
        """
        if not self.connection_status.is_connected:
            self.connection_status.is_connected = True
            self.channel.in_queue = asyncio.Queue()
            await self.channel.connect()

    async def disconnect(self) -> None:
        """
        Disconnect from a HTTP server.

        :return: None
        """
        if self.connection_status.is_connected:
            self.connection_status.is_connected = False
            await self.channel.disconnect()

    async def send(self, envelope: "Envelope") -> None:
        """
        The webhook connection does not support send. Webhooks only receive.

        :param envelope: the envelop
        :return: None
        """
        pass

    async def receive(self, *args, **kwargs) -> Optional[Union["Envelope", None]]:
        """
        Receive an envelope.

        :return: the envelope received, or None.
        """
        if not self.connection_status.is_connected:
            raise ConnectionError(
                "Connection not established yet. Please use 'connect()'."
            )  # pragma: no cover
        assert self.channel.in_queue is not None
        try:
            envelope = await self.channel.in_queue.get()
            if envelope is None:
                return None  # pragma: no cover
            return envelope
        except CancelledError:  # pragma: no cover
            return None

    @classmethod
    def from_config(
        cls, address: Address, configuration: ConnectionConfig
    ) -> "Connection":
        """
        Get the HTTP connection from a connection configuration.

        :param address: the address of the agent.
        :param configuration: the connection configuration object.
        :return: the connection object
        """
        webhook_address = cast(str, configuration.config.get("webhook_address"))
        webhook_port = cast(int, configuration.config.get("webhook_port"))
        webhook_url_path = cast(str, configuration.config.get("webhook_url_path"))
        return WebhookConnection(
            webhook_address,
            webhook_port,
            webhook_url_path,
            address=address,
            configuration=configuration,
        )
