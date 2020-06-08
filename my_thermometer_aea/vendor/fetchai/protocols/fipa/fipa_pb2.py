# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fipa.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="fipa.proto",
    package="fetch.aea.Fipa",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=b'\n\nfipa.proto\x12\x0e\x66\x65tch.aea.Fipa"\xc4\x0c\n\x0b\x46ipaMessage\x12\x12\n\nmessage_id\x18\x01 \x01(\x05\x12"\n\x1a\x64ialogue_starter_reference\x18\x02 \x01(\t\x12$\n\x1c\x64ialogue_responder_reference\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\x05\x12\x41\n\x06\x61\x63\x63\x65pt\x18\x05 \x01(\x0b\x32/.fetch.aea.Fipa.FipaMessage.Accept_PerformativeH\x00\x12S\n\x0f\x61\x63\x63\x65pt_w_inform\x18\x06 \x01(\x0b\x32\x38.fetch.aea.Fipa.FipaMessage.Accept_W_Inform_PerformativeH\x00\x12;\n\x03\x63\x66p\x18\x07 \x01(\x0b\x32,.fetch.aea.Fipa.FipaMessage.Cfp_PerformativeH\x00\x12\x43\n\x07\x64\x65\x63line\x18\x08 \x01(\x0b\x32\x30.fetch.aea.Fipa.FipaMessage.Decline_PerformativeH\x00\x12\x41\n\x06inform\x18\t \x01(\x0b\x32/.fetch.aea.Fipa.FipaMessage.Inform_PerformativeH\x00\x12M\n\x0cmatch_accept\x18\n \x01(\x0b\x32\x35.fetch.aea.Fipa.FipaMessage.Match_Accept_PerformativeH\x00\x12_\n\x15match_accept_w_inform\x18\x0b \x01(\x0b\x32>.fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform_PerformativeH\x00\x12\x43\n\x07propose\x18\x0c \x01(\x0b\x32\x30.fetch.aea.Fipa.FipaMessage.Propose_PerformativeH\x00\x1a"\n\x0b\x44\x65scription\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\x0c\x1a\x81\x01\n\x05Query\x12\x0f\n\x05\x62ytes\x18\x01 \x01(\x0cH\x00\x12<\n\x07nothing\x18\x02 \x01(\x0b\x32).fetch.aea.Fipa.FipaMessage.Query.NothingH\x00\x12\x15\n\x0bquery_bytes\x18\x03 \x01(\x0cH\x00\x1a\t\n\x07NothingB\x07\n\x05query\x1a\x44\n\x10\x43\x66p_Performative\x12\x30\n\x05query\x18\x01 \x01(\x0b\x32!.fetch.aea.Fipa.FipaMessage.Query\x1aQ\n\x14Propose_Performative\x12\x39\n\x08proposal\x18\x01 \x01(\x0b\x32\'.fetch.aea.Fipa.FipaMessage.Description\x1a\x9d\x01\n\x1c\x41\x63\x63\x65pt_W_Inform_Performative\x12P\n\x04info\x18\x01 \x03(\x0b\x32\x42.fetch.aea.Fipa.FipaMessage.Accept_W_Inform_Performative.InfoEntry\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xa9\x01\n"Match_Accept_W_Inform_Performative\x12V\n\x04info\x18\x01 \x03(\x0b\x32H.fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform_Performative.InfoEntry\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x8b\x01\n\x13Inform_Performative\x12G\n\x04info\x18\x01 \x03(\x0b\x32\x39.fetch.aea.Fipa.FipaMessage.Inform_Performative.InfoEntry\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x15\n\x13\x41\x63\x63\x65pt_Performative\x1a\x16\n\x14\x44\x65\x63line_Performative\x1a\x1b\n\x19Match_Accept_PerformativeB\x0e\n\x0cperformativeb\x06proto3',
)


_FIPAMESSAGE_DESCRIPTION = _descriptor.Descriptor(
    name="Description",
    full_name="fetch.aea.Fipa.FipaMessage.Description",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="description",
            full_name="fetch.aea.Fipa.FipaMessage.Description.description",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=750,
    serialized_end=784,
)

_FIPAMESSAGE_QUERY_NOTHING = _descriptor.Descriptor(
    name="Nothing",
    full_name="fetch.aea.Fipa.FipaMessage.Query.Nothing",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=898,
    serialized_end=907,
)

