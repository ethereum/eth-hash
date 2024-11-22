# eth-hash

[![Join the conversation on Discord](https://img.shields.io/discord/809793915578089484?color=blue&label=chat&logo=discord&logoColor=white)](https://discord.gg/GHryRvPB84)
[![Build Status](https://circleci.com/gh/ethereum/eth-hash.svg?style=shield)](https://circleci.com/gh/ethereum/eth-hash)
[![PyPI version](https://badge.fury.io/py/eth-hash.svg)](https://badge.fury.io/py/eth-hash)
[![Python versions](https://img.shields.io/pypi/pyversions/eth-hash.svg)](https://pypi.python.org/pypi/eth-hash)
[![Docs build](https://readthedocs.org/projects/eth-hash/badge/?version=latest)](https://eth-hash.readthedocs.io/en/latest/?badge=latest)

The Ethereum hashing function, keccak256, sometimes (erroneously) called sha3

Note: the similarly named [pyethash](https://github.com/ethereum/ethash)
has a completely different use: it generates proofs of work.

This is a low-level library, intended to be used internally by other Ethereum tools.
If you're looking for a convenient hashing tool, check out
[`eth_utils.keccak()`](https://eth-utils.readthedocs.io/en/stable/utilities.html#keccak-bytes-int-bool-text-str-hexstr-str-bytes)
which will be a little friendlier, and provide access to other helpful utilities.

Read the [documentation](https://eth-hash.readthedocs.io/).

[View the change log](https://eth-hash.readthedocs.io/en/latest/release_notes.html).

## Installation

```sh
python -m pip install "eth-hash[pycryptodome]"
```

```py
>>> from eth_hash.auto import keccak
>>> keccak(b'')
b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';{\xfa\xd8\x04]\x85\xa4p"
```

See the [docs](http://eth-hash.readthedocs.io/en/latest/quickstart.html#quickstart)
for more about choosing and installing backends.
