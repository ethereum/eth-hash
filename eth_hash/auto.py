import sys

from eth_hash.backends.auto import (
    AutoBackend,
)
from eth_hash.main import (
    Keccak256,
)

keccak = Keccak256(AutoBackend())


def main():
    print(keccak(sys.argv[1].encode()))
