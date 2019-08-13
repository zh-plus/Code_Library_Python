read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))


def solve(x: str, y: str):
    x_reverse = x[::-1]
    y_reverse = y[::-1]

    y_1 = y_reverse.find('1')
    x_1 = y_1 + x_reverse[y_1:].find('1')

    k = x_1 - y_1

    return k


if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        x = input()
        y = input()
        result = solve(x, y)
        print(result, end='' if i == T - 1 else '\n')
