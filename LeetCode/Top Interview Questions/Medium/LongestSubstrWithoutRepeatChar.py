class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 1
        appearance = dict()
        i, j = 0, 0
        while j < len(s):
            if s[j] not in appearance:
                appearance[s[j]] = j
            else:
                length = j - i
                for x in range(i, appearance[s[j]] + 1):
                    appearance.pop(s[x])

                if length > result:
                    result = length
                i = appearance[s[j]]
            j += 1

        return result


if __name__ == '__main__':
    s = input()
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)
