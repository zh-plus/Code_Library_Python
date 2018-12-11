from time import perf_counter


class Timer:
    def __enter__(self):
        self.start = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('{:0<6.4} s elapsed!'.format(perf_counter() - self.start))
