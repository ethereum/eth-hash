from Crypto.Hash import (
    keccak,
)


def keccak256(prehash: bytes) -> bytes:
    hash = keccak.new(digest_bits=256)
    hash.update(prehash)
    return hash.digest()
