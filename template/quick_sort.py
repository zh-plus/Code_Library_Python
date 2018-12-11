from tool_kit import sort_perf_cmp


def swap(array, p, q):
    array[p], array[q] = array[q], array[p]


def quick_sort(array):
    _quick_sort(array, 0, len(array))


def _quick_sort(array, first, last):
    if first < last:
        p = partition(array, first, last)
        _quick_sort(array, first, p)
        _quick_sort(array, p + 1, last)


def partition(array, first, last):
    p = first
    pivot = array[last - 1]
    for q in range(first, last - 1):
        if array[q] <= pivot:
            swap(array, p, q)
            p += 1

    swap(array, p, last - 1)
    return p


if __name__ == '__main__':
    sort_perf_cmp(quick_sort)
