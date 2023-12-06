import re


def find_symbols(file):
    symbols = [[False for i in range(142)] for j in range(142)]
    i = 1
    for row in file:
        row = row.strip("\n")
        j = 1
        for ch in row:
            if not ch.isnumeric() and ch != ".":
                symbols[i][j] = ch
            j += 1
        i += 1
    return symbols


def is_star_adjacent(item, symbols, row_number, col_number):
    is_symbol = False
    length = len(item)

    for i in range(3):
        for j in range(length+2):
            row_index = row_number-1+i
            col_index = col_number-1+j
            if symbols[row_index][col_index] == "*":
                return True, row_index, col_index

    return is_symbol, -1, -1


def process_input():
    with open("input.txt") as file:
        symbols = find_symbols(file)
    with open("input.txt") as file:
        star_number = [[list() for i in range(142)] for j in range(142)]

        row_number = 1
        for row in file:
            max_col = 0
            row = re.sub('\D', '.', row)
            items = row.split(".")
            for i in items:
                if i.isnumeric():
                    col_number = row.index(i, max_col) + 1
                    max_col = col_number
                    number = int(i)
                    is_star, star_row, star_col = is_star_adjacent(i, symbols, row_number, col_number)
                    if is_star:
                        star_number[star_row][star_col].append(number)

            row_number += 1

    sum_of_gears = 0
    for i in range(142):
        for j in range(142):
            if len(star_number[i][j]) == 2:
                sum_of_gears += star_number[i][j][0] * star_number[i][j][1]

    print("Sum :", sum_of_gears)


def main():
    process_input()


if __name__ == '__main__':
    main()