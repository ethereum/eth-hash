from sha3 import (
    keccak_256,
)


def keccak256(prehash: bytes) -> bytes:
    return keccak_256(prehash).digest()
