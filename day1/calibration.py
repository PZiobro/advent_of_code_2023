
def get_digit_from_line(line, reserved_direction=False):
    if reserved_direction:
        line = line[::-1]
    keep_search = True
    i = 0
    while keep_search:
        if line[i].isdigit():
            keep_search = True
            return int(line[i])
        i += 1


def process_file():
    result = 0
    with open("input.txt") as file:
        for line in file:
            first = get_digit_from_line(line)
            last = get_digit_from_line(line, True)
            number = first * 10 + last
            result += number
    return result


def main():
    print(process_file())


if __name__ == '__main__':
    main()