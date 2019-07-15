read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split()))


def solve(A, b):
    for a in A:
        if not (a + b) % 7:
            return 'Yes'

    return 'No'


if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        n, b = read_ints()
        A = read_ints()
        result = solve(A, b)
        print(result, end='\n' if i != T - 1 else '')
