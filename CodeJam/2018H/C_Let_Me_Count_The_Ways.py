from functools import reduce
from math import factorial

file = open('input/C-large-practice.in', 'r')
input = lambda: file.readline().rstrip('\n')

read_ints = lambda: list(map(int, input().split(' ')))
read_int = lambda: int(input())

MOD = 1000000007


def combination(r, k):
    return int(reduce(lambda x, y: x * y, list(range(r - k + 1, r + 1))) / factorial(k))


def solve(N, M):
    all_ways = factorial(2 * N) % MOD

    # all ways - (ways that have at least one nearby newlywed couples)
    # applying inclusion-exclusion
    nearby_ways = 0
    for x in range(1, M + 1):
        ways = combination(M, x) % MOD
        ways = (ways * 2 ** x) % MOD
        ways = (ways * factorial(2 * N - x)) % MOD

        if x % 2:
            nearby_ways = (nearby_ways + ways) % MOD
        else:
            nearby_ways = (nearby_ways + MOD - ways) % MOD

    return int(all_ways - nearby_ways) % MOD


if __name__ == '__main__':
    T = read_int()
    with open('output.txt', 'w') as output_file:
        for i in range(1, T + 1):
            N, M = read_ints()
            answer = solve(N, M)

            result = f'Case #{i}: {answer}'
            print(result)
            output_file.write(result + '\n')
