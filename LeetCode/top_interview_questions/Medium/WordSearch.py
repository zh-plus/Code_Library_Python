from itertools import product
from typing import List


class Solution:
    def __init__(self):
        self.visited = None
        self.height = None
        self.width = None
        self.pattern = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not str:
            return True

        self.height = len(board)
        self.width = len(board[0])

        self.visited = [[False] * self.width for _ in range(self.height)]

        for i, j in product(range(self.height), range(self.width)):
            self.visited[i][j] = True

            if board[i][j] == word[0] and self.dfs(board, word[1:], i, j):
                return True

            self.visited[i][j] = False

        return False

    def dfs(self, board, word, i, j):

        def get_around():
            return ((max(0, min(self.height - 1, i + x)), max(0, min(self.width - 1, j + y))) for x, y in self.pattern)

        if not word:
            return True

        g = get_around()

        around = ((x, y) for x, y in g if not self.visited[x][y] and board[x][y] == word[0])
        for x, y in around:
            self.visited[x][y] = True

            if self.dfs(board, word[1:], x, y):
                return True

            self.visited[x][y] = False

        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    s = Solution()
    print(s.exist(board, 'ABCCED'))
    print(s.exist(board, 'SEE'))
    print(s.exist(board, 'ABCB'))
