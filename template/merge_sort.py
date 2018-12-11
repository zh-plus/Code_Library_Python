from tool_kit import sort_perf_cmp


def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    merged_array = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1

    merged_array.extend(left[i:])
    merged_array.extend(right[j:])

    return merged_array


if __name__ == '__main__':
    sort_perf_cmp(merge_sort)