_FIPAMESSAGE_QUERY = _descriptor.Descriptor(
    name="Query",
    full_name="fetch.aea.Fipa.FipaMessage.Query",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="bytes",
            full_name="fetch.aea.Fipa.FipaMessage.Query.bytes",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="nothing",
            full_name="fetch.aea.Fipa.FipaMessage.Query.nothing",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="query_bytes",
            full_name="fetch.aea.Fipa.FipaMessage.Query.query_bytes",
            index=2,
            number=3,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_FIPAMESSAGE_QUERY_NOTHING,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="query",
            full_name="fetch.aea.Fipa.FipaMessage.Query.query",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=787,
    serialized_end=916,
)

_FIPAMESSAGE_CFP_PERFORMATIVE = _descriptor.Descriptor(
    name="Cfp_Performative",
    full_name="fetch.aea.Fipa.FipaMessage.Cfp_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="query",
            full_name="fetch.aea.Fipa.FipaMessage.Cfp_Performative.query",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=918,
    serialized_end=986,
)

_FIPAMESSAGE_PROPOSE_PERFORMATIVE = _descriptor.Descriptor(
    name="Propose_Performative",
    full_name="fetch.aea.Fipa.FipaMessage.Propose_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="proposal",
            full_name="fetch.aea.Fipa.FipaMessage.Propose_Performative.proposal",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=988,
    serialized_end=1069,
)

_FIPAMESSAGE_ACCEPT_W_INFORM_PERFORMATIVE_INFOENTRY = _descriptor.Descriptor(
    name="InfoEntry",
    full_name="fetch.aea.Fipa.FipaMessage.Accept_W_Inform_Performative.InfoEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="fetch.aea.Fipa.FipaMessage.Accept_W_Inform_Performative.InfoEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="fetch.aea.Fipa.FipaMessage.Accept_W_Inform_Performative.InfoEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1186,
    serialized_end=1229,
)

_FIPAMESSAGE_ACCEPT_W_INFORM_PERFORMATIVE = _descriptor.Descriptor(
    name="Accept_W_Inform_Performative",
    full_name="fetch.aea.Fipa.FipaMessage.Accept_W_Inform_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="info",
            full_name="fetch.aea.Fipa.FipaMessage.Accept_W_Inform_Performative.info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_FIPAMESSAGE_ACCEPT_W_INFORM_PERFORMATIVE_INFOENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1072,
    serialized_end=1229,
)

_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_PERFORMATIVE_INFOENTRY = _descriptor.Descriptor(
    name="InfoEntry",
    full_name="fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform_Performative.InfoEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform_Performative.InfoEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform_Performative.InfoEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1186,
    serialized_end=1229,
)

_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_PERFORMATIVE = _descriptor.Descriptor(
    name="Match_Accept_W_Inform_Performative",
    full_name="fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="info",
            full_name="fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform_Performative.info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_PERFORMATIVE_INFOENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1232,
    serialized_end=1401,
)

_FIPAMESSAGE_INFORM_PERFORMATIVE_INFOENTRY = _descriptor.Descriptor(
    name="InfoEntry",
    full_name="fetch.aea.Fipa.FipaMessage.Inform_Performative.InfoEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="fetch.aea.Fipa.FipaMessage.Inform_Performative.InfoEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="fetch.aea.Fipa.FipaMessage.Inform_Performative.InfoEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1186,
    serialized_end=1229,
)

_FIPAMESSAGE_INFORM_PERFORMATIVE = _descriptor.Descriptor(
    name="Inform_Performative",
    full_name="fetch.aea.Fipa.FipaMessage.Inform_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="info",
            full_name="fetch.aea.Fipa.FipaMessage.Inform_Performative.info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_FIPAMESSAGE_INFORM_PERFORMATIVE_INFOENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1404,
    serialized_end=1543,
)

_FIPAMESSAGE_ACCEPT_PERFORMATIVE = _descriptor.Descriptor(
    name="Accept_Performative",
    full_name="fetch.aea.Fipa.FipaMessage.Accept_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1545,
    serialized_end=1566,
)

_FIPAMESSAGE_DECLINE_PERFORMATIVE = _descriptor.Descriptor(
    name="Decline_Performative",
    full_name="fetch.aea.Fipa.FipaMessage.Decline_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1568,
    serialized_end=1590,
)

_FIPAMESSAGE_MATCH_ACCEPT_PERFORMATIVE = _descriptor.Descriptor(
    name="Match_Accept_Performative",
    full_name="fetch.aea.Fipa.FipaMessage.Match_Accept_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1592,
    serialized_end=1619,
)

