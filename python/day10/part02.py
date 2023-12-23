import sys
# "|" straight pipe, down or up
# "-" straight pipe, left or right
# "L" left curve, up or right
# "J"
# "7"
# "F"


def print_maze(maze):
    for row in maze:
        print(''.join(row))


def main():
    sys.setrecursionlimit(3000)

    # parse input.txt
    lines = open("./input.txt", "r").readlines()
    maze = [
        [x for x in line.strip()]
        for line in lines
    ]

    ROWS = len(maze)
    COLS = len(maze[0])

    # find start
    start = None
    for i in range(ROWS):
        for j in range(COLS):
            if maze[i][j] == 'S':
                start = (i, j)
                break

    relevant = [
        [False for _ in range(COLS)]
        for _ in range(ROWS)
    ]

    current = start
    momentum = (1, 0)  # down

    while True:
        relevant[current[0]][current[1]] = True

        # move
        current = (current[0] + momentum[0], current[1] + momentum[1])

        # check if turn
        current_char = maze[current[0]][current[1]]

        # print(f'current: {current}, momentum: {momentum}, current_char: {current_char}')

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

    # clean maze
    for i in range(ROWS):
        for j in range(COLS):
            if not relevant[i][j]:
                maze[i][j] = '.'

    # print maze
    print_maze(maze)


    def dfs(start, mark):
        if not (0 <= start[0] < ROWS and 0 <= start[1] < COLS):
            return
        print(f'start: {start}, mark: {mark}, current_char: {maze[start[0]][start[1]]}')
        if maze[start[0]][start[1]] != '.':
            return
        maze[start[0]][start[1]] = mark
        # start dfs to all 4 directions
        dfs((start[0] + 1, start[1]), mark)
        dfs((start[0] - 1, start[1]), mark)
        dfs((start[0], start[1] + 1), mark)
        dfs((start[0], start[1] - 1), mark)

    LEFT = 'X'
    RIGHT = 'Y'

    # traverse maze again
    current = start
    momentum = (1, 0)  # down

    while True:
        # move
        current = (current[0] + momentum[0], current[1] + momentum[1])
        current_char = maze[current[0]][current[1]]

        print(f'current: {current}, momentum: {momentum}, current_char: {current_char}')

        # if straight, continue
        if current_char == '|':
            print(f'straight: {current}')
            # start dfs to both sides orthogonal to momentum, mark which side of current direction it is, i.e.,
            # left or right
            if momentum == (1, 0):
                # down, i.e. "right is left" and "left is right"
                # start dfs to left
                dfs_start_left = (current[0], current[1] + 1)
                dfs(dfs_start_left, LEFT)
                # start dfs to right
                dfs_start_right = (current[0], current[1] - 1)
                dfs(dfs_start_right, RIGHT)
            elif momentum == (-1, 0):
                # up, i.e. "right is right" and "left is left"
                # start dfs to left
                dfs_start_left = (current[0], current[1] - 1)
                dfs(dfs_start_left, LEFT)
                # start dfs to right
                dfs_start_right = (current[0], current[1] + 1)
                dfs(dfs_start_right, RIGHT)
            else:
                raise Exception('bad momentum')
            continue
        if current_char == '-':
            print(f'straight: {current}')
            # start dfs to both sides orthogonal to momentum, mark which side of current direction it is, i.e., left or right
            if momentum == (0, 1):
                # right, i.e., "up is left" and "down is right"
                # start dfs to left
                dfs_start_left = (current[0] - 1, current[1])
                dfs(dfs_start_left, LEFT)
                # start dfs to right
                dfs_start_right = (current[0] + 1, current[1])
                dfs(dfs_start_right, RIGHT)
            elif momentum == (0, -1):
                # left, i.e., "up is right" and "down is left"
                # start dfs to left
                dfs_start_left = (current[0] + 1, current[1])
                dfs(dfs_start_left, LEFT)
                # start dfs to right
                dfs_start_right = (current[0] - 1, current[1])
                dfs(dfs_start_right, RIGHT)
            else:
                raise Exception('bad momentum')
            continue

        # if turn, change momentum
        if current_char == 'L':
            # down -> right
            if momentum == (1, 0):
                # start dfs to "right"
                dfs_start_right_side = (current[0], current[1] - 1)
                dfs(dfs_start_right_side, RIGHT)
                dfs_start_right_bottom = (current[0] + 1, current[1])
                dfs(dfs_start_right_bottom, RIGHT)
                momentum = (0, 1)
            # left -> up
            elif momentum == (0, -1):
                # start dfs to "left"
                dfs_start_left_side = (current[0], current[1] - 1)
                dfs(dfs_start_left_side, LEFT)
                dfs_start_left_top = (current[0] + 1, current[1])
                dfs(dfs_start_left_top, LEFT)
                momentum = (-1, 0)
            else:
                raise Exception('bad momentum')

        elif current_char == 'J':
            # down -> left
            if momentum == (1, 0):
                # start dfs to "left"
                dfs_start_left_side = (current[0], current[1] + 1)
                dfs(dfs_start_left_side, LEFT)
                dfs_start_left_bottom = (current[0] + 1, current[1])
                dfs(dfs_start_left_bottom, LEFT)
                momentum = (0, -1)
            # right -> up
            elif momentum == (0, 1):
                # start dfs to "right"
                dfs_start_right_side = (current[0], current[1] + 1)
                dfs(dfs_start_right_side, RIGHT)
                dfs_start_right_top = (current[0] + 1, current[1])
                dfs(dfs_start_right_top, RIGHT)
                momentum = (-1, 0)
            else:
                raise Exception('bad momentum')

        elif current_char == '7':
            # right -> down
            if momentum == (0, 1):
                # start dfs to "left"
                dfs_start_left_side = (current[0], current[1] + 1)
                dfs(dfs_start_left_side, LEFT)
                dfs_start_left_top = (current[0] - 1, current[1])
                dfs(dfs_start_left_top, LEFT)
                momentum = (1, 0)
            # up -> left
            elif momentum == (-1, 0):
                # start dfs to "right"
                dfs_start_right_side = (current[0], current[1] + 1)
                dfs(dfs_start_right_side, RIGHT)
                dfs_start_right_bottom = (current[0] - 1, current[1])
                dfs(dfs_start_right_bottom, RIGHT)
                momentum = (0, -1)
            else:
                raise Exception('bad momentum')

        elif current_char == 'F':
            # up -> right
            if momentum == (-1, 0):
                # start dfs to "left"
                dfs_start_left_side = (current[0], current[1] - 1)
                dfs(dfs_start_left_side, LEFT)
                dfs_start_left_top = (current[0] - 1, current[1])
                dfs(dfs_start_left_top, LEFT)
                momentum =(0, 1)
            # left -> down
            elif momentum == (0, -1):
                # start dfs to "right"
                dfs_start_right_side = (current[0], current[1] - 1)
                dfs(dfs_start_right_side, RIGHT)
                dfs_start_right_bottom = (current[0] - 1, current[1])
                dfs(dfs_start_right_bottom, RIGHT)
                momentum = (1, 0)
            else:
                raise Exception('bad momentum')

        elif current_char == 'S':
            # end
            break

    # print maze
    print_maze(maze)

    # assert there is no '.' left
    assert all([all([x != '.' for x in row]) for row in maze]), f'there are still {sum([row.count(".") for row in maze])} "."s left'

    # print number of X and Ys
    print (sum([row.count(LEFT) for row in maze]))
    print (sum([row.count(RIGHT) for row in maze]))


if __name__ == '__main__':
    main()
