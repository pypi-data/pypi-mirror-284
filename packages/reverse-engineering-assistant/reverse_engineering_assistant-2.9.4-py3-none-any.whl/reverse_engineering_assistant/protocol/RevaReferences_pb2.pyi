from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RevaGetReferencesRequest(_message.Message):
    __slots__ = ("address",)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class RevaGetReferencesResponse(_message.Message):
    __slots__ = ("outgoing_references", "incoming_references")
    OUTGOING_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    INCOMING_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    outgoing_references: _containers.RepeatedScalarFieldContainer[str]
    incoming_references: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, outgoing_references: _Optional[_Iterable[str]] = ..., incoming_references: _Optional[_Iterable[str]] = ...) -> None: ...
