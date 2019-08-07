class Solution:
    def mySqrt(self, x: int) -> int:
        return int(self._sqrt(x))

    def _sqrt(self, x):
        xn = 6
        for _ in range(1000000):
            xn = xn - ((xn ** 2 - x) / (2 * xn))

        return xn


if __name__ == '__main__':
    s = Solution()
    r = s._sqrt(1000)
    print(r)

    print(r ** 2)
