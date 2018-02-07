class Keccak256:
    def __init__(self, backend):
        self.hasher = backend.keccak256
        # TODO run assertion to validate hash once on load, after first backend set up

    def __call__(self, preimage):
        if not isinstance(preimage, bytes):
            raise TypeError("Can only compute the hash of a `bytes` value, not %r" % preimage)

        return self.hasher(preimage)
