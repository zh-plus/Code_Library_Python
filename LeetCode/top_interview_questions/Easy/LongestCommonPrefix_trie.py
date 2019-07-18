from typing import List

read_strs = lambda: input().split()


class TrieNode:
    def __init__(self, char: str):
        self.char = char  # '' for root node
        self.children_chars = []
        self.children = []
        self.word_finished = False
        self.counter = 1  # How many times this character appeared in the addition process

    def add_child(self, new_node):
        self.children.append(new_node)
        self.children_chars.append(new_node.char)


class Trie:
    def __init__(self):
        self.root = TrieNode('')
        self.total_num = 0

    def add(self, word: str):
        node = self.root
        continuous = True
        for char in word:
            children_chars = node.children_chars
            if continuous and char in children_chars:
                node = node.children[children_chars.index(char)]
                node.counter += 1
            else:
                new_node = TrieNode(char)
                node.add_child(new_node)
                node = new_node
                continuous = False

        self.total_num += 1
        node.word_finished = True

    def find_longest_common(self):
        length = 0
        node = self.root
        while len(node.children) == 1 and node.children[0].counter == self.total_num:
            node = node.children[0]
            length += 1

        return length


class Solution:
    def __init__(self):
        self.trie = Trie()

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        if len(strs) == 1:
            return strs[0]

        trie = self.trie
        for word in strs:
            trie.add(word)

        return strs[0][:trie.find_longest_common()]


if __name__ == '__main__':
    strs = read_strs()
    s = Solution()
    result = s.longestCommonPrefix(strs)
    print(result)
