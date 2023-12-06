import re


def find_symbols(file):
    symbols = [[False for i in range(142)] for j in range(142)]
    i = 1
    for row in file:
        row = row.strip("\n")
        j = 1
        for ch in row:
            if not ch.isnumeric() and ch != ".":
                symbols[i][j] = True
            j += 1
        i += 1
    return symbols


def is_symbol_adjacent(item, symbols, row_number, col_number):
    is_symbol = False
    length = len(item)

    for i in range(3):
        for j in range(length+2):
            row_index = row_number-1+i
            col_index = col_number-1+j
            if symbols[row_index][col_index]:
                is_symbol = True

    return is_symbol


def process_row(row, symbols, row_number):
    sum_of_numbers = 0
    max_col = 0
    row = re.sub('\D', '.', row)
    items = row.split(".")
    for i in items:
        if i.isnumeric():
            col_number = row.index(i, max_col)+1
            max_col = col_number
            number = int(i)
            if is_symbol_adjacent(i, symbols, row_number, col_number):
                sum_of_numbers += number

    return sum_of_numbers


def process_input():
    sum_of_engine = 0
    with open("input.txt") as file:
        symbols = find_symbols(file)
    with open("input.txt") as file:
        row_number = 1
        for row in file:
            sum_of_engine += process_row(row, symbols, row_number)
            row_number += 1
    print('Sum of numbers: ', sum_of_engine)


def main():
    process_input()


if __name__ == '__main__':
    main()