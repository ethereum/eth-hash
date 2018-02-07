import importlib

from .main import (
    Keccak256,
)


def choose_available_backend():
    possible_backends = [
        'pycryptodome',  # prefer over pysha3, for pypy3 support
        'pysha3',
    ]
    for backend in possible_backends:
        try:
            return importlib.import_module('eth_hash.backends.%s' % backend)
        except ImportError:
            pass
    raise EnvironmentError("None of these backends are available: %r" % possible_backends)


keccak = Keccak256(choose_available_backend())
