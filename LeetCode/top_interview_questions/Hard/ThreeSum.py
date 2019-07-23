from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: l += 1
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    l += 1
                    r -= 1

        return result


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i, num in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            sum = -num
            while left < right:
                if nums[left] + nums[right] == sum:
                    result.add((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < sum:
                    left += 1
                else:
                    right -= 1

        return list(result)


if __name__ == '__main__':
    a = [-1, -1, 0, 1, 1]
    s = Solution2()
    print(s.threeSum(a))
