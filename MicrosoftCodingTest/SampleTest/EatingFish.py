def solve(input1, input2, input3, input4):
    N, M, Q = input1, input2, input3
    queries = input4

    eat_by_A = [[] for x in range(N + 1)]
    B_eat_by = [-1 for x in range(M + 1)]
    for query in queries:
        E_type, predator, prey = query
        if E_type == 1:
            B_eat_by[prey] = predator
            eat_by_A[predator].append(prey)
        elif len(eat_by_A[predator]) > len(eat_by_A[prey]):
            for B in eat_by_A[prey]:
                B_eat_by[B] = predator
                eat_by_A[predator].append(B)

    return B_eat_by


if __name__ == '__main__':
    data = [2, 3, 4, [[1, 1, 1], [1, 1, 2], [1, 2, 3], [2, 1, 2]]]
    print(solve(*data))