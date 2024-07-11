from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RevaSetCommentRequest(_message.Message):
    __slots__ = ("address", "symbol", "comment")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    address: str
    symbol: str
    comment: str
    def __init__(self, address: _Optional[str] = ..., symbol: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class RevaSetCommentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
