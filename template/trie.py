class TrieNode:
    def __init__(self, char: str):
        self.char = char  # '' for root node
        self.children = dict()
        self.word_finished = False
        self.counter = 1  # How many times this character appeared in the addition process

    def add_child(self, char):
        self.children[char] = TrieNode(char)


class Trie:
    def __init__(self):
        self.root = TrieNode('')
        self.total_num = 0

    def add(self, word: str):
        node = self.root
        continuous = True
        for char in word:
            children = node.children
            if continuous and char in children:
                node = node.children[char]
                node.counter += 1
            else:
                node.add_child(char)
                node = children[char]
                continuous = False

        self.total_num += 1
        node.word_finished = True

    def find_longest_common(self):
        length = 0
        node = self.root
        while len(node.children) == 1 and next(iter(node.children.values())).counter == self.total_num:
            node = next(iter(node.children.values()))
            length += 1

        return length
