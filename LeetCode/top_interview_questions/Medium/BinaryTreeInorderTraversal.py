from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        node = root
        stack = []

        result = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result.append(node.val)
            node = node.right

        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    s = Solution()
    print(s.inorderTraversal(root))
