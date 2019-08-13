from typing import List


class Solution:
    def __init__(self):
        self.result = None

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self._permute2(nums)

        return self.result

    def _permute1(self, nums):
        self.result = self.dfs(nums)

    def dfs(self, nums):
        if len(nums) in (0, 1):
            return [nums]
        elif len(nums) == 2:
            return [nums, nums[::-1]]

        temp = []
        for i, n in enumerate(nums):
            for m in self.permute(nums[:i] + nums[i + 1:]):
                temp.append([n] + m)

        return temp

    def _permute2(self, nums, path=None):
        """Back tracking"""
        if path is None:
            path = []

        if not nums:
            self.result.append(path)

        for i, num in enumerate(nums):
            self._permute2(nums[:i] + nums[i + 1:], path + [num])


if __name__ == '__main__':
    s = Solution()

    print(s.permute([1, 2, 3]))
