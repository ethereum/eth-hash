import pytest

# Note that this file is symlink'd in all backend folders, so a change here is
# automatically shared across backend tests. If you want to add a backend-specific
# test, add it to a new file.


@pytest.fixture
def keccak_auto():
    from eth_hash.auto import keccak
    return keccak


@pytest.mark.parametrize(
    'prehash, expected_result',
    (
        (
            b'',
            b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';\x7b\xfa\xd8\x04]\x85\xa4p",  # noqa: E501
        ),
    ),
)
def test_keccak_256(keccak, prehash, expected_result):
    assert keccak(prehash) == expected_result


@pytest.mark.parametrize(
    'parts, expected_result',
    (
        (
            [b''],
            b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';\x7b\xfa\xd8\x04]\x85\xa4p",  # noqa: E501
        ),
        (
            [b'', b'', b''],
            b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';\x7b\xfa\xd8\x04]\x85\xa4p",  # noqa: E501
        ),
        (
            [b'arst', b'tsra'],
            b"\xb1\xf3T\xb2\x8f\xf2\x84R\xd6\xb9\xd6\x1fA\x06\x1b\xbe\x82\xbe\xb1\xfc\x98\xf33d\xa8\x05\x8d\x1a]\x16M\x05",  # noqa: E501
        ),
    ),
)
def test_keccak_256_digest(keccak, parts, expected_result):
    digest = keccak.Digest(parts[0])
    for part in parts[1:]:
        digest.update(part)
    assert digest.digest() == expected_result


def test_copy_keccak_256_digest(keccak):
    digest_origin = keccak.Digest(b'')
    digest_copy = digest_origin.copy()

    digest_origin.update(b'arsttsra')

    assert digest_origin.digest() == b"\xb1\xf3T\xb2\x8f\xf2\x84R\xd6\xb9\xd6\x1fA\x06\x1b\xbe\x82\xbe\xb1\xfc\x98\xf33d\xa8\x05\x8d\x1a]\x16M\x05"  # noqa: E501
    assert digest_copy.digest() == b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';\x7b\xfa\xd8\x04]\x85\xa4p"  # noqa: E501
