from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = []
        i, j = 0, 0
        while i < len(nums1) and j < n:
            while i < len(nums1) and nums1[i] < nums2[j]:
                i += 1

            nums1.insert(i, nums2[j])
            j += 1

        if j < n:
            nums1.extend(nums2[j:])


if __name__ == '__main__':
    a = [1, 2, 3, 0, 0, 0]
    b = [2, 5, 6]
    s = Solution()
    s.merge(a, 3, b, 3)
    print(a)
