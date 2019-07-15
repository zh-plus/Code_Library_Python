read_int = lambda: int(input())


def solve(N, P):
    P = P.replace('S', 'T')
    P = P.replace('E', 'S')
    P = P.replace('T', 'E')

    return P


T = read_int()
for i in range(1, T + 1):
    N, P = read_int(), input()
    answer = solve(N, P)
    print('Case #{}: {}'.format(i, answer))
