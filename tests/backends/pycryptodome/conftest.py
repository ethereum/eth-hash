import pytest


@pytest.fixture(params=["auto", "explicit", "env"])
def keccak(monkeypatch, request, keccak_auto):
    if request.param == "auto":
        return keccak_auto
    elif request.param == "explicit":
        from eth_hash import (
            Keccak256,
        )
        from eth_hash.backends import (
            pycryptodome,
        )

        return Keccak256(pycryptodome)
    elif request.param == "env":
        monkeypatch.setenv("ETH_HASH_BACKEND", "pycryptodome")
        from eth_hash.auto import (
            keccak,
        )

        return keccak
    else:
        raise AssertionError(f"Unrecognized approach to import keccak: {request.param}")
