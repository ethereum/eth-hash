#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)

extras_require = {
    "test": [
        "pytest>=6.2.5,<7",
        "pytest-xdist>=2.4.0,<3",
        "tox>=3.14.6,<4",
    ],
    "lint": [
        "flake8==3.7.9",
        "isort>=4.2.15,<5",
        "mypy==0.961",
        "pydocstyle>=5.0.0,<6",
        "black>=22.0,<23",
    ],
    "doc": [
        "Sphinx>=5.0.0",
        "sphinx_rtd_theme>=1.0.0",
        "towncrier>=21,<22",
    ],
    "dev": [
        "bumpversion>=0.5.3,<1",
        "pytest-watch>=4.1.0,<5",
        "wheel",
        "twine",
        "ipython",
    ],
    # optional backends:
    "pycryptodome": [
        "pycryptodome>=3.6.6,<4",
    ],
    "pysha3": [
        "pysha3>=1.0.0,<2.0.0;python_version<'3.9'",
        "safe-pysha3>=1.0.0;python_version>='3.9'",
    ],
}

extras_require["dev"] = (
    extras_require["dev"]
    + extras_require["test"]
    + extras_require["lint"]
    + extras_require["doc"]
)


with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="eth-hash",
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version="0.5.1",
    description="""eth-hash: The Ethereum hashing function, keccak256, sometimes (erroneously) called sha3""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="The Ethereum Foundation",
    author_email="snakecharmers@ethereum.org",
    url="https://github.com/ethereum/eth-hash",
    include_package_data=True,
    python_requires=">=3.7, <4",
    extras_require=extras_require,
    py_modules=["eth_hash"],
    license="MIT",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"eth_hash": ["py.typed"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
