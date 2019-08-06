from queue import Queue


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @staticmethod
    def from_array(array):
        # bfs construct binary tree
        root = TreeNode(array[0])
        q = Queue()
        q.put(root)

        i = 1
        while not q.empty() and i != len(array):
            node = q.get()
            node.left = TreeNode(array[i])
            q.put(node.left)

            if i + 1 != len(array):
                node.right = TreeNode(array[i + 1])
                q.put(node.right)

            i += 2

        return root


def ldr(root: TreeNode):
    stack = []
    node = root

    result = []
    while node or stack:
        # go to the most left node
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        result.append(node.val)
        node = node.right

    return ' '.join(list(map(str, result)))


def dlr(root: TreeNode):
    stack = []
    node = root

    result = []
    while node or stack:
        while node:
            result.append(node.val)
            stack.append(node)
            node = node.left

        node = stack.pop()
        node = node.right

    return ' '.join(list(map(str, result)))


def lrd(root: TreeNode):
    """
    After getting DRL(reverse RL for DLR), reverse output to LRD.
    """
    stack = []
    node = root

    result = []
    while node or stack:
        while node:
            result.append(node.val)
            stack.append(node)
            node = node.right

        node = stack.pop()
        node = node.left

    return ' '.join(list(map(str, reversed(result))))


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(ldr(root))
