from random import choice
from typing import List


def is_empty_string(string: str) -> bool:
    return string.isspace() or len(string) == 0


def sample_no_replace(seq: List[str]) -> str:
    result = choice(seq)
    seq.remove(result)
    return result
