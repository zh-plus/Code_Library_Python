read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))


def solve(N, M, A):
    top = N * M
    forward, left = 0, 0
    for row in A:
        left += max(row)

    for column in zip(*A):
        forward += max(column)

    return (top + forward + left) * 2


if __name__ == '__main__':
    N = read_int()
    M = read_int()
    A = [None] * N
    for i in range(N):
        A[i] = read_ints()
    result = solve(N, M, A)
    print(result, end='')
