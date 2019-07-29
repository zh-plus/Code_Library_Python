from template.tool_kit import sort_perf_cmp

from functools import reduce


def radix_sort(array):
    array = list(map(str, array))
    max_length = len(max(array, key=lambda s: len(s)))
    array = list(map(lambda s: s.zfill(max_length), array))

    boxes = [[] for x in range(10)]

    for i in reversed(range(max_length)):
        # put them into boxes according to the i-th number
        for s in array:
            boxes[int(s[i])].append(s)

        # recombination
        array = []
        for box in boxes:
            array.extend(box)
            box.clear()

    return list(map(int, array))


if __name__ == '__main__':
    a = [0, 10, 35, 2, 4, 1]

    b = radix_sort(a)
    print(b)

    sort_perf_cmp(radix_sort)
