#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(idx, total):
            if idx == len(nums):
                return total == target
            
            return dfs(idx + 1, total + nums[idx]) \
                + dfs(idx + 1, total - nums[idx])
        
        return dfs(0, 0)

# @lc code=end

