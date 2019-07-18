from typing import List

read_strs = lambda: input().split()


class Solution:
    def __init__(self):
        self.temp = None

    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = len(min(strs, key=lambda s: len(s), default=''))
        self.temp = [None for _ in range(shortest + 1)]

        if not self.is_all_equal(strs, shortest):
            shortest = self.binary_search(strs, shortest)

        return strs[0][:shortest] if strs else ''

    def binary_search(self, strs, stop):
        half = stop // 2
        if self.is_all_equal(strs, half):
            if self.temp[half + 1] == False:
                return half

            return self.binary_search(strs, stop + half)
        else:
            if self.temp[half - 1] == True:
                return half - 1
            return self.binary_search(strs, half)

    def is_all_equal(self, strs, stop):
        if stop == 0:
            return True

        str_set = set([s[:stop] for s in strs])
        result = True if len(str_set) == 1 else False

        self.temp[stop] = result
        return result


if __name__ == '__main__':
    strs = read_strs()
    s = Solution()
    result = s.longestCommonPrefix(strs)
    print(result)
