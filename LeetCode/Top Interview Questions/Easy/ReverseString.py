from typing import List

read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))


class Solution:
    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]

    def reverseString(self, nums: List[int]) -> None:
        # nums.reverse()

        # nums = nums[::-1] //This is wrong! Python parameter passing: Object reference are passed by value.

        half = len(nums) // 2
        for i in range(half):
            self.swap(nums, i, -i - 1)


if __name__ == '__main__':
    nums = read_ints()
    s = Solution()
    s.reverseString(nums)
    print(nums)
