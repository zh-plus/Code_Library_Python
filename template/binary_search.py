from bisect import bisect
import numpy as np
from timer import Timer


def lower_bound(array, first, last, value):
    while first < last:
        mid = first + (last - first) // 2
        if array[mid] < value:
            first = mid + 1
        else:
            last = mid
    return first


if __name__ == '__main__':
    a = sorted(list(np.random.randint(0, 10000000, 100000)))

    print('my impl:', end='\t')
    with Timer():
        for _ in range(100000):
            b = np.random.randint(0, 10000000)
            c = lower_bound(a, 0, 100000, b)

    print('py impl:', end='\t')
    with Timer():
        for _ in range(100000):
            b = np.random.randint(0, 10000000)
            c = bisect(a, b)
