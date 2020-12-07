def load_data() -> {}:
    data = set()
    with open('input.txt', 'r') as f:
        for line in f.read().split('\n\n'):
            data.add(line.replace('\n', ''))  # have to also get rid of blank spaces in input data

    return data


def part_one(data):
    count = 0
    # iterate through all of the groups of people
    for group in data:
        # for each person in a distinct group (meaning no duplicate values per group)
        for person in set(group):
            # count the number of responses per person
            count += len(person)
    print(count)

def run():
    data = load_data()
    part_one(data)
    # part_two(data)


if __name__ == '__main__':
    run()
