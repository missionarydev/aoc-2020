import re

raw_data = []
data = []


# isn't really needed, looks clean, you can tell i'm a java programmer :-)
class PasswordRequirements:
    def __init__(self, minimum, maximum, character, password):
        self.minimum = minimum
        self.maximum = maximum
        self.character = character
        self.password = password


def load_data():
    with open("input.txt", 'r') as f:
        for line in f:
            raw_data.append(str(line))

    for string in raw_data:
        numbers = re.search("^(\d{1,})+-(\d{1,})+ (\w)", string)
        minimum = int(numbers.group(1))
        maximum = int(numbers.group(2))
        character = numbers.group(3)
        password = string.rstrip().split(":")[1].lstrip()  # todo use regex (couldn't figure out pattern, not familiar)
        data.append(PasswordRequirements(minimum, maximum, character, password))


def part_one():
    counter = 0
    for requirements in data:
        if requirements.minimum <= requirements.password.count(requirements.character) <= requirements.maximum:
            counter += 1

    print(counter)


def part_two():
    count = 0
    for requirements in data:
        # zero index
        position_a = requirements.minimum - 1
        position_b = requirements.maximum - 1

        # XOR check (only allow one of the operands to be true)
        if (requirements.password[position_a] == requirements.character) ^ (requirements.password[
                                                                                position_b] == requirements.character):
            count += 1

    print(count)


if __name__ == '__main__':
    load_data()
    part_one()
    part_two()
