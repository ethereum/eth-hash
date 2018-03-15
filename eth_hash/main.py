from typing import (
    Union,
)

from .preimage import (
    BasePreImage,
)


class Keccak256:
    def __init__(self, backend):
        self.hasher = backend.keccak256
        self.preimage = backend.preimage

        assert self.hasher(b'') == b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';\x7b\xfa\xd8\x04]\x85\xa4p"  # noqa: E501

    def __call__(self, preimage: Union[bytes, bytearray]) -> bytes:
        if not isinstance(preimage, (bytes, bytearray)):
            raise TypeError(
                "Can only compute the hash of `bytes` or `bytearray` values, not %r" % preimage
            )

        return self.hasher(preimage)

    def new(self, preimage: (Union[bytes, bytearray])) -> BasePreImage:
        if not isinstance(preimage, (bytes, bytearray)):
            raise TypeError(
                "Can only compute the hash of `bytes` or `bytearray` values, not %r" % preimage
            )
        return self.preimage(preimage)
