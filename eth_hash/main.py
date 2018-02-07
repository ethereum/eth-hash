class Keccak256:
    def __init__(self, backend):
        self.hasher = backend.keccak256

        assert self.hasher(b'') == b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';{\xfa\xd8\x04]\x85\xa4p"  # noqa: E501

    def __call__(self, preimage):
        if not isinstance(preimage, bytes):
            raise TypeError("Can only compute the hash of a `bytes` value, not %r" % preimage)

        return self.hasher(preimage)
