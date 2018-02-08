from eth_hash.main import (
    Keccak256,
)
from eth_hash.utils import (
    auto_choose_backend,
)

keccak = Keccak256(auto_choose_backend())
