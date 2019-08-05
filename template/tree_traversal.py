from queue import LifoQueue


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def ldr(root: TreeNode):
    stack = LifoQueue()
    node = root

    while node or not stack.empty():
        # go to the most left node
        while node.left:
            stack.put(node)
            node = node.left

        print(node.val)
        node = node.right

