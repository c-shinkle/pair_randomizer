from random import choice
from typing import Set, List, Optional


def main():
    all_engineer_set = {
        'christian',
        'eric',
        'girish',
        'jason',
        'kyle',
        'manny',
        'niko',
        'tumsa',
        'tyler',
    }

    missing_set = parse_input_to_set('Who is gone today? (Comma separated list)\n', all_engineer_set)
    if missing_set is None:
        return

    working_engineer_set = all_engineer_set - missing_set

    owner_set = parse_input_to_set('Who owns a story? (Comma separated list)\n', all_engineer_set)
    if owner_set is None:
        return

    free_engineers = list(working_engineer_set - owner_set)

    pairs = [(owner, sample_no_replace(free_engineers)) for owner in owner_set]
    while len(free_engineers) >= 2:
        pairs.append((sample_no_replace(free_engineers), sample_no_replace(free_engineers)))

    print("Here's the pairs:")
    for pair in pairs:
        print(f'{pair[0]} + {pair[1]}')

    if len(free_engineers) == 1:
        print(f'{free_engineers[0]} is on his own!')


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


if __name__ == '__main__':
    main()
