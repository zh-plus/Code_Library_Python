class Solution:
    def isValid(self, s: str) -> bool:
        right = {')', '}', ']'}
        lr_map = {'(': ')', '{': '}', '[': ']'}

        s2 = []
        for c in reversed(s):
            if c in right:
                s2.append(c)
            elif not s2 or lr_map[c] != s2.pop():
                return False

        return False if s2 else True


if __name__ == '__main__':
    s = '[[{{{}}}]{}{}]'
    solution = Solution()

    print(solution.isValid(s))
