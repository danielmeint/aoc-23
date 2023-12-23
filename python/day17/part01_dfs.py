import heapq


def compute_all_paths(heat_map, start, end):
    # compute all paths from start to end without stepping in the same direction for more than three steps
    ROWS = len(heat_map)
    COLS = len(heat_map[0])

    # initialize previous
    previous = [
        [None for _ in range(COLS)]
        for _ in range(ROWS)
    ]


def find_least_heat_loss(grid):
    def get_neighbors(pos, direction, moves):
        row, col = pos
        neighbors = []

        # Directions: 0 = up, 1 = right, 2 = down, 3 = left
        # Mapping direction to row, col changes
        direction_changes = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Continue straight (if less than 3 moves in the same direction)
        if moves < 3:
            d_row, d_col = direction_changes[direction]
            new_pos = (row + d_row, col + d_col)
            neighbors.append((new_pos, direction, moves + 1))

        # Turn left
        left_direction = (direction - 1) % 4
        d_row, d_col = direction_changes[left_direction]
        new_pos = (row + d_row, col + d_col)
        neighbors.append((new_pos, left_direction, 1))

        # Turn right
        right_direction = (direction + 1) % 4
        d_row, d_col = direction_changes[right_direction]
        new_pos = (row + d_row, col + d_col)
        neighbors.append((new_pos, right_direction, 1))

        return neighbors

    start = (0, 0, None, 0)  # (row, col, direction, moves)
    end = (len(grid) - 1, len(grid[0]) - 1)
    visited = set()
    heap = [(0, start)]  # (cost, position)

    while heap:
        cost, (row, col, direction, moves) = heapq.heappop(heap)
        if (row, col) == end:
            return cost
        if (row, col, direction) in visited:
            continue
        visited.add((row, col, direction))

        for next_pos in get_neighbors((row, col), direction, moves):
            next_cost = cost + grid[next_pos[0]][next_pos[1]]
            heapq.heappush(heap, (next_cost, next_pos))

    return float('inf')  # No path found


def find_all_paths(heat_map, start, end):
    def backtrack(current, path):
        if current == end:
            all_paths.append(path.copy())
            return

        for neighbor in graph[current]:
            if neighbor not in path:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()

    all_paths = []
    backtrack(start, [start])
    return all_paths


def main():
    # parse input.txt
    lines = open("./input.txt", "r").readlines()
    heat_map = [
        [int(x) for x in line.strip()]
        for line in lines
    ]

    ROWS = len(heat_map)
    COLS = len(heat_map[0])

    start = (0, 0)
    end = (ROWS - 1, COLS - 1)

    # compute all paths
    # paths = compute_all_paths(heat_map, start, end)
    find_least_heat_loss(heat_map)


if __name__ == '__main__':
    main()
