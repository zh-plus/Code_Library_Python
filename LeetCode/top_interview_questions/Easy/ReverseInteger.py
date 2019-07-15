from typing import List
import sys

read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))

MAX_RESULT = (1 << 31) - 1


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x_str = str(abs(x))
        reversed_x_str = x_str[::-1]
        result = int(reversed_x_str) * sign

        return result if -MAX_RESULT - 1 <= result <= MAX_RESULT else 0


if __name__ == '__main__':
    num = read_int()
    s = Solution()
    result = s.reverse(num)
    print(result)
