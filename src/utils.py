from random import choice
from typing import List, Optional, Set


def parse_input_to_set(prompt: str, engineer_set: Set[str]) -> Optional[Set[str]]:
    raw_input = input(prompt)
    input_set = set(token.strip().lower() for token in raw_input.split(',') if not is_empty_string(token))
    if input_set.issubset(engineer_set):
        return input_set
    else:
        print('The engineers you listed are not a subset of the current team.')
        print('Check for typos or update "all_engineers_set".')
        print(input_set)
        return None


def is_empty_string(string: str) -> bool:
    return string.isspace() or len(string) == 0


def sample_no_replace(seq: List[str]) -> str:
    result = choice(seq)
    seq.remove(result)
    return result
