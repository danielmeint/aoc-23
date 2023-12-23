import math


def read_input(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


START = 'AAA'
END = 'ZZZ'


def solve_part_1():
    # read input.txt
    lines = read_input('/Users/d.meint/projects/personal/advent-of-code/aoc-23/python/day08/input.txt')

    path = lines[0]

    parent_to_children = {}

    # example: JKT = (KFV, CFQ)
    for line in lines[2:]:
        parent, children = line.split(' = ')
        # remove ( and )
        children = children[1:-1]
        children = children.split(', ')
        parent_to_children[parent] = children

    direction_to_index = {
        'L': 0,
        'R': 1,
    }

    steps = 0
    current = START
    while current != END:
        path_index = steps % len(path)
        direction = path[path_index]
        index = direction_to_index[direction]
        current = parent_to_children[current][index]
        steps += 1

    print(steps)


def compute_cycle_length(start, parent_to_children, instructions):
    direction_to_index = {
        'L': 0,
        'R': 1,
    }

    steps = 0
    current = start
    while not current.endswith('Z'):
        path_index = steps % len(instructions)
        direction = instructions[path_index]
        index = direction_to_index[direction]
        current = parent_to_children[current][index]
        steps += 1

    return steps


def solve_part_2():
    # read input.txt
    lines = read_input('/Users/d.meint/projects/personal/advent-of-code/aoc-23/python/day08/input.txt')

    instructions = lines[0]

    parent_to_children = {}

    # example: JKT = (KFV, CFQ)
    for line in lines[2:]:
        parent, children = line.split(' = ')
        # remove ( and )
        children = children[1:-1]
        children = children.split(', ')
        parent_to_children[parent] = children

    # all nodes that end with A
    all_starting_points = [node for node in parent_to_children.keys() if node.endswith('A')]

    cycle_lenghts = [compute_cycle_length(start, parent_to_children, instructions) for start in all_starting_points]

    # get least common multiple of cycle lengths
    res = math.lcm(*cycle_lenghts)
    return res




def is_goal(current_nodes):
    for node in current_nodes:
        if not node.endswith('Z'):
            return False
    return True


def main():
    solve_part_1()
    print(solve_part_2())


if __name__ == '__main__':
    main()
