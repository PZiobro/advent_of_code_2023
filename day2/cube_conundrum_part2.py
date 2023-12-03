
def get_power_of_game(game):
    game_cube = {
        'red': 0,
        'green': 0,
        'blue': 0

    }
    game_results = game[game.find(":")+2:].split("; ")
    for g in game_results:
        cubes = g.split(", ")
        for c in cubes:
            number, color = c.strip("\n").split(" ")
            if int(number) > game_cube[color]:
                game_cube[color] = int(number)
    power = 1
    for key, value in game_cube.items():
        power *= value

    return power


def process_input():
    power_of_games = 0
    with open("input.txt") as file:
        for game in file:
            print(game, get_power_of_game(game))
            power_of_games += get_power_of_game(game.strip("\n"))
    print('Sum of idexes of possible game: ', power_of_games)


def main():
    process_input()


if __name__ == '__main__':
    main()