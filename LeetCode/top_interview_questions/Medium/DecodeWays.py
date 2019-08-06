class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        # f(0)
        temp = 1 if s else 0

        # f(i) = f(i - 1) + ...
        for i in range(1, len(s)):
            if s[i - 1] in '12':
                if s[i] == '0' and i != 1 and s[i - 2] in '12':
                    temp -= 1
                elif (s[i - 1] == '1' and s[i] != '0') or (s[i - 1] == '2' and s[i] not in '7890'):
                    temp += 1
            elif s[i] == '0':
                return 0

        return temp


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('120'))
