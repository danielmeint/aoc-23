def parse_input(lines):
    # seeds is first line after colon
    colon_index = lines[0].find(':')
    seeds = [int(x) for x in lines[0][colon_index + 1:].strip().split(' ') if x != '']
    print(seeds)

    stages_mappings = []

    # process each stage, stages are separated by empty lines
    current_stage = []
    for i in range(2, len(lines)):
        line = lines[i].strip()
        if line == '':
            stages_mappings.append(current_stage)
            current_stage = []
        # if line does not start with number
        elif not line[0].isdigit():
            # ignore
            continue
        else:
            # split by spaces (and ignore empty strings)
            current_stage.append([int(x) for x in line.split(' ') if x != ''])

    # add last stage
    stages_mappings.append(current_stage)

    # sort individual stages by first number
    for stage in stages_mappings:
        stage.sort(key=lambda x: x[1])

    return seeds, stages_mappings


def map_number(number, stage_mappings):
    # find the correct mapping via binary search, i.e., find the mapping with the highest first number that is still smaller than the number
    print(f'number: {number}, stage_mappings: {stage_mappings}')

    dest_range_start, src_range_start, range_length = find_correct_mapping(number, stage_mappings)

    print(
        f'number {number} is in range {src_range_start} to {src_range_start + range_length - 1} and will be mapped to {dest_range_start} to {dest_range_start + range_length - 1}')

    # assert that the number is in the range
    assert src_range_start <= number < src_range_start + range_length

    # map the number according to the mapping; the mapping is a linear function
    res = dest_range_start + (number - src_range_start)
    print(f'res: {res}')
    return res


def find_correct_mapping(number, stage_mappings):
    print(f'finding correct mapping for number {number} in stage_mappings {stage_mappings}')
    # use linear search for now
    src_range_starts = [x[1] for x in stage_mappings]

    # assert that src_range_starts is sorted
    assert src_range_starts == sorted(src_range_starts)

    print(f'src_range_starts: {src_range_starts}')

    for i in range(len(src_range_starts)):
        # if last one or if number is in between this and next, return this
        if i == len(src_range_starts) - 1 or src_range_starts[i] <= number < src_range_starts[i + 1]:
            return stage_mappings[i]

    raise Exception('should not happen')





def solve_part_01(seeds, stages_mappings):
    locations = [0 for _ in range(len(seeds))]

    print(f'seeds: {seeds}, stages_mappings: {stages_mappings}')

    for i in range(len(seeds)):
        # go through each stage
        current = seeds[i]
        for stage in stages_mappings:
            # map current
            current = map_number(current, stage)

        locations[i] = current

    return locations


def main():
    lines = open("./input.txt", "r").readlines()
    seeds, stages_mappings = parse_input(lines)

    print(solve_part_01(seeds, stages_mappings))


if __name__ == '__main__':
    main()
