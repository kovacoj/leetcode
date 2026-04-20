#
# @lc app=leetcode id=2078 lang=python3
#
# [2078] Two Furthest Houses With Different Colors
#

# @lc code=start
from functools import lru_cache

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        @lru_cache
        def helper(left, right):
            if colors[left] != colors[right]:
                return right - left

            return max(
                helper(left + 1, right), helper(left, right - 1)
            )

        return helper(0, len(colors) - 1)



        
# @lc code=end

