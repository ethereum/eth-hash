Quickstart
============

Choose a hashing backend
---------------------------

If you're not sure, choose "pycryptodome" because it supports pypy3.

You can find a full list of each currently supported backend in :mod:`eth_hash.backends`.

Install
----------

Put the backend you would like to use in brackets during install, like:

.. code-block:: shell

  pip install eth-hash[pycryptodome]

Compute a Keccak256 Hash
-----------------------------

.. doctest::

  >>> from eth_hash.auto import keccak
  >>> keccak(b'')
  b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';{\xfa\xd8\x04]\x85\xa4p"

Select one of many installed backends
---------------------------------------

If you have several backends installed, and you want to
specify which one to use, you can select it like so:

.. code-block:: python

  >>> from eth_hash.backends import pysha3
  >>> from eth_hash import Keccak256
  >>> keccak = Keccak256(pysha3)
  >>> keccak(b'')
  b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';{\xfa\xd8\x04]\x85\xa4p"
