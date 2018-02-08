import pytest


def test_import():
    import eth_hash  # noqa: F401


@pytest.mark.parametrize(
    'backend',
    [
        'pycryptodome',
        'pysha3',
    ],
)
def test_load_by_env(monkeypatch, backend):
    monkeypatch.setenv('ETH_HASH_BACKEND', backend)
    with pytest.raises(ImportError) as excinfo:
        from eth_hash.auto import keccak  # noqa: F401
    expected_msg = (
        "The backend specified in ETH_HASH_BACKEND, '{0}', is not installed. "
        "Install with `pip install eth-hash[{0}]`.".format(backend)
    )
    assert expected_msg in str(excinfo.value)


def test_load_unavailable_backend_by_env(monkeypatch):
    backend = 'this-backend-will-never-exist'
    monkeypatch.setenv('ETH_HASH_BACKEND', backend)
    with pytest.raises(ValueError) as excinfo:
        from eth_hash.auto import keccak  # noqa: F401
    expected_msg = (
        "The backend specified in ETH_HASH_BACKEND, '{0}', is not supported. "
        "Choose one of".format(backend)
    )
    assert expected_msg in str(excinfo.value)
