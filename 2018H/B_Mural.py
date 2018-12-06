import math
import numpy as np

input_file = open('input/B-large-practice.in', 'r')
input = lambda: input_file.readline().rstrip('\n')

read_ints = lambda: list(map(int, list(input())))
read_int = lambda: int(input())


def solve(N, scores):
    working_days = math.ceil(N / 2)
    s = np.sum(scores[: working_days])
    best = s
    # print(N - working_days + 1)
    for i in range(N - working_days):
        s += (scores[i + working_days] - scores[i])
        if s > best:
            best = s

    return best


if __name__ == '__main__':
    T = read_int()
    with open('output.txt', 'w') as output_file:
        for i in range(1, T + 1):
            N = read_int()
            scores = read_ints()
            result = solve(N, scores)
            output_file.write('Case #{}: {}\n'.format(i, result))
            print('Case #{}: {}'.format(i, result))
