from typing import Tuple


def load_data(debug) -> {}:
    data = []
    file = "test.txt" if debug else "input.txt"
    with open(file, 'r') as f:
        for line in f.read().split('\n'):
            data.append(line)

    return data


# Originally wrote this in java (https://gist.github.com/missionarydev/d54ed59bc3eff3cbedeacaf4df8b750c)
def part_one(data):
    accumulator = 0
    index = 0
    already_seen = set()
    while index not in already_seen and index < len(data):
        instructions = data[index].split(' ')
        operation = instructions[0]
        op_value = int(instructions[1])
        already_seen.add(index)
        if operation == "acc":
            accumulator += op_value
            index += 1
        elif operation == "jmp":
            index += op_value
        elif operation == "nop":
            index += 1
    print(accumulator)


def part_two(data):
    copy_data = data.copy()
    for i in range(len(copy_data)):
        ddata = copy_data[i].split(' ')
        instruction = ddata[0]
        if instruction == "jmp":
            copy_data[i] = f"nop {ddata[1]}"
        elif instruction == "nop":
            copy_data[i] = f"jmp {ddata[1]}"

        completion_data = can_complete(copy_data)
        print(completion_data)
        if completion_data[0] is True:
            print(f"Completed @ {completion_data[1]}")
        else:
            continue


def can_complete(data) -> Tuple[bool, int]:
    accumulator = 0
    index = 1
    already_seen = set()
    while index:
        if index in already_seen:
            return False, accumulator
        instructions = data[index].split(' ')
        operation = instructions[0]
        op_value = int(instructions[1])
        already_seen.add(index)
        if operation == "acc":
            accumulator += op_value
            index += 1
        elif operation == "jmp":
            index += op_value
        elif operation == "nop":
            index += 1
    return True, accumulator


def run(debug=False):
    data = load_data(debug)
    part_one(data)
    part_two(data)


if __name__ == '__main__':
    run(debug=False)
