
DIGITS_STR = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def get_list_of_numbers(line):
    list_of_chars = []
    for pos, character in enumerate(line):
        part_line = line[pos:]
        if part_line[0].isnumeric():
            list_of_chars.append(part_line[0])
        else:
            for nm in DIGITS_STR:
                if part_line.startswith(nm):
                    list_of_chars.append(str(DIGITS_STR.index(nm)+1))

    return list_of_chars


def process_file():
    result = 0
    with open("input.txt") as file:
        for line in file:
            list_of_numbers = get_list_of_numbers(line)
            first = int(list_of_numbers[0])
            last = int(list_of_numbers[-1])
            number = first * 10 + last
            result += number
    return result


def main():
    print(process_file())


if __name__ == '__main__':
    main()
