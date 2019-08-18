from collections import Counter

read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))


def solve(n, sticks):
    counter = Counter(sticks)
    for c in counter.values():
        if c % 2 == 1:
            return 'NO'


if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        n = read_int()
        sticks = read_ints()
        result = solve(n, sticks)
        print(result, end='' if i == T - 1 else '\n')
