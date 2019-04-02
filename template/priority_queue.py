import queue
from functools import total_ordering


@total_ordering
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x or self.x == other.x and self.y < other.y

    def __str__(self):
        return f'({self.x}, {self.y})'


q = queue.PriorityQueue()

a = [MyClass(1, 2), MyClass(1, 3), MyClass(2, 0)]

for c in a:
    q.put(c)

while not q.empty():
    print(q.get())
