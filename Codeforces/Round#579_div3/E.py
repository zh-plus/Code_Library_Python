from collections import Counter

read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))


def solve(n, t):
    counter = Counter(t)
    s = set()
    for i, c in counter.items():
        if c >= 3:
            s.update([i - 1, i, i + 1])
        elif c == 2:
            s.update([i, i + 1 if i + 1 not in s else i - 1])
        else:
            s.add(i)

    if 0 in s:
        s.remove(0)

    return len(s)


if __name__ == '__main__':
    n = read_int()
    t = read_ints()
    result = solve(n, t)
    print(result, end='')
