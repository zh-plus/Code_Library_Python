from itertools import chain


def bucket_sort(array, bucket_num=1000):
    min_num, max_num = min(array), max(array)
    buckets = [[] for _ in range(bucket_num + 1)]
    bucket_size = (max_num - min_num) / bucket_num

    for a in array:
        index = int((a - min_num) / bucket_size)
        buckets[index].append(a)

    buckets = [sorted(b) for b in buckets]

    return list(chain.from_iterable(buckets))


if __name__ == '__main__':
    from template.tool_kit import sort_perf_cmp

    sort_perf_cmp(bucket_sort)
