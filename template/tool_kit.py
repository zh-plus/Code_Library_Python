from time import perf_counter
import numpy as np


class Timer:
    def __enter__(self):
        self.start = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('{:0<6.4} s elapsed!'.format(perf_counter() - self.start))


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
