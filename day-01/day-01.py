numbers = []


def run():
    with open("day-01-input.txt", 'r') as f:
        for line in f:
            numbers.append(int(line))
    part_1()
    part_2()


def part_1():
    for a in numbers:
        for b in numbers:
            if a + b == 2020:
                print(a * b)
                return


def part_2():
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if a + b + c == 2020:
                    print(a * b * c)
                    return


if __name__ == '__main__':
    run()
