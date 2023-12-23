def solve_part_01(grid):
    ROWS = len(grid)
    COLS = len(grid[0])

    is_number = lambda x: x in '0123456789'
    is_number_grid = [
        [is_number(x) for x in row]
        for row in grid
    ]

    def is_symbol(i, j):
        if i < 0 or i >= ROWS:
            return False

        if j < 0 or j >= COLS:
            return False

        # anything that is not a number or '.'
        return not is_number_grid[i][j] and grid[i][j] != '.'

    def is_start_of_number(i, j):
        if not is_number_grid[i][j]:
            return False

        # if left is not number, then this is start of number
        if j == 0:
            return True

        return not is_number_grid[i][j - 1]

    is_start_of_number_grid = [
        [is_start_of_number(i, j) for j in range(COLS)]
        for i in range(ROWS)
    ]

    def get_number_starting_at(i, j):
        if not is_start_of_number_grid[i][j]:
            return None

        # get number
        number = ''
        while j < COLS and is_number_grid[i][j]:
            number += grid[i][j]
            j += 1

        return number

    def get_length_of_number_starting_at(i, j):
        if not is_start_of_number_grid[i][j]:
            return None

        # get number
        length = 0
        while j < COLS and is_number_grid[i][j]:
            length += 1
            j += 1

        return length

    def is_valid_number_starting_at(i, j):
        if not is_start_of_number_grid[i][j]:
            return False

        # check if any of the surrounding spots is a symbol, including diagonals
        for row_offset in [-1, 0, 1]:
            number_length = get_length_of_number_starting_at(i, j)  # e.g., 3 --> col_offset = [-1, 0, 1, 2, 3]
            # for col_offset in range(-1, number_length + 1):
            for col_offset in range(-1, number_length + 1):
                if is_symbol(i + row_offset, j + col_offset):
                    return True

        return False

    valid_numbers = []
    for row in range(ROWS):
        for col in range(COLS):
            if is_valid_number_starting_at(row, col):
                valid_numbers.append(int(get_number_starting_at(row, col)))

    return sum(valid_numbers)


def solve_part_02(grid):
    ROWS = len(grid)
    COLS = len(grid[0])

    def is_number(i, j):
        if i < 0 or i >= ROWS:
            return False

        if j < 0 or j >= COLS:
            return False

        return grid[i][j] in '0123456789'

    def find_starting_indices_for_number_at(row, col):
        if not is_number(row, col):
            return None

        # find start of number
        while col >= 0 and is_number(row, col):
            col -= 1

        col += 1

        return row, col

    def get_number_starting_at(row, col):
        if not is_number(row, col):
            return None

        # get number
        number = ''
        while col < COLS and is_number(row, col):
            number += grid[row][col]
            col += 1

        return int(number)

    def find_adjacent_numbers_unique(row, col):
        adjacent_numbers_starting_indices = set()  # (row, col)
        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:
                if row_offset == 0 and col_offset == 0:
                    continue

                i = row + row_offset
                j = col + col_offset

                if is_number(i, j):
                    adjacent_numbers_starting_indices.add(find_starting_indices_for_number_at(i, j))

        adjacent_numbers = []
        for row, col in adjacent_numbers_starting_indices:
            adjacent_numbers.append(get_number_starting_at(row, col))

        return adjacent_numbers

    # gears are '*' symbols with exactly 2 adjacent numbers
    result = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] != '*':
                continue

            adjacent_numbers = find_adjacent_numbers_unique(row, col)
            if len(adjacent_numbers) == 2:
                result += adjacent_numbers[0] * adjacent_numbers[1]

    return result

def main():
    lines = open("./input.txt", "r").readlines()

    grid = [
        [x for x in line.strip()]
        for line in lines
    ]

    print(solve_part_01(grid))
    print(solve_part_02(grid))


if __name__ == '__main__':
    main()
