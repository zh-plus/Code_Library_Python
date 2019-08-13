from collections import deque

from template.tool_kit import sort_perf_cmp


def swap(array, p, q):
    array[p], array[q] = array[q], array[p]


def partition(array, first, last):
    p = first
    pivot = array[last - 1]
    for q in range(first, last - 1):
        if array[q] <= pivot:
            swap(array, p, q)
            p += 1

    swap(array, p, last - 1)
    return p


def quick_sort(array):
    _quick_sort(array, 0, len(array))


def _quick_sort(array, first, last):
    if first < last:
        p = partition(array, first, last)
        _quick_sort(array, first, p)
        _quick_sort(array, p + 1, last)


def quick_sort_loop(array):
    queue = deque()
    queue.append((0, len(array)))
    while len(queue):
        first, last = queue.popleft()
        if first < last:
            p = partition(array, first, last)
            queue.append((first, p))
            queue.append((p + 1, last))


if __name__ == '__main__':
    sort_perf_cmp(quick_sort_loop)
