def parse_round(round):
    # 3 blue, 4 red
    # return a dictionary of colors and counts
    count_color = round.split(',')  # ['3 blue', '4 red']
    count_color = [x.strip() for x in count_color]  # ['3 blue', '4 red']
    colors = [x.split(' ')[1] for x in count_color]  # ['blue', 'red']
    counts = [int(x.split(' ')[0]) for x in count_color]  # [3, 4]
    return dict(zip(colors, counts))  # {'blue': 3, 'red': 4}


def parse_game(game):
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # find first colon and ignore everything before it
    colon_index = game.find(':')
    game = game[colon_index + 1:]
    rounds = game.split(';')
    rounds = [round.strip() for round in rounds]
    rounds = [parse_round(round) for round in rounds]
    return rounds


def compute_game_power(game):
    # find max per color across all rounds
    max_per_color = {}
    for round in game:
        for color, count in round.items():
            if color not in max_per_color:
                max_per_color[color] = count
            else:
                max_per_color[color] = max(max_per_color[color], count)

    # compute power, i.e., multiply all maxes
    power = 1
    for color, count in max_per_color.items():
        power *= count
    return power


def solve_part_02(games):
    game_powers = [
        compute_game_power(game)
        for game in games
    ]
    return sum(game_powers)


def main():
    lines = open("./input.txt", "r").readlines()

    games = [
        parse_game(line.strip())
        for line in lines
    ]

    assert len(games) == 100

    print(solve_part_01(games))
    print(solve_part_02(games))


def solve_part_01(games):
    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    max_allowed = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    def is_valid_game(game):
        # check if each round is valid
        for round in game:
            for color, count in round.items():
                if count > max_allowed[color]:
                    return False
        return True

    is_valid = [
        is_valid_game(game)
        for game in games
    ]
    assert len(games) == len(is_valid), f'len(games): {len(games)}, len(is_valid): {len(is_valid)}'
    return sum(i + 1 for i, x in enumerate(is_valid) if x)


if __name__ == '__main__':
    main()
