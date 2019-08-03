import math

read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split()))
read_tuple = lambda: tuple(map(int, input().split()))


def solve():
    pass


def main():
    T = read_int()
    for i in range(T):
        result = solve()
        print(result, end='\n' if i != T - 1 else '')


if __name__ == '__main__':
    main()
