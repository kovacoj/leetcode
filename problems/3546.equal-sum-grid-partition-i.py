#
# @lc app=leetcode id=3546 lang=python3
#
# [3546] Equal Sum Grid Partition I
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        for sums in [
            [sum(row) for row in grid],
            [sum(col) for col in zip(*grid)],
        ]:
            left, right = 0, sum(sums)

            for value in sums:
                left += value
                right -= value

                if left == right:
                    return True
        
        return False

# @lc code=end

