from typing import List


class Solution:
    def __init__(self):
        self.result = None

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self._subsets2(sorted(nums))

        return self.result

    def _subsets1(self, nums):
        """
        Recursive (DFS)
        """
        self.result = [[]]

        for i, num in enumerate(nums):
            self._dfs(nums[i + 1:], [num])

    def _dfs(self, nums, path):
        self.result.append(path)

        for i, num in enumerate(nums):
            self._dfs(nums[i + 1:], path + [num])

    def _subsets2(self, nums):
        """
        Iterative
        """
        self.result = [[]]

        for num in nums:
            temp = [r + [num] for r in self.result]
            self.result.extend(temp)

    def _subsets3(self, nums):
        """
        Bit Manipulation
        """
        self.result = []

        for bits in range(1 << len(nums)):
            temp = [num for i, num in filter(lambda x: (1 << x[0]) & bits, enumerate(nums))]
            self.result.append(temp)


if __name__ == '__main__':
    s = Solution()

    print(s.subsets([1, 2, 3]))
