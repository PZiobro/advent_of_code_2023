

def get_points_from_card(card):
    card_index = int(card[card.find("Card ")+5:card.find(":")])
    all_numbers = card[card.find(":") + 1:].split("|")

    winning_numbers = list(filter(None, all_numbers[0].split(' ')))
    elf_numbers = list(filter(None, all_numbers[1].split(' ')))

    set1 = set(winning_numbers)
    set2 = set(elf_numbers)
    intersection = set1.intersection(set2)
    number_of_winning_numbers = len(intersection)
    return card_index, number_of_winning_numbers


def process_input():
    cards_dict = {}
    final_number_of_cards = 0
    for i in range(1, 204):
        cards_dict[i] = 1
    with open("input.txt") as file:
        for card in file:
            card_index, number_of_winning_numbers = get_points_from_card(card.strip("\n"))
            current_number_of_cards = cards_dict[card_index]
            for j in range(1, current_number_of_cards+1):
                for i in range(1, number_of_winning_numbers+1):
                    cards_dict[card_index+i] += 1
    for v in cards_dict.values():
        final_number_of_cards += v
    print("Total scratchcards: ", final_number_of_cards)


def main():
    process_input()


if __name__ == '__main__':
    main()