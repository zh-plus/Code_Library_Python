from typing import List

read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p, q = 0, 0
        while q < len(nums):
            while q + 1 < len(nums) and nums[q] == nums[q + 1]:
                q += 1

            nums[p] = nums[q]
            p += 1
            q += 1

        return p


if __name__ == '__main__':
    nums = read_ints()
    s = Solution()
    result = s.removeDuplicates(nums)
    print(nums)
    print(result)
