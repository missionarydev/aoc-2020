import re

passport_data_keys = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
    # 'cid' We don't care about this per requirements
]

passport_data_valid_fields = {
    'byr': re.compile('^(19([2-9][0-9])|200[0-2])$'),
    'iyr': re.compile('^(201[0-9]|2020)$'),
    'eyr': re.compile('^(202[0-9]|2030)$'),
    'hgt': re.compile('^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$'),
    "hcl": re.compile('^#([0-9a-f]{6})$'),
    "ecl": re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$'),
    "pid": re.compile('^[0-9]{9}(?!\S)$'),
    "cid": re.compile('.*')
}


def run():
    loaded_data = load_data()
    valid_passports = 0
    valid_passports_two = 0
    for data in loaded_data:
        if check_for_required_fields(data):
            valid_passports += 1
        if validate_field_data(data):
            valid_passports_two += 1

    print(f"part 1: {valid_passports} valid passports \n"
          f"part 2: {valid_passports_two} valid passports")


def load_data() -> []:
    raw_data = []
    with open('input.txt', 'r') as f:
        for line in f.read().split('\n\n'):
            regexed = re.findall('([a-z]{3}):([0-9a-z#]+)', line)
            raw_data.append(regexed)

    return raw_data


def check_for_required_fields(data) -> bool:
    present_keys = [keys[0] for keys in data]
    for valid_key in passport_data_keys:
        if valid_key not in present_keys:
            return False

    return True


def validate_field_data(data) -> bool:
    if not check_for_required_fields(data):
        return False

    for field in data:
        key = field[0]
        value = field[1]
        if passport_data_valid_fields[key].match(value) is None:
            return False

    return True


if __name__ == '__main__':
    run()
