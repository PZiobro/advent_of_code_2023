CUBE_SETTINGS = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def check_results(game_cube):
    possible = True
    for key, value in game_cube.items():
        if game_cube[key] > CUBE_SETTINGS[key]:
            possible = False
    return possible


def get_idx_game_if_possible(game):
    possible = True
    game_index = int(game[game.find("Game ")+5:game.find(":")])
    game_results = game[game.find(":")+2:].split("; ")
    for g in game_results:
        game_cube = {
            'red': 0,
            'green': 0,
            'blue': 0

        }
        cubes = g.split(", ")
        for c in cubes:
            number, color = c.split(" ")
            game_cube[color] += int(number)

        for key, value in game_cube.items():
            if game_cube[key] > CUBE_SETTINGS[key]:
                possible = False
                return 0

    if possible:
        return game_index


def process_input():
    sum_of_game_idx = 0
    with open("input.txt") as file:
        for game in file:
            sum_of_game_idx += get_idx_game_if_possible(game.strip("\n"))
    print('Sum of idexes of possible game: ', sum_of_game_idx)


def main():
    process_input()


if __name__ == '__main__':
    main()