class Keccak256:
    def __init__(self, backend):
        self.hasher = backend.keccak256

        assert self.hasher(b'') == b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';\x7b\xfa\xd8\x04]\x85\xa4p"  # noqa: E501

    def __call__(self, preimage):
        if not isinstance(preimage, bytes):
            raise TypeError("Can only compute the hash of a `bytes` value, not %r" % preimage)

        return self.hasher(preimage)

    def Digest(self, part):
        if not isinstance(part, bytes):
            raise TypeError("Can only compute the hash of a `bytes` value, not %r" % part)
        return Digest(part, keccak_fn=self.hasher)


class Digest:
    def __init__(self, *parts, keccak_fn):
        self.preimage_parts = list(parts)
        self.keccak_fn = keccak_fn

    def update(self, part):
        if not isinstance(part, bytes):
            raise TypeError("Can only compute the hash of a `bytes` value, not %r" % part)
        self.preimage_parts.append(part)

    def digest(self):
        return self.keccak_fn(b''.join(self.preimage_parts))

    def copy(self):
        digest = type(self)(*self.preimage_parts, keccak_fn=self.keccak_fn)
        return digest
