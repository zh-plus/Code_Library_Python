from queue import LifoQueue, Queue


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
    stack = LifoQueue()
    node = root

    while node or not stack.empty():
        # go to the most left node
        while node:
            stack.put(node)
            node = node.left

        node = stack.get()
        print(node.val, end=' ')
        node = node.right


if __name__ == '__main__':
    a = [3, 1, 5, 0, None, 4, 8]
    root = TreeNode.from_array(a)
    ldr(root)
