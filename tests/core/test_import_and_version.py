import sys
from unittest import (
    mock,
)

import pytest


def clean_module(name):
    """Clean a module import so all variables in it will be created again"""
    try:
        del sys.modules[name]
    except KeyError:
        pass
    return


def test_import_auto():
    clean_module("eth_hash.auto")
    from eth_hash.auto import keccak  # noqa: F401


def test_import_auto_empty_crash(monkeypatch):
    clean_module("eth_hash.auto")
    from eth_hash.auto import (
        keccak,
    )

    with mock.patch.dict("sys.modules", {"sha3": None, "Crypto.Hash": None}):
        with pytest.raises(
            ImportError, match="None of these hashing backends are installed"
        ):
            keccak(b"eh")


def test_import():
    clean_module("eth_hash")
    import eth_hash

    assert isinstance(eth_hash.__version__, str)


@pytest.mark.parametrize(
    "backend",
    [
        "pycryptodome",
        "pysha3",
    ],
)
def test_load_by_env(monkeypatch, backend):
    clean_module("eth_hash.auto")
    from eth_hash.auto import (
        keccak,
    )

    monkeypatch.setenv("ETH_HASH_BACKEND", backend)
    with mock.patch.dict("sys.modules", {"sha3": None, "Crypto.Hash": None}):
        with pytest.raises(ImportError) as excinfo:
            keccak(b"triggered")
    expected_msg = (
        f"The backend specified in ETH_HASH_BACKEND, '{backend}', is not installed. "
        f'Install with `python -m pip install "eth-hash[{backend}]"`.'
    )
    assert expected_msg in str(excinfo.value)


def test_load_unavailable_backend_by_env(monkeypatch):
    clean_module("eth_hash.auto")
    from eth_hash.auto import (
        keccak,
    )

    backend = "this-backend-will-never-exist"
    monkeypatch.setenv("ETH_HASH_BACKEND", backend)
    with pytest.raises(ValueError) as excinfo:
        keccak(b"triggered")
    expected_msg = (
        f"The backend specified in ETH_HASH_BACKEND, '{backend}', is not supported. "
        "Choose one of"
    )
    assert expected_msg in str(excinfo.value)
