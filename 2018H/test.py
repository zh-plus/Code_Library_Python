f = open('B-large-practice.in', 'r')
input = lambda: f.readline().rstrip('\n')

read_ints = lambda: list(map(int, list(input())))
read_int = lambda: int(input())

print(read_int())
print(read_int())