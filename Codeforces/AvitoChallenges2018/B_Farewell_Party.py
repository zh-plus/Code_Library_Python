read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))


def solve(n, diffs):
    array = []
    for _ in range(n + 1):
        array.append(set())

    for i, d in enumerate(diffs):
        array[n - d].add(i)

    is_possible = True
    for i, s in enumerate(array[1:]):
        if len(s) % (i + 1) != 0:
            is_possible = False

    if is_possible:
        print('Possible')

        hats = [0] * n
        hat_kind = 1
        for i, s in enumerate(array):
            for j, person in enumerate(s):
                hats[person] = hat_kind

                if (j + 1) % i == 0:
                    hat_kind += 1

        print(' '.join(map(str, hats)))

    else:
        print('Impossible')


if __name__ == '__main__':
    n = read_int()
    diffs = read_ints()
    solve(n, diffs)
