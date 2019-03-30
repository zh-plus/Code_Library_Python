from typing import List

read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split(' ')))


class Solution:
    def find_medium(self, nums):
        half = len(nums) // 2
        return nums[half] if len(nums) % 2 == 1 else (nums[half] + nums[half - 1]) / 2

    def findNthNumber(self, nums1, nums2, N):
        if not nums1:
            return nums2[N - 1]

        if not nums2:
            return nums1[N - 1]

        if len(nums1) + len(nums2) <= 3:
            # print(len(nums1) + len(nums2), N)
            # print(nums1, nums2)
            nums = list(nums1) + list(nums2)
            nums.sort()
            # print(nums)
            return nums[N - 1]

        half1, half2 = len(nums1) // 2, len(nums2) // 2
        if nums1[half1] < nums2[half2]:
            half1 = self.findFirstLargeOrEqual(nums1, half1, len(nums1), nums2[half2])
        elif nums1[half1] > nums2[half2]:
            half2 = self.findFirstLargeOrEqual(nums2, half2, len(nums2), nums1[half1])
        else:
            temp = nums1[half1]
            half1 = self.findFirstLargeOrEqual(nums1, 0, len(nums1), temp)
            half2 = self.findFirstLargeOrEqual(nums2, 0, len(nums2), temp)

            left = half1 + half2
            if left == 0:
                temp = temp + 1
                half1 = self.findFirstLargeOrEqual(nums1, 0, len(nums1), temp)
                half2 = self.findFirstLargeOrEqual(nums2, 0, len(nums2), temp)

                if half1 + half2 == len(nums1) + len(nums2):
                    half1 = nums1.index(nums1[-1])
                    half2 = nums2.index(nums2[-1])

                    if half1 + half2 == 0:
                        return nums1[0]

        left = half1 + half2

        if N <= left:
            return self.findNthNumber(nums1[:half1], nums2[:half2], N)
        else:
            return self.findNthNumber(nums1[half1:], nums2[half2:], N - left)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        half = (len(nums1) + len(nums2)) // 2
        if (len(nums1) + len(nums2)) % 2 == 1:
            return float(self.findNthNumber(nums1, nums2, half + 1))
        else:
            return (self.findNthNumber(nums1, nums2, half) + self.findNthNumber(nums1, nums2, half + 1)) / 2

    def findFirstLargeOrEqual(self, nums, left, right, N):
        if right - left < 2:
            if nums[right - 1] < N:
                return right
            elif nums[left] < N:
                return left + 1
            else:
                return left

        half = (left + right) // 2
        if nums[half] < N:
            return self.findFirstLargeOrEqual(nums, half, right, N)
        else:
            return self.findFirstLargeOrEqual(nums, left, half, N)


if __name__ == '__main__':
    nums1 = read_ints()
    nums2 = read_ints()
    s = Solution()
    print(sorted(nums1 + nums2))
    print(s.findMedianSortedArrays(nums1, nums2))
