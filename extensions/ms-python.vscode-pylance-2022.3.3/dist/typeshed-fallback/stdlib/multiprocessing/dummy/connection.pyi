from _typeshed import Self
from queue import Queue
from types import TracebackType
from typing import Any, Union

__all__ = ["Client", "Listener", "Pipe"]

families: list[None]

_Address = Union[str, tuple[str, int]]

class Connection:
    _in: Any
    _out: Any
    recv: Any
    recv_bytes: Any
    send: Any
    send_bytes: Any
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __init__(self, _in: Any, _out: Any) -> None: ...
    def close(self) -> None: ...
    def poll(self, timeout: float = ...) -> bool: ...

class Listener:
    _backlog_queue: Queue[Any] | None
    @property
    def address(self) -> Queue[Any] | None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __init__(self, address: _Address | None = ..., family: int | None = ..., backlog: int = ...) -> None: ...
    def accept(self) -> Connection: ...
    def close(self) -> None: ...

def Client(address: _Address) -> Connection: ...
def Pipe(duplex: bool = ...) -> tuple[Connection, Connection]: ...
