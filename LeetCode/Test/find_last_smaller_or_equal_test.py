def findFirstLargeOrEqual(nums, left, right, N):
    if right - left < 2:
        if nums[right - 1] < N:
            return right
        elif nums[left] < N:
            return left + 1
        else:
            raise Exception('Wrong!')

    half = (left + right) // 2
    if nums[half] < N:
        return findFirstLargeOrEqual(nums, half, right, N)
    else:
        return findFirstLargeOrEqual(nums, left, half, N)


def findFirstLargeOrEqual_brute(nums, N):
    index = 0
    for i, x in enumerate(nums):
        if x < N:
            index = i
        else:
            break
    return index + 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 6, 7, 7, 10, 12, 17]
    nums2 = [2, 3, 4, 7, 8, 10, 13, 14, 15]
    # for _ in range(100000):
    #     a1 = np.sort(np.random.randint(0, 10000, 1000))
    #     a2 = np.sort(np.random.randint(0, 10000, 1000))
    #     N = np.random.randint(np.min(a1) + 1, 10000 + 10)
    #     if findFirstLarge(a1, 0, len(a1), N) == findFirstLarge_brute(a1, N):
    #         pass
    #     else:
    #         print(a1, N)
    #         break
    print(findFirstLargeOrEqual(nums1, 0, 9, 7))
    print(findFirstLargeOrEqual_brute(nums1, 7))
