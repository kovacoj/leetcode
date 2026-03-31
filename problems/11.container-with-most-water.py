#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0

        left, right = 0, len(height) - 1

        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return area

# @lc code=end

