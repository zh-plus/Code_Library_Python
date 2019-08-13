import warnings

import numpy as np

from LeetCode.top_interview_questions.Hard.FindMedianSortedArrays import Solution


def brute_force(nums1, nums2):
    nums = nums1 + nums2
    half = len(nums) // 2
    nums.sort()

    return nums[half] if len(nums) % 2 == 1 else (nums[half] + nums[half - 1]) / 2


for i in range(100000):
    len1 = np.random.randint(0, 5000)
    len2 = np.random.randint(0, 5000)

    nums1 = sorted(np.random.randint(0, 100, len1))
    nums2 = sorted(np.random.randint(0, 100, len2))
    # print(' '.join(list(map(str, nums1))), ' '.join(list(map(str, nums2))), sep='\n')
    # print()
    s = Solution()
    my_answer = s.findMedianSortedArrays(nums1, nums2)
    brute_answer = brute_force(nums1, nums2)
    if my_answer != brute_answer:
        print(my_answer, brute_answer)
        warnings.warn('not correct!')
        break
    else:
        print(i)

# 0 0 3 4 5
# 2 3 3 4 5
