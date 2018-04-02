from eth_hash.utils import (
    auto_choose_backend,
)


class AutoBackend:
    _backend = None

    @property
    def backend(self):
        if self._backend is None:
            self._backend = auto_choose_backend()
        return self._backend

    def __getattr__(self, attr):
        return getattr(self.backend, attr)
