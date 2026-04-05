#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
from collections import Counter

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = Counter(moves)

        return counter['U'] == counter['D'] \
            and counter['L'] == counter['R']

# @lc code=end

