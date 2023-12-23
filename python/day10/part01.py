momentum = (0, 1)


# "|" straight pipe, down or up
# "-" straight pipe, left or right
# "L" left curve, up or right
# "J"
# "7"
# "F"


def main():
    # parse input.txt
    lines = open("./input.txt", "r").readlines()
    maze = [
        [x for x in line.strip()]
        for line in lines
    ]

    # find start
    start = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
                break

    current = start
    momentum = (1, 0)  # down
    count = 0
    while True:
        print(f'current: {current}, momentum: {momentum}')

        # move
        current = (current[0] + momentum[0], current[1] + momentum[1])
        count += 1

        # check if turn
        current_char = maze[current[0]][current[1]]

        print(f'current: {current}, momentum: {momentum}, current_char: {current_char}')

        # if straight, continue
        if current_char == '|':
            continue
        if current_char == '-':
            continue

        # if turn, change momentum
        if current_char == 'L':
            # down -> right
            if momentum == (1, 0):
                momentum = (0, 1)
            # left -> up
            elif momentum == (0, -1):
                momentum = (-1, 0)
            else:
                raise Exception('bad momentum')

        elif current_char == 'J':
            # down -> left
            if momentum == (1, 0):
                momentum = (0, -1)
            # right -> up
            elif momentum == (0, 1):
                momentum = (-1, 0)
            else:
                raise Exception('bad momentum')

        elif current_char == '7':
            # right -> down
            if momentum == (0, 1):
                momentum = (1, 0)
            # up -> left
            elif momentum == (-1, 0):
                momentum = (0, -1)
            else:
                raise Exception('bad momentum')

        elif current_char == 'F':
            # up -> right
            if momentum == (-1, 0):
                momentum = (0, 1)
            # left -> down
            elif momentum == (0, -1):
                momentum = (1, 0)
            else:
                raise Exception('bad momentum')

        elif current_char == 'S':
            # end
            break

    solution = count // 2
    print(solution)


if __name__ == '__main__':
    main()
