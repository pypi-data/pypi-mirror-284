from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RevaAddBookmarkRequest(_message.Message):
    __slots__ = ("category", "description", "address")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    category: str
    description: str
    address: str
    def __init__(self, category: _Optional[str] = ..., description: _Optional[str] = ..., address: _Optional[str] = ...) -> None: ...

class RevaAddBookmarkResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevaGetBookmarksRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevaGetbookmarksResponse(_message.Message):
    __slots__ = ("category", "description", "address")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    category: str
    description: str
    address: str
    def __init__(self, category: _Optional[str] = ..., description: _Optional[str] = ..., address: _Optional[str] = ...) -> None: ...
