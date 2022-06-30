Release Notes
=============

.. towncrier release notes start

eth-hash v0.3.3 (2022-06-30)
----------------------------
Eth_Hash 0.3.3 (2022-06-30)
---------------------------

Performance improvements
~~~~~~~~~~~~~~~~~~~~~~~~

- Keccak backend was initialized every time it was called. Now it's initialized only the first time it's called. (`#36 <https://github.com/ethereum/eth-hash/issues/36>`__)


Internal Changes - for eth-hash Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Prune ``venv`` files from the release via MANIFEST.in (`#38 <https://github.com/ethereum/eth-hash/issues/38>`__)


eth-hash v0.3.2 (2021-09-03)
----------------------------

Miscellaneous changes
~~~~~~~~~~~~~~~~~~~~~

- Drop eth-utils requirement, to fix dependency cycle (`#33 <https://github.com/ethereum/eth-hash/issues/33>`__)


eth-hash v0.3.1 (2021-01-21)
----------------------------

Bugfixes
~~~~~~~~

- Bugfix to export type annotations (`#28 <https://github.com/ethereum/eth-hash/issues/28>`__)


eth-hash v0.3.0 (2021-01-20)
----------------------------

Features
~~~~~~~~

- Export type annotations, for use in importing projects (`#29 <https://github.com/ethereum/eth-hash/issues/29>`__)


Internal Changes - for eth-hash Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Import 3 years worth of template updates (`#29 <https://github.com/ethereum/eth-hash/issues/29>`__)


v0.2.0
--------------

Released September 5, 2018

- set `pycryptodome` version to `>=3.6.6,<4` to fix a recently discovered vulnerability

v0.1.4
--------------

Released May 28, 2018

- Ensure the auto backend is pickleable (#19)



v0.1.3
--------------

Released May 14, 2018

- The pycryptodome backend now allows ``update()``, then ``digest()``, then ``update()``.

v0.1.2
--------------

Released Apr 2, 2018

- You can now import eth-hash without a backend, it won't fail until trying to generate a hash

v0.1.1
--------------

Released Mar 15, 2018

- upgrade pycryptodome to v3.5.1+
- performance improvements with preimage
- Better docs and tests

v0.1.0
--------------

Released Feb 28, 2018

- Add support for :class:`bytearray` input to keccak
- Add support for incrementally building hash results

v0.1.0-alpha.3
--------------

Released Feb 7, 2018

- Add pycryptodome backend support
- Add pysha3 backend support
- Can specify backend in environment variable ``ETH_HASH_BACKEND``
- New :ref:`Quickstart` docs

v0.1.0-alpha.2
--------------

Released Feb 6, 2018

- Bugfix pypy3 reference in pypi

v0.1.0-alpha.1
--------------

- Launched repository, claimed names for pip, RTD, github, etc
