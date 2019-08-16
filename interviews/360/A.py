read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))


def solve(N, M, A):
    top = sum(1 for row in A for x in row if x > 0)
    left = sum(max(row) for row in A)
    forward = sum(max(column) for column in zip(*A))

    return (top + forward + left) * 2


if __name__ == '__main__':
    N = read_int()
    M = read_int()
    A = [None] * N
    for i in range(N):
        A[i] = read_ints()
    result = solve(N, M, A)
    print(result, end='')
