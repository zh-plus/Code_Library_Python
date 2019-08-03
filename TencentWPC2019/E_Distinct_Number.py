from collections import defaultdict

read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split()))
read_tuple = lambda: tuple(map(int, input().split()))


def solve(L, x):
    pass


if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        n, x = read_int(), read_int()
        L = []
        for _ in range(n):
            L.append(read_tuple())

        result = solve(L, x)
        print(result, end='\n' if i != T - 1 else '')
