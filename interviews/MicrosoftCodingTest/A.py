class UserMainCode(object):
    def solve(cls, input1, input2, input3):
        N, P, X = input1, input2, input3

    def find_all_factors(self, number):
        result = []
        for i in range(1, number):
            if number % i == 0:
                result.append(i)

        return result


if __name__ == '__main__':
    # data = [2, 3, 4, [[1, 1, 1], [1, 1, 2], [1, 2, 3], [2, 1, 2]]]
    u = UserMainCode()
    # # print(solve(*data))

    n = 10
    print(u.find_all_factor(n))
