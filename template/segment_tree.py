import math


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
        self.build(left, middle, p << 1)
        self.build(middle + 1, right, (p << 1) | 1)
        tree[p] = tree[p << 1] + tree[(p << 1) | 1]

    def query(self, l, r, s, t, p):
        if l <= s and t <= r:
            return self.tree[p]

        middle = (s + t) >> 1
        summation = 0

        if l <= middle:
            summation += self.query(l, r, s, middle, p << 1)

        if r > middle:
            summation += self.query(l, r, middle + 1, t, (p << 1) | 1)

        return summation


if __name__ == '__main__':
    array = [10, 11, 12, 13, 14]
    t = SegmentTree(array)

    print(t.tree)

    print(t.query(1, 3, 1, len(array), 1))
