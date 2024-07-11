from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OllamaConfig(_message.Message):
    __slots__ = ("url", "model")
    URL_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    url: str
    model: str
    def __init__(self, url: _Optional[str] = ..., model: _Optional[str] = ...) -> None: ...

class OpenAIConfig(_message.Message):
    __slots__ = ("model", "token")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    model: str
    token: str
    def __init__(self, model: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class RevaChatMessage(_message.Message):
    __slots__ = ("chatId", "message", "project", "programName", "ollama", "openai")
    CHATID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    PROGRAMNAME_FIELD_NUMBER: _ClassVar[int]
    OLLAMA_FIELD_NUMBER: _ClassVar[int]
    OPENAI_FIELD_NUMBER: _ClassVar[int]
    chatId: str
    message: str
    project: str
    programName: str
    ollama: OllamaConfig
    openai: OpenAIConfig
    def __init__(self, chatId: _Optional[str] = ..., message: _Optional[str] = ..., project: _Optional[str] = ..., programName: _Optional[str] = ..., ollama: _Optional[_Union[OllamaConfig, _Mapping]] = ..., openai: _Optional[_Union[OpenAIConfig, _Mapping]] = ...) -> None: ...

class RevaChatMessageResponse(_message.Message):
    __slots__ = ("chatId", "thought", "message")
    CHATID_FIELD_NUMBER: _ClassVar[int]
    THOUGHT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    chatId: str
    thought: str
    message: str
    def __init__(self, chatId: _Optional[str] = ..., thought: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class RevaChatShutdown(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevaChatShutdownResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
