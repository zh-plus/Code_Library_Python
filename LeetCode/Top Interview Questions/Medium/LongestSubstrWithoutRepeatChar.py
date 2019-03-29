class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == ' ':
            return 1

        if s == '':
            return 0

        result = 1
        appearance = dict()
        i, j = 0, 0
        while j < len(s):
            length = j - i
            if s[j] not in appearance:
                appearance[s[j]] = j
                length += 1

                if length > result:
                    result = length
            else:
                repeat_index = appearance[s[j]]
                for x in range(i, repeat_index + 1):
                    appearance.pop(s[x])

                appearance[s[j]] = j

                if length > result:
                    result = length
                i = repeat_index + 1
            j += 1

        return result


if __name__ == '__main__':
    s = input()
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)
