from utils import parse_input_to_set, sample_no_replace


def main():
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

    missing_set: set[str] | None = parse_input_to_set('Who is gone today? (Comma separated list)\n',
                                                      all_engineer_set)
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


if __name__ == '__main__':
    main()
