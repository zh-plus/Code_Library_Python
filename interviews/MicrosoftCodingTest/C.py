class UserMainCode(object):
    def solve(cls, input1, input2, input3):
        N, Q = input1, input2

        if Q == 0 or N == 0:
            return 0

        # q_types, q_target = zip(*queries)
        # if max(q_types) <= 2:
        #     return 0

        result = 0
        q = list(range(1, N + 1))
        for E, X in input3:
            if len(q) == 0:
                break

            if E == 1:
                q.pop(0)
            elif E == 2:
                q.remove(X)
            else:
                result = result + (q.index(X) + 1)

        return result


if __name__ == '__main__':
    data1 = [5, 3, [[1, 0], [3, 3], [2, 2]]]
    data2 = [5, 1, [[1, 0]]]
    data3 = [1, 2, [[2, 1], [3, 1]]]
    u = UserMainCode()

    print(u.solve(*data3))
