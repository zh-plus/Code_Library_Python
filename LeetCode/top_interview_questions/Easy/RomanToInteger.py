from typing import List

read_strs = lambda: input().split()


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = len(min(strs, key=lambda s: len(s)))
        self.temp = [None for _ in range(shortest + 1)]

        if not self.is_all_equal(strs, shortest):
            shortest = self.binary_search(strs, shortest)

        return strs[0][:shortest]

    def binary_search(self, strs, stop):
        if self.is_all_equal(strs, stop // 2):
            return self.binary_search(strs, stop + stop // 2)
        else:
            return self.binary_search(strs, stop // 2)

    def is_all_equal(self, strs, stop):
        result = True
        first = strs[0][:stop]
        for s in strs[1:]:
            if s[:stop] != first:
                return False

        return result


if __name__ == '__main__':
    strs = read_strs()
    s = Solution()
    result = s.longestCommonPrefix(strs)
    print(result)
