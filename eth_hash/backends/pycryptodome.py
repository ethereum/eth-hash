from Crypto.Hash import (
    keccak,
)


def keccak256(prehash: bytes) -> bytes:
    hasher = keccak.new(digest_bits=256)
    hasher.update(prehash)
    return hasher.digest()
