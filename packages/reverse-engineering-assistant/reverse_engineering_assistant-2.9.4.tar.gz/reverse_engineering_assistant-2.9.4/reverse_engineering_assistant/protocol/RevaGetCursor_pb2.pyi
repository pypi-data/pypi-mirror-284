from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RevaGetCursorRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevaGetCursorResponse(_message.Message):
    __slots__ = ("address", "symbol", "function", "selection")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    SELECTION_FIELD_NUMBER: _ClassVar[int]
    address: str
    symbol: str
    function: str
    selection: str
    def __init__(self, address: _Optional[str] = ..., symbol: _Optional[str] = ..., function: _Optional[str] = ..., selection: _Optional[str] = ...) -> None: ...