_FIPAMESSAGE = _descriptor.Descriptor(
    name="FipaMessage",
    full_name="fetch.aea.Fipa.FipaMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="message_id",
            full_name="fetch.aea.Fipa.FipaMessage.message_id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dialogue_starter_reference",
            full_name="fetch.aea.Fipa.FipaMessage.dialogue_starter_reference",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dialogue_responder_reference",
            full_name="fetch.aea.Fipa.FipaMessage.dialogue_responder_reference",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="target",
            full_name="fetch.aea.Fipa.FipaMessage.target",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="accept",
            full_name="fetch.aea.Fipa.FipaMessage.accept",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="accept_w_inform",
            full_name="fetch.aea.Fipa.FipaMessage.accept_w_inform",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="cfp",
            full_name="fetch.aea.Fipa.FipaMessage.cfp",
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="decline",
            full_name="fetch.aea.Fipa.FipaMessage.decline",
            index=7,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="inform",
            full_name="fetch.aea.Fipa.FipaMessage.inform",
            index=8,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="match_accept",
            full_name="fetch.aea.Fipa.FipaMessage.match_accept",
            index=9,
            number=10,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="match_accept_w_inform",
            full_name="fetch.aea.Fipa.FipaMessage.match_accept_w_inform",
            index=10,
            number=11,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="propose",
            full_name="fetch.aea.Fipa.FipaMessage.propose",
            index=11,
            number=12,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _FIPAMESSAGE_DESCRIPTION,
        _FIPAMESSAGE_QUERY,
        _FIPAMESSAGE_CFP_PERFORMATIVE,
        _FIPAMESSAGE_PROPOSE_PERFORMATIVE,
        _FIPAMESSAGE_ACCEPT_W_INFORM_PERFORMATIVE,
        _FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_PERFORMATIVE,
        _FIPAMESSAGE_INFORM_PERFORMATIVE,
        _FIPAMESSAGE_ACCEPT_PERFORMATIVE,
        _FIPAMESSAGE_DECLINE_PERFORMATIVE,
        _FIPAMESSAGE_MATCH_ACCEPT_PERFORMATIVE,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="fetch.aea.Fipa.FipaMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=31,
    serialized_end=1635,
)

