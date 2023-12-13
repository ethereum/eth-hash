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

Read more in the [documentation on ReadTheDocs](https://eth-hash.readthedocs.io/). [View the change log](https://eth-hash.readthedocs.io/en/latest/release_notes.html).

## Quickstart

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

## Developer Setup

If you would like to hack on eth-hash, please check out the [Snake Charmers
Tactical Manual](https://github.com/ethereum/snake-charmers-tactical-manual)
for information on how we do:

- Testing
- Pull Requests
- Documentation

We use [pre-commit](https://pre-commit.com/) to maintain consistent code style. Once
installed, it will run automatically with every commit. You can also run it manually
with `make lint`. If you need to make a commit that skips the `pre-commit` checks, you
can do so with `git commit --no-verify`.

### Development Environment Setup

You can set up your dev environment with:

```sh
git clone git@github.com:ethereum/eth-hash.git
cd eth-hash
python -m virtualenv venv
. venv/bin/activate
python -m pip install -e ".[dev]"
pre-commit install
```

### Release setup

To release a new version:

```sh
make release bump=$$VERSION_PART_TO_BUMP$$
```

#### How to bumpversion

The version format for this repo is `{major}.{minor}.{patch}` for stable, and
`{major}.{minor}.{patch}-{stage}.{devnum}` for unstable (`stage` can be alpha or beta).

To issue the next version in line, specify which part to bump,
like `make release bump=minor` or `make release bump=devnum`. This is typically done from the
master branch, except when releasing a beta (in which case the beta is released from master,
and the previous stable branch is released from said branch).

If you are in a beta version, `make release bump=stage` will switch to a stable.

To issue an unstable version when the current version is stable, specify the
new version explicitly, like `make release bump="--new-version 4.0.0-alpha.1 devnum"`
