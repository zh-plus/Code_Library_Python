class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.LDR_result = None

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        self.LDR_result = []
        self.do_LDR(root)

        return self.is_sorted(self.LDR_result)

    def do_LDR(self, node: TreeNode):
        self.do_LDR(node.left) if node.left else None
        self.LDR_result.append(node.val)
        self.do_LDR(node.right) if node.right else None

    def is_sorted(self, array):
        return all(array[i] <= array[i + 1] for i in range(len(array) - 1))
