read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))


def solve(s: str, t: str):
    f1, f2 = s.find(t), s.rfind(t)

    r1 = max(len(s) - f1 - len(t) + 1, f1)
    r2 = max(f2, len(s) - f2 - len(t) + 1)

    return max(r1, r2)


if __name__ == '__main__':
    s = input()
    t = input()
    result = solve(s, t)
    print(result, end='')
