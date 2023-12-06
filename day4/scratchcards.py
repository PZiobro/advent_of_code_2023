

def get_points_from_card(card):
    card_index = int(card[card.find("Card ")+5:card.find(":")])
    all_numbers = card[card.find(":") + 1:].split("|")

    winning_numbers = list(filter(None, all_numbers[0].split(' ')))
    elf_numbers = list(filter(None, all_numbers[1].split(' ')))

    set1 = set(winning_numbers)
    set2 = set(elf_numbers)
    intersection = set1.intersection(set2)
    number_of_winning_numbers = len(intersection)

    if number_of_winning_numbers > 0:
        points = pow(2, number_of_winning_numbers-1)
    else:
        points = 0

    return points


def process_input():
    sum_of_points = 0
    with open("input.txt") as file:
        for card in file:
            sum_of_points += get_points_from_card(card.strip("\n"))
    print('Sum of winning points: ', sum_of_points)


def main():
    process_input()


if __name__ == '__main__':
    main()