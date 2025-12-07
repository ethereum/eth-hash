from abc import (
    ABC,
    abstractmethod,
)


class PreImageAPI(ABC):
    @abstractmethod
    def __init__(self, value: bytes) -> None:
        ...

    @abstractmethod
    def update(self, value: bytes) -> None:
        ...

    @abstractmethod
    def digest(self) -> bytes:
        ...

    @abstractmethod
    def copy(self) -> "PreImageAPI":
        ...


class BackendAPI(ABC):
    @abstractmethod
    def keccak256(self, in_data: bytearray | bytes) -> bytes:
        ...

    @abstractmethod
    def preimage(self, in_data: bytearray | bytes) -> PreImageAPI:
        ...
