read_int = lambda: int(input())


def solve(num):
    if '4' not in str(num):
        return num, 0

    a, b = '', ''
    for x in str(num):
        if x == '4':
            a += '{}'.format(int(x) - 1)
            b += '1'
        else:
            a += x
            b += '0'

    return int(a), int(b)


T = read_int()
for i in range(1, T + 1):
    a, b = solve(read_int())
    print('Case #{}: {} {}'.format(i, a, b))
