data = []


def load_data():
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            data.append(line.strip())


def part_one(dy, dx) -> int:
    tree_count = 0
    right = 0
    size = len(data[0])
    # iterate through the range from 0 to length of 'data', stepping 1 value each iteration
    for i in range(0, len(data), dy):
        if data[i][right] == '#':
            tree_count += 1
        right = (right + dx) % size  # if step over three each iteration staying in the bounds
    return tree_count


def part_two():
    positions = {
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    }

    values = []
    for position in positions:
        num = part_one(position[1], position[0])  # part_one takes dy then dx
        values.append(num)

    product = 1
    for val in values:
        product *= val

    print(product)


if __name__ == '__main__':
    load_data()
    print(part_one(1, 3))
    part_two()
