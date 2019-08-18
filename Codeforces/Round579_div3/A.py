read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))


def solve(n, nums):
    if len(nums) <= 3:
        return 'YES'

    cnext = lambda i: (i + 1) % n
    change = 0
    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i - 1]) != 1:
            change = i + 1
            break
    else:
        return 'YES'

    for _ in range(len(nums) - 1):
        if abs(nums[change] - nums[change - 1]) != 1:
            return 'NO'

        change = cnext(change)

    return 'YES'


if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        n = read_int()
        nums = read_ints()
        result = solve(n, nums)
        print(result, end='' if i == T - 1 else '\n')
