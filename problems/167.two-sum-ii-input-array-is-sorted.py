#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            
            total = numbers[left] + numbers[right]

            if total == target:
                return left+1, right+1
            
            if total < target:
                left += 1

            if total > target:
                right -= 1

        

# @lc code=end

