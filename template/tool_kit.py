import functools
from time import perf_counter

import numpy as np

from template.bucket_sort import bucket_sort
from template.merge_sort import merge_sort
from template.quick_sort import quick_sort
from template.radix_sort import radix_sort


class Timer:
    def __enter__(self):
        self.start = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{(perf_counter() - self.start):0<6.4} s elapsed!')


def timer_deco(func):
    @functools.wraps(func)
    def wrapper_timer_deco(*args, **kwargs):
        tic = perf_counter()
        value = func(*args, **kwargs)
        toc = perf_counter()
        print(f'{(toc - tic):0<6.4} s elapsed!')

        return value

    return wrapper_timer_deco


def sort_perf_cmp_all():
    algs = [quick_sort, bucket_sort, merge_sort, radix_sort]

    for alg in algs:
        print(f'{alg.__name__}:', end='\t')
        with Timer():
            for _ in range(100):
                a = list(np.random.randint(0, 1000000, 10000))
                alg(a)

    print('py impl:', end='\t')
    with Timer():
        for _ in range(100):
            a = list(np.random.randint(0, 1000000, 10000))
            a.sort()


def sort_perf_cmp(sort_alg):
    print('my impl:', end='\t')
    with Timer():
        for _ in range(100):
            a = list(np.random.randint(0, 1000000, 10000))
            sort_alg(a)

    print('py impl:', end='\t')
    with Timer():
        for _ in range(100):
            a = list(np.random.randint(0, 1000000, 10000))
            a.sort()


if __name__ == '__main__':
    sort_perf_cmp_all()