_FIPAMESSAGE_DESCRIPTION.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_QUERY_NOTHING.containing_type = _FIPAMESSAGE_QUERY
_FIPAMESSAGE_QUERY.fields_by_name["nothing"].message_type = _FIPAMESSAGE_QUERY_NOTHING
_FIPAMESSAGE_QUERY.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_QUERY.oneofs_by_name["query"].fields.append(
    _FIPAMESSAGE_QUERY.fields_by_name["bytes"]
)
_FIPAMESSAGE_QUERY.fields_by_name[
    "bytes"
].containing_oneof = _FIPAMESSAGE_QUERY.oneofs_by_name["query"]
_FIPAMESSAGE_QUERY.oneofs_by_name["query"].fields.append(
    _FIPAMESSAGE_QUERY.fields_by_name["nothing"]
)
_FIPAMESSAGE_QUERY.fields_by_name[
    "nothing"
].containing_oneof = _FIPAMESSAGE_QUERY.oneofs_by_name["query"]
_FIPAMESSAGE_QUERY.oneofs_by_name["query"].fields.append(
    _FIPAMESSAGE_QUERY.fields_by_name["query_bytes"]
)
_FIPAMESSAGE_QUERY.fields_by_name[
    "query_bytes"
].containing_oneof = _FIPAMESSAGE_QUERY.oneofs_by_name["query"]
_FIPAMESSAGE_CFP_PERFORMATIVE.fields_by_name["query"].message_type = _FIPAMESSAGE_QUERY
_FIPAMESSAGE_CFP_PERFORMATIVE.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_PROPOSE_PERFORMATIVE.fields_by_name[
    "proposal"
].message_type = _FIPAMESSAGE_DESCRIPTION
_FIPAMESSAGE_PROPOSE_PERFORMATIVE.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_ACCEPT_W_INFORM_PERFORMATIVE_INFOENTRY.containing_type = (
    _FIPAMESSAGE_ACCEPT_W_INFORM_PERFORMATIVE
)
_FIPAMESSAGE_ACCEPT_W_INFORM_PERFORMATIVE.fields_by_name[
    "info"
].message_type = _FIPAMESSAGE_ACCEPT_W_INFORM_PERFORMATIVE_INFOENTRY
_FIPAMESSAGE_ACCEPT_W_INFORM_PERFORMATIVE.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_PERFORMATIVE_INFOENTRY.containing_type = (
    _FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_PERFORMATIVE
)
_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_PERFORMATIVE.fields_by_name[
    "info"
].message_type = _FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_PERFORMATIVE_INFOENTRY
_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_PERFORMATIVE.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_INFORM_PERFORMATIVE_INFOENTRY.containing_type = (
    _FIPAMESSAGE_INFORM_PERFORMATIVE
)
_FIPAMESSAGE_INFORM_PERFORMATIVE.fields_by_name[
    "info"
].message_type = _FIPAMESSAGE_INFORM_PERFORMATIVE_INFOENTRY
_FIPAMESSAGE_INFORM_PERFORMATIVE.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_ACCEPT_PERFORMATIVE.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_DECLINE_PERFORMATIVE.containing_type = _FIPAMESSAGE
_FIPAMESSAGE_MATCH_ACCEPT_PERFORMATIVE.containing_type = _FIPAMESSAGE
_FIPAMESSAGE.fields_by_name["accept"].message_type = _FIPAMESSAGE_ACCEPT_PERFORMATIVE
_FIPAMESSAGE.fields_by_name[
    "accept_w_inform"
].message_type = _FIPAMESSAGE_ACCEPT_W_INFORM_PERFORMATIVE
_FIPAMESSAGE.fields_by_name["cfp"].message_type = _FIPAMESSAGE_CFP_PERFORMATIVE
_FIPAMESSAGE.fields_by_name["decline"].message_type = _FIPAMESSAGE_DECLINE_PERFORMATIVE
_FIPAMESSAGE.fields_by_name["inform"].message_type = _FIPAMESSAGE_INFORM_PERFORMATIVE
_FIPAMESSAGE.fields_by_name[
    "match_accept"
].message_type = _FIPAMESSAGE_MATCH_ACCEPT_PERFORMATIVE
_FIPAMESSAGE.fields_by_name[
    "match_accept_w_inform"
].message_type = _FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_PERFORMATIVE
_FIPAMESSAGE.fields_by_name["propose"].message_type = _FIPAMESSAGE_PROPOSE_PERFORMATIVE
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["accept"]
)
_FIPAMESSAGE.fields_by_name["accept"].containing_oneof = _FIPAMESSAGE.oneofs_by_name[
    "performative"
]
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["accept_w_inform"]
)
_FIPAMESSAGE.fields_by_name[
    "accept_w_inform"
].containing_oneof = _FIPAMESSAGE.oneofs_by_name["performative"]
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["cfp"]
)
_FIPAMESSAGE.fields_by_name["cfp"].containing_oneof = _FIPAMESSAGE.oneofs_by_name[
    "performative"
]
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["decline"]
)
_FIPAMESSAGE.fields_by_name["decline"].containing_oneof = _FIPAMESSAGE.oneofs_by_name[
    "performative"
]
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["inform"]
)
_FIPAMESSAGE.fields_by_name["inform"].containing_oneof = _FIPAMESSAGE.oneofs_by_name[
    "performative"
]
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["match_accept"]
)
_FIPAMESSAGE.fields_by_name[
    "match_accept"
].containing_oneof = _FIPAMESSAGE.oneofs_by_name["performative"]
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["match_accept_w_inform"]
)
_FIPAMESSAGE.fields_by_name[
    "match_accept_w_inform"
].containing_oneof = _FIPAMESSAGE.oneofs_by_name["performative"]
_FIPAMESSAGE.oneofs_by_name["performative"].fields.append(
    _FIPAMESSAGE.fields_by_name["propose"]
)
_FIPAMESSAGE.fields_by_name["propose"].containing_oneof = _FIPAMESSAGE.oneofs_by_name[
    "performative"
]
DESCRIPTOR.message_types_by_name["FipaMessage"] = _FIPAMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FipaMessage = _reflection.GeneratedProtocolMessageType(
    "FipaMessage",
    (_message.Message,),
    {
        "Description": _reflection.GeneratedProtocolMessageType(
            "Description",
            (_message.Message,),
            {
                "DESCRIPTOR": _FIPAMESSAGE_DESCRIPTION,
                "__module__": "fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Description)
            },
        ),
        "Query": _reflection.GeneratedProtocolMessageType(
            "Query",
            (_message.Message,),
            {
                "Nothing": _reflection.GeneratedProtocolMessageType(
                    "Nothing",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _FIPAMESSAGE_QUERY_NOTHING,
                        "__module__": "fipa_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Query.Nothing)
                    },
                ),
                "DESCRIPTOR": _FIPAMESSAGE_QUERY,
                "__module__": "fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Query)
            },
        ),
        "Cfp_Performative": _reflection.GeneratedProtocolMessageType(
            "Cfp_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _FIPAMESSAGE_CFP_PERFORMATIVE,
                "__module__": "fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Cfp_Performative)
            },
        ),
        "Propose_Performative": _reflection.GeneratedProtocolMessageType(
            "Propose_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _FIPAMESSAGE_PROPOSE_PERFORMATIVE,
                "__module__": "fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Propose_Performative)
            },
        ),
        "Accept_W_Inform_Performative": _reflection.GeneratedProtocolMessageType(
            "Accept_W_Inform_Performative",
            (_message.Message,),
            {
                "InfoEntry": _reflection.GeneratedProtocolMessageType(
                    "InfoEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _FIPAMESSAGE_ACCEPT_W_INFORM_PERFORMATIVE_INFOENTRY,
                        "__module__": "fipa_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Accept_W_Inform_Performative.InfoEntry)
                    },
                ),
                "DESCRIPTOR": _FIPAMESSAGE_ACCEPT_W_INFORM_PERFORMATIVE,
                "__module__": "fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Accept_W_Inform_Performative)
            },
        ),
        "Match_Accept_W_Inform_Performative": _reflection.GeneratedProtocolMessageType(
            "Match_Accept_W_Inform_Performative",
            (_message.Message,),
            {
                "InfoEntry": _reflection.GeneratedProtocolMessageType(
                    "InfoEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_PERFORMATIVE_INFOENTRY,
                        "__module__": "fipa_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform_Performative.InfoEntry)
                    },
                ),
                "DESCRIPTOR": _FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_PERFORMATIVE,
                "__module__": "fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Match_Accept_W_Inform_Performative)
            },
        ),
        "Inform_Performative": _reflection.GeneratedProtocolMessageType(
            "Inform_Performative",
            (_message.Message,),
            {
                "InfoEntry": _reflection.GeneratedProtocolMessageType(
                    "InfoEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _FIPAMESSAGE_INFORM_PERFORMATIVE_INFOENTRY,
                        "__module__": "fipa_pb2"
                        # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Inform_Performative.InfoEntry)
                    },
                ),
                "DESCRIPTOR": _FIPAMESSAGE_INFORM_PERFORMATIVE,
                "__module__": "fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Inform_Performative)
            },
        ),
        "Accept_Performative": _reflection.GeneratedProtocolMessageType(
            "Accept_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _FIPAMESSAGE_ACCEPT_PERFORMATIVE,
                "__module__": "fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Accept_Performative)
            },
        ),
        "Decline_Performative": _reflection.GeneratedProtocolMessageType(
            "Decline_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _FIPAMESSAGE_DECLINE_PERFORMATIVE,
                "__module__": "fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Decline_Performative)
            },
        ),
        "Match_Accept_Performative": _reflection.GeneratedProtocolMessageType(
            "Match_Accept_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _FIPAMESSAGE_MATCH_ACCEPT_PERFORMATIVE,
                "__module__": "fipa_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage.Match_Accept_Performative)
            },
        ),
        "DESCRIPTOR": _FIPAMESSAGE,
        "__module__": "fipa_pb2"
        # @@protoc_insertion_point(class_scope:fetch.aea.Fipa.FipaMessage)
    },
)
_sym_db.RegisterMessage(FipaMessage)
_sym_db.RegisterMessage(FipaMessage.Description)
_sym_db.RegisterMessage(FipaMessage.Query)
_sym_db.RegisterMessage(FipaMessage.Query.Nothing)
_sym_db.RegisterMessage(FipaMessage.Cfp_Performative)
_sym_db.RegisterMessage(FipaMessage.Propose_Performative)
_sym_db.RegisterMessage(FipaMessage.Accept_W_Inform_Performative)
_sym_db.RegisterMessage(FipaMessage.Accept_W_Inform_Performative.InfoEntry)
_sym_db.RegisterMessage(FipaMessage.Match_Accept_W_Inform_Performative)
_sym_db.RegisterMessage(FipaMessage.Match_Accept_W_Inform_Performative.InfoEntry)
_sym_db.RegisterMessage(FipaMessage.Inform_Performative)
_sym_db.RegisterMessage(FipaMessage.Inform_Performative.InfoEntry)
_sym_db.RegisterMessage(FipaMessage.Accept_Performative)
_sym_db.RegisterMessage(FipaMessage.Decline_Performative)
_sym_db.RegisterMessage(FipaMessage.Match_Accept_Performative)


_FIPAMESSAGE_ACCEPT_W_INFORM_PERFORMATIVE_INFOENTRY._options = None
_FIPAMESSAGE_MATCH_ACCEPT_W_INFORM_PERFORMATIVE_INFOENTRY._options = None
_FIPAMESSAGE_INFORM_PERFORMATIVE_INFOENTRY._options = None
# @@protoc_insertion_point(module_scope)