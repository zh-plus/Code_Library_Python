from template.tool_kit import Timer

# f = open('in.txt', 'r')
# input = lambda: f.readline()

read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))


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


def solve(s1, s2):
    min_len = min(len(s1), len(s2))
    if s1[:min_len] == s2[:min_len]:
        return min_len

    trie = Trie()
    trie.add(s1)
    trie.add(s2)

    return trie.find_longest_common()

    # length = 0
    # for x, y in zip(s1, s2):
    #     if x == y:
    #         length += 1
    #     else:
    #         break
    #
    # return length


if __name__ == '__main__':
    T = read_int()
    strings = [None] * T
    for i in range(T):
        strings[i] = input()

    strings_len = len(strings)
    with Timer():
        q1, q2 = read_ints()
        q1 -= 1
        q2 -= 1
        if not 0 <= q1 < strings_len or not 0 <= q2 < strings_len:
            exit()

        result = solve(strings[q1], strings[q2])
        print(result)
