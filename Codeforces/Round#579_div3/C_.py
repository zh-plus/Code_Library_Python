read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))


def solve(n, rating, projects):
    positive = {p for p in projects if p[1] > 0}
    while len(positive):
        remove = [False] * len(projects)
        for i, p in enumerate(projects):
            if rating >= p[0] and p[1] > 0:
                remove.append(i)
                rating += p[1]
        projects = [projects[i] for i in range(len(projects)) if not remove[i]]

        if rating < min(positive, key=lambda x: x[0]):
            return 'NO'

    while len(projects):
        remove = [False] * len(projects)
        for i, p in enumerate(projects):
            if rating < p[0]:
                return 'NO'
            remove.append(i)
            rating += p[2]
        projects = [projects[i] for i in range(len(projects)) if not remove[i]]

    return 'YES'


if __name__ == '__main__':
    l = read_ints()
    n, r = l[0], l[1]
    p = []
    for _ in range(n):
        p.append(read_ints)

    result = solve(n, r, p)
    print(result, end='')
