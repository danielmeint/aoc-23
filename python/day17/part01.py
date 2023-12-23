import heapq
from enum import Enum


def get_neighbors(current, heat_map, disallowed_direction=None):
    # returns a list of neighbors of current
    if disallowed_direction:
        print(f'disallowed_direction: {disallowed_direction}')
    cur_row, cur_col = current
    neighbors = []
    # up
    if cur_row > 0 and disallowed_direction != (-1, 0):
        neighbors.append((cur_row - 1, cur_col))
    # down
    if cur_row < len(heat_map) - 1 and disallowed_direction != (1, 0):
        neighbors.append((cur_row + 1, cur_col))
    # left
    if cur_col > 0 and disallowed_direction != (0, -1):
        neighbors.append((cur_row, cur_col - 1))
    # right
    if cur_col < len(heat_map[0]) - 1 and disallowed_direction != (0, 1):
        neighbors.append((cur_row, cur_col + 1))

    return neighbors


def draw_path(heat_map, previous, start, end):
    # draw path from start to end
    ROWS = len(heat_map)
    COLS = len(heat_map[0])

    path_map = [
        [heat_map[i][j] for j in range(COLS)]
        for i in range(ROWS)
    ]
    current = end
    print(f'current: {current}')
    while current != start:
        path_map[current[0]][current[1]] = 'X'
        current = previous[current[0]][current[1]]

    path_map[start[0]][start[1]] = 'X'
    # print path_map
    for row in path_map:
        print(''.join([str(x) for x in row]))



def get_direction(previous, current):
    return (current[0] - previous[0], current[1] - previous[1])


def get_allowed_neighbors(current, heat_map, previous):
    # it is only allowed to take three steps in the same direction
    # in other words, if the "history" of the previous three steps are all in the same direction, then the next step
    # must be in a different direction; otherwise, the next step can be in any direction
    # to implement this, we need to track back the previous three steps
    step_directions = []
    current_direction = None
    if previous[current[0]][current[1]] is not None:
        # get current direction
        current_direction = get_direction(previous[current[0]][current[1]], current)
        # get previous three directions
        current_step = current
        for _ in range(3):
            if previous[current_step[0]][current_step[1]] is None:
                break
            step_directions.append(get_direction(previous[current_step[0]][current_step[1]], current_step))
            current_step = previous[current_step[0]][current_step[1]]

    print(f'current: {current}, current_direction: {current_direction}, step_directions: {step_directions}')

    if current_direction is None:
        return get_neighbors(current, heat_map)
    if len(step_directions) < 3:
        return get_neighbors(current, heat_map)
    # check if they are all the same
    if not all([x == current_direction for x in step_directions]):
        return get_neighbors(current, heat_map)
    # if they are all the same, return only neighbors in different directions
    disallowed_direction = current_direction
    return get_neighbors(current, heat_map, disallowed_direction=disallowed_direction)

    # return get_neighbors(current, heat_map, disallowed_direction=current_direction)


def find_shortest_path(heat_map, start, end):
    # dijkstra's algorithm
    # Input example:
    # 2413432311323
    # 3215453535623
    # 3255245654254
    distances = [
        [float('inf') for _ in range(len(heat_map[0]))]
        for _ in range(len(heat_map))
    ]
    distances[start[0]][start[1]] = 0
    previous = [
        [None for _ in range(len(heat_map[0]))]
        for _ in range(len(heat_map))
    ]

    def get_next(q):
        # return the next node to visit according to dijkstra's algorithm
        # q is a list of (node, distance)
        # return the node with the smallest distance
        min_distance = float('inf')
        min_node = None
        for node, distance in q:
            if distance < min_distance:
                min_distance = distance
                min_node = node
        q.remove((min_node, min_distance))
        return min_node, min_distance

    min_heap = [(start, 0)]
    heapq.heapify(min_heap)

    while len(min_heap) > 0:
        current, current_distance = heapq.heappop(min_heap)
        print(f'current: {current}, current_distance: {current_distance}')

        # check if done
        if current == end:
            # draw path
            draw_path(heat_map, previous, start, end)
            return current_distance

        # check if visited
        if current_distance > distances[current[0]][current[1]]:
            continue

        # check neighbors
        # neighbors = get_neighbors(current, heat_map)
        neighbors = get_allowed_neighbors(current, heat_map, previous)
        print(f'neighbors: {neighbors}')
        for neighbor in neighbors:
            # if neighbor is wall, skip
            if neighbor == -1:
                continue

            # if neighbor is not wall, check if distance is better
            neighbor_distance = current_distance + heat_map[neighbor[0]][neighbor[1]]
            if neighbor_distance < distances[neighbor[0]][neighbor[1]]:
                distances[neighbor[0]][neighbor[1]] = neighbor_distance
                previous[neighbor[0]][neighbor[1]] = current
                # q.append((neighbor, neighbor_distance))
                heapq.heappush(min_heap, (neighbor, neighbor_distance))


def main():
    # parse input.txt
    lines = open("./input.txt", "r").readlines()
    heat_map = [
        [int(x) for x in line.strip()]
        for line in lines
    ]

    ROWS = len(heat_map)
    COLS = len(heat_map[0])

    # dijkstra's algorithm
    find_shortest_path(heat_map, start=(0, 0), end=(ROWS - 1, COLS - 1))


if __name__ == '__main__':
    main()
