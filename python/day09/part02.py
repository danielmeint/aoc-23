def calc_next_val(history):
    # if all 0, return 0
    if all([x == 0 for x in history]):
        return 0

    # compute child history and extrapolate
    child_history = compute_child_history(history)

    assert len(history) == len(child_history)
    return history[-1] + child_history[-1]


def compute_child_history(history):
    child_history = [0 for _ in range(len(history) - 1)]
    # child_history[i] = history[i+1] - history[i]
    for i in range(len(history) - 1):
        child_history[i] = history[i + 1] - history[i]

    # if all 0, append another 0 and return
    if all([x == 0 for x in child_history]):
        child_history.append(0)
        print(f'child_history: {child_history}')
        return child_history

    # extrapolate the last value by recursively computing the child history
    child_history.append(calc_next_val(child_history))
    print(f'child_history: {child_history}')
    return child_history


def main():
    # readiness from input.txt
    histories = open("./input.txt", "r").readlines()
    histories = [
        [int(x) for x in history.strip().split(' ')]
        for history in histories
    ]

    # reverse
    histories = [history[::-1] for history in histories]

    print(histories[0])

    print(len(histories))

    next_vals = []

    for history in histories:
        next_vals.append(calc_next_val(history))

    print(sum(next_vals))


if __name__ == '__main__':
    main()
