from typing import Tuple  # needed for type checks


def load_data() -> []:
    data = []
    with open('input.txt', 'r') as f:
        for line in f.read().split('\n'):
            data.append(line)

    return data


# Takes the data, converts F -> 0, and B -> 1 "binary", then converts that binary string to a base 10 integer
# Takes L -> 0 and R -> 1 and does the same.
# I really had to sit & think about this, it's been a few years since I've had to deal w/ binary
def get_row_and_column(input_data) -> Tuple[int, int]:
    return int(input_data[:7].replace('F', '0').replace('B', '1'), 2), int(
        input_data[7:].replace('L', '0').replace('R', '1'), 2)


def part_one(data):
    seats = []
    for seat_data in data:
        row, column = get_row_and_column(seat_data)
        # we multiply row by 8 since its given by AoC, not entirely sure why "8" is the magic number
        seat_id = row * 8 + column
        seats.append(seat_id)
    print(f"Maximum seat id: {max(seats)}")


# look for the missing seat id A ? C
def part_two(data):
    seats = []
    for seat_data in data:
        row, column = get_row_and_column(seat_data)
        seat_id = row * 8 + column
        seats.append(seat_id)
    # seat ids don't start at 0, they start at 89 for some reason so we have to min & max to not go out of bounds
    for i in range(min(seats), max(seats)):
        if i not in seats and i + 1 in seats and i - 1 in seats:
            print(f"My seat is {i}")


def run():
    data = load_data()
    part_one(data)
    part_two(data)


if __name__ == '__main__':
    run()
