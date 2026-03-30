#
# @lc app=leetcode id=2840 lang=python3
#
# [2840] Check if Strings Can be Made Equal With Operations II
#

# @lc code=start
from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) \
            and Counter(s1[1::2]) == Counter(s2[1::2])
# @lc code=end

