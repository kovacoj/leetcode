#
# @lc app=leetcode id=2515 lang=python3
#
# [2515] Shortest Distance to Target String in a Circular Array
#

# @lc code=start
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)

        for step in range(n):
            right = (startIndex + step) % n
            left = (startIndex - step) % n

            if words[right] == target or words[left] == target:
                return step

        return -1


# @lc code=end

