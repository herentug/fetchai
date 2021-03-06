# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
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

"""This package contains a scaffold of a behaviour."""

from typing import Optional, cast

from aea.helpers.search.models import Description
from aea.skills.behaviours import TickerBehaviour

from packages.fetchai.protocols.oef_search.message import OefSearchMessage
from packages.fetchai.protocols.oef_search.serialization import OefSearchSerializer
from packages.fetchai.skills.weather_station.strategy import Strategy

DEFAULT_SERVICES_INTERVAL = 30.0


class ServiceRegistrationBehaviour(TickerBehaviour):
    """This class implements a behaviour."""

    def __init__(self, **kwargs):
        """Initialise the behaviour."""
        services_interval = kwargs.pop(
            "services_interval", DEFAULT_SERVICES_INTERVAL
        )  # type: int
        super().__init__(tick_interval=services_interval, **kwargs)
        self._registered_service_description = None  # type: Optional[Description]

    def setup(self) -> None:
        """
        Implement the setup.

        :return: None
        """
        strategy = cast(Strategy, self.context.strategy)
        if self.context.ledger_apis.has_ledger(strategy.ledger_id):
            balance = self.context.ledger_apis.token_balance(
                strategy.ledger_id,
                cast(str, self.context.agent_addresses.get(strategy.ledger_id)),
            )
            if balance > 0:
                self.context.logger.info(
                    "[{}]: starting balance on {} ledger={}.".format(
                        self.context.agent_name, strategy.ledger_id, balance
                    )
                )
            else:
                self.context.logger.warning(
                    "[{}]: you have no starting balance on {} ledger!".format(
                        self.context.agent_name, strategy.ledger_id
                    )
                )

        self._register_service()

    def act(self) -> None:
        """
        Implement the act.

        :return: None
        """
        self._unregister_service()
        self._register_service()

    def teardown(self) -> None:
        """
        Implement the task teardown.

        :return: None
        """
        strategy = cast(Strategy, self.context.strategy)
        if self.context.ledger_apis.has_ledger(strategy.ledger_id):
            balance = self.context.ledger_apis.token_balance(
                strategy.ledger_id,
                cast(str, self.context.agent_addresses.get(strategy.ledger_id)),
            )
            self.context.logger.info(
                "[{}]: ending balance on {} ledger={}.".format(
                    self.context.agent_name, strategy.ledger_id, balance
                )
            )

        self._unregister_service()

    def _register_service(self) -> None:
        """
        Register to the OEF Service Directory.

        :return: None
        """
        strategy = cast(Strategy, self.context.strategy)
        desc = strategy.get_service_description()
        self._registered_service_description = desc
        oef_msg_id = strategy.get_next_oef_msg_id()
        msg = OefSearchMessage(
            performative=OefSearchMessage.Performative.REGISTER_SERVICE,
            dialogue_reference=(str(oef_msg_id), ""),
            service_description=desc,
        )
        self.context.outbox.put_message(
            to=self.context.search_service_address,
            sender=self.context.agent_address,
            protocol_id=OefSearchMessage.protocol_id,
            message=OefSearchSerializer().encode(msg),
        )
        self.context.logger.info(
            "[{}]: updating weather station services on OEF service directory.".format(
                self.context.agent_name
            )
        )

    def _unregister_service(self) -> None:
        """
        Unregister service from OEF Service Directory.

        :return: None
        """
        strategy = cast(Strategy, self.context.strategy)
        oef_msg_id = strategy.get_next_oef_msg_id()
        msg = OefSearchMessage(
            performative=OefSearchMessage.Performative.UNREGISTER_SERVICE,
            dialogue_reference=(str(oef_msg_id), ""),
            service_description=self._registered_service_description,
        )
        self.context.outbox.put_message(
            to=self.context.search_service_address,
            sender=self.context.agent_address,
            protocol_id=OefSearchMessage.protocol_id,
            message=OefSearchSerializer().encode(msg),
        )
        self.context.logger.info(
            "[{}]: unregistering weather station services from OEF service directory.".format(
                self.context.agent_name
            )
        )
        self._registered_service_description = None
