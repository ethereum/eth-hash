import pytest


def test_import_auto():
    from eth_hash.auto import keccak  # noqa: F401


def test_import_auto_empty_crash():
    from eth_hash.auto import keccak
    with pytest.raises(ImportError, match="None of these hashing backends are installed"):
        keccak(b'')


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
    from eth_hash.auto import keccak
    monkeypatch.setenv('ETH_HASH_BACKEND', backend)
    with pytest.raises(ImportError) as excinfo:
        keccak(b'triggered')
    expected_msg = (
        "The backend specified in ETH_HASH_BACKEND, '{0}', is not installed. "
        "Install with `pip install eth-hash[{0}]`.".format(backend)
    )
    assert expected_msg in str(excinfo.value)


def test_load_unavailable_backend_by_env(monkeypatch):
    from eth_hash.auto import keccak
    backend = 'this-backend-will-never-exist'
    monkeypatch.setenv('ETH_HASH_BACKEND', backend)
    with pytest.raises(ValueError) as excinfo:
        keccak(b'triggered')
    expected_msg = (
        "The backend specified in ETH_HASH_BACKEND, '{0}', is not supported. "
        "Choose one of".format(backend)
    )
    assert expected_msg in str(excinfo.value)
