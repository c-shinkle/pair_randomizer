from src.utils import sample_no_replace, is_empty_string

all_engineer_set = {
    'christian',
    'girish',
    'jason',
    'kyle',
    'manny',
    'niko',
    'tumsa',
    'tyler',
}


def main():
    raw_missing = input('Who is gone today? (Comma separated list)\n')
    missing_set = set(token.strip().lower() for token in raw_missing.split(',') if not is_empty_string(token))
    if not missing_set.issubset(all_engineer_set):
        print('The engineers you listed are not a subset of the current team.')
        print('Check for typos or update "all_engineers_set".')
        print(missing_set)
        return

    working_engineer_set = all_engineer_set - missing_set

    raw_owners = input('Who owns a story? (Comma separated list)\n')
    owner_set = set(token.strip().lower() for token in raw_owners.split(',') if not is_empty_string(token))
    if not owner_set.issubset(all_engineer_set):
        print('The engineers you listed are not a subset of the current team.')
        print('Check for typos or update "all_engineers_set".')
        print(owner_set)
        return

    free_engineer_list = list(working_engineer_set - owner_set)

    pairs = [(owner, sample_no_replace(free_engineer_list)) for owner in owner_set]
    while len(free_engineer_list) >= 2:
        pairs.append((sample_no_replace(free_engineer_list), sample_no_replace(free_engineer_list)))

    print("Here's the pairs:")
    for pair in pairs:
        print(f'{pair[0]} + {pair[1]}')

    if len(free_engineer_list) == 1:
        print(f'{free_engineer_list[0]} is on his own!')


if __name__ == '__main__':
    main()
