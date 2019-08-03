read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split()))


def solve(n, s):
    return ''.join([x[0].capitalize() for x in s.split()])


if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        n = read_int()
        s = input()
        result = solve(n, s)
        print(result, end='\n' if i != T - 1 else '')
