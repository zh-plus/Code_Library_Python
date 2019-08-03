import math

read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split()))
read_tuple = lambda: tuple(map(int, input().split()))


# noinspection DuplicatedCode
class SegmentTree:
    def __init__(self, array):
        self.array = [None] + array
        self.tree = [None] + [None] * (2 ** math.ceil(math.log(len(array), 2) + 1))
        self.build(1, len(array), 1)

    def build(self, left, right, p):
        tree = self.tree

        if left == right:
            tree[p] = self.array[left]
            return

        middle = (left + right) >> 1
        l_child = p << 1
        r_child = (p << 1) | 1

        self.build(left, middle, l_child)
        self.build(middle + 1, right, r_child)
        tree[p] = min(tree[l_child], tree[r_child])

    def query(self, l, r, s, t, p):
        tree = self.tree

        if l <= s and t <= r:
            return tree[p]

        middle = (s + t) >> 1
        l_min, r_min = math.inf, math.inf

        if l <= middle:
            l_min = self.query(l, r, s, middle, p << 1)

        if r > middle:
            r_min = self.query(l, r, middle + 1, t, (p << 1) | 1)

        return min(l_min, r_min)


def solve1(string):
    s_tree = SegmentTree([int(x) for x in string])

    result = 0
    length = len(string)
    for i in range(1, length + 1):
        for j in range(i, length + 1):
            result += s_tree.query(i, j, 1, length, 1)

    return result


def solve2(string):
    result = 0
    length = len(string)
    for i in range(length):
        temp_min = int(string[i])
        for j in range(i, length):
            c = int(string[j])
            if c < temp_min:
                result += c
            else:
                result += temp_min


def main():
    T = read_int()
    for i in range(T):
        string = input()
        result = solve2(string)
        print(result, end='\n' if i != T - 1 else '')


if __name__ == '__main__':
    main()
