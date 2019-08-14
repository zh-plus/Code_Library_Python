class Solution:
    def isValid(self, s: str) -> bool:
        left = {'(', '{', '['}
        right = {')', '}', ']'}
        lr_map = {'(': ')', '{': '}', '[': ']'}

        s1 = list(s)
        s2 = []
        while s1:
            while s1 and s1[-1] in right:
                s2.append(s1.pop())

            if not s2:
                return False

            while s1 and s2 and s1[-1] in left:
                l, r = s1.pop(), s2.pop()
                if lr_map[l] != r:
                    return False

        return True


if __name__ == '__main__':
    s = '['
    solution = Solution()

    print(solution.isValid(s))