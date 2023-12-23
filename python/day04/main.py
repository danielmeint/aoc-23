def process_card(line):
    # example: "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    # ignore everything before colon
    colon_index = line.find(':')
    line = line[colon_index + 1:]
    line = line.strip()
    winners, chosen = line.split('|')
    # split by spaces (and ignore empty strings)
    winners = [int(x) for x in winners.split(' ') if x != '']
    chosen = [int(x) for x in chosen.split(' ') if x != '']

    # assert len(winners) == 5, f'winners: {winners}'
    # assert len(chosen) == 8, f'chosen: {chosen}'

    return winners, chosen


def calc_score(card):
    winners, chosen = card
    intersection = set(winners).intersection(set(chosen))
    matches = len(intersection)
    return 2 ** (matches - 1) if matches > 0 else 0


def solve_part_01(cards):
    return sum([
        calc_score(card)
        for card in cards
    ])


def solve_part_02(cards):
    copies = [1 for _ in range(len(cards))]

    matches = [
        len(set(winners).intersection(set(chosen)))
        for winners, chosen in cards
    ]

    for i in range(len(cards)):
        # add a copy for the subsequent cards according to the number of matches
        match_count = matches[i] # e.g., 2 --> the next 2 cards will get a copy
        for j in range(i + 1, i + 1 + match_count):
            copies[j] += copies[i]

    return sum(copies)


def main():
    lines = open("./input.txt", "r").readlines()

    cards = [
        process_card(line.strip())
        for line in lines
    ]

    print(solve_part_01(cards))
    print(solve_part_02(cards))


if __name__ == '__main__':
    main()
