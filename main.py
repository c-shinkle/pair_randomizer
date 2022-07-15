from random import choice, sample


def main():
    raw_owners = input('Who owns a story? (Comma separated list)\n')
    owner_set = set(token.strip().lower() for token in raw_owners.split(','))
    if owner_set == {''}:
        owner_set = set()

    engineer_set = {
        'christian',
        'girish',
        'jason',
        'kyle',
        'manny',
        'niko',
        'tumsa',
        'tyler',
    }
    if not owner_set.issubset(engineer_set):
        print('The owners you listed are not a subset of the current team.')
        print('Check for typos or update the "engineers" set.')
        print(owner_set)
        return

    free_list = list(engineer_set - owner_set)
    owner_pairs = []

    for owner in owner_set:
        owner_pairs.append((owner, (sample_no_replace(free_list))))

    print("Here's the owner pairs:")
    print(owner_pairs)

    remaining_pairs = []
    while len(free_list) >= 2:
        remaining_pairs.append((sample_no_replace(free_list), sample_no_replace(free_list)))

    print("Here's the remaining pairs:")
    print(remaining_pairs)

    if len(free_list) == 1:
        print(f'{free_list[0]} is on his own!')


def sample_no_replace(seq):
    result = choice(seq)
    seq.remove(result)
    return result


if __name__ == '__main__':
    main()
