from sha3 import (
    keccak_256 as _keccak_256,
)


def keccak256(prehash: bytes) -> bytes:
    return _keccak_256(prehash).digest()
