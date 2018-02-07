import pytest


@pytest.fixture(params=['auto', 'explicit'])
def keccak(request, keccak_auto):
    if request.param == 'auto':
        return keccak_auto
    elif request.param == 'explicit':
        from eth_hash.backends import pysha3
        from eth_hash import Keccak256
        return Keccak256(pysha3)
    else:
        raise AssertionError("Unrecognized approach to import keccak: %s" % request.param)
