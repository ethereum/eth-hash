import pytest


@pytest.fixture(params=["auto", "explicit", "env"])
def keccak(monkeypatch, request, keccak_auto):
    if request.param == "auto":
        return keccak_auto
    elif request.param == "explicit":
        from eth_hash.backends import pysha3
        from eth_hash import Keccak256

        return Keccak256(pysha3)
    elif request.param == "env":
        monkeypatch.setenv("ETH_HASH_BACKEND", "pysha3")
        from eth_hash.auto import keccak

        return keccak
    else:
        raise AssertionError(
            "Unrecognized approach to import keccak: %s" % request.param
        )
