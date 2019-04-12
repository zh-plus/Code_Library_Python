class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = 2 * numRows - 2
        result = []
        result.append(''.join([x for i, x in enumerate(s) if i % l == 0]))
        for r in range(1, numRows - 1):
            first_match = l - r
            second_match = l / 2 - r
            line = [x for i, x in enumerate(s) if (i + first_match) % l == 0 or (i + second_match) % l == 0]
            result.append(''.join(line))
        result.append(''.join([x for i, x in enumerate(s) if (i + l / 2) % l == 0]))

        return '\n'.join(result)


if __name__ == '__main__':
    string = input()
    numRows = int(input())
    s = Solution()
    answer = s.convert(string, numRows)

    print(answer)