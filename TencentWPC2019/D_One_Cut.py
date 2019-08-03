from collections import defaultdict

read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split()))


def solve(n, q1, q2):
    if set(q1) != set(q2):
        return 'No'

    m1, m2 = defaultdict(int), defaultdict(int)
    for x, y in zip(q1, q2):
        m1[x] += 1
        m2[y] += 1

    if m1 != m2:
        return 'No'

    return 'Yes'


if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        n = read_int()
        q1 = read_ints()
        q2 = read_ints()
        result = solve(n, q1, q2)
        print(result, end='\n' if i != T - 1 else '')
