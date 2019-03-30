from typing import List

read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash set solution
        num_set = set(nums)
        for x in num_set:
            if target - x in num_set:
                first = nums.index(x)
                second = nums.index(target - x)
                if first == second:
                    second = nums.index(x, first + 1)
                return [first, second]


if __name__ == '__main__':
    nums = read_ints()
    target = read_int()
    s = Solution()
    result = s.twoSum(nums, target)
    print(result)
