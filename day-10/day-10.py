def load_data(debug) -> {}:
    data = []
    file = "input.txt" if debug else "input.txt"
    with open(file, 'r') as f:
        for line in f.read().split('\n'):
            data.append(line)
            if debug:
                print(line)

    return data


def run(debug=False):
    data = load_data(debug)
    # part_one(data)
    # part_two(data)


if __name__ == '__main__':
    run(debug=True)
