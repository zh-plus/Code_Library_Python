import functools
import numpy as np

from time import perf_counter


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


def sort_perf_cmp(sort_alg):
    print('my impl:', end='\t')
    with Timer():
        for _ in range(100000):
            a = list(np.random.randint(0, 20, 10))
            sort_alg(a)

    print('py impl:', end='\t')
    with Timer():
        for _ in range(100000):
            a = list(np.random.randint(0, 20, 10))
            a.sort()