from typing import List


class Solution:
    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)

        # flip according to diagnose
        for i in range(length - 1):
            for j in range(length - 1 - i):
                matrix[i][j], matrix[length - 1 - j][length - 1 - i] = matrix[length - 1 - j][length - 1 - i], matrix[i][j]

        # flip horizontal middle line
        matrix.reverse()

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)

        # flip horizontal middle line
        matrix.reverse()

        # flip according to symmetry
        for i in range(1, length):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    s = Solution()
    s.rotate2(matrix)

    for m in matrix:
        print(m)
