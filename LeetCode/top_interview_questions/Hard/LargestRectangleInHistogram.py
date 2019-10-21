from typing import List


class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        length = len(heights)
        less_to_left = [-1] * length
        less_to_right = [length] * length

        for i in range(1, length):
            p = i - 1
            while p >= 0 and heights[i] <= heights[p]:
                p = less_to_left[p]

            less_to_left[i] = p

        for i in range(length - 2, -1, -1):
            p = i + 1
            while p < length and heights[i] <= heights[p]:
                p = less_to_right[p]

            less_to_right[i] = p

        histograms = [heights[i] * (less_to_right[i] - less_to_left[i] - 1) for i in range(length)]

        return max(histograms)


if __name__ == '__main__':
    l = [2, 1, 5, 6, 2, 3]
    s = Solution1()
    print(s.largestRectangleArea(l), end='')
