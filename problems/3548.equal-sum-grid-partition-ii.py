#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
from collections import defaultdict

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        def can_discard(target, cnt, h, w, corners):
            """Can we remove a cell with value=target from an h x w rectangular section?
            - h>=2, w>=2: any cell removal keeps rectangle connected
            - single row/col: only endpoints are removable
            - 1x1: nothing removable
            """
            if h >= 2 and w >= 2:
                return cnt.get(target, 0) > 0
            if h >= 2 or w >= 2:          # thin strip (1×w or h×1)
                return target in corners
            return False                   # 1×1 section

        # ---- Horizontal cuts (cut after row i) ----
        if m >= 2:
            top_cnt = defaultdict(int)
            bot_cnt = defaultdict(int)
            for row in grid:
                for v in row:
                    bot_cnt[v] += 1
            top_sum = 0
            for i in range(m - 1):
                for c in range(n):
                    v = grid[i][c]
                    top_cnt[v] += 1
                    bot_cnt[v] -= 1
                    if bot_cnt[v] == 0:
                        del bot_cnt[v]
                    top_sum += v
                diff = 2 * top_sum - total        # top_sum - bot_sum
                if diff == 0:
                    return True
                if diff > 0:                      # discard from top section
                    th = i + 1
                    corners = (grid[0][0], grid[0][n - 1]) if th == 1 else \
                              (grid[0][0], grid[i][0]) if n == 1 else ()
                    if can_discard(diff, top_cnt, th, n, corners):
                        return True
                else:                             # discard from bottom section
                    bh = m - i - 1
                    corners = (grid[m - 1][0], grid[m - 1][n - 1]) if bh == 1 else \
                              (grid[i + 1][0], grid[m - 1][0]) if n == 1 else ()
                    if can_discard(-diff, bot_cnt, bh, n, corners):
                        return True

        # ---- Vertical cuts (cut after column j) ----
        if n >= 2:
            left_cnt = defaultdict(int)
            right_cnt = defaultdict(int)
            for row in grid:
                for v in row:
                    right_cnt[v] += 1
            left_sum = 0
            for j in range(n - 1):
                for r in range(m):
                    v = grid[r][j]
                    left_cnt[v] += 1
                    right_cnt[v] -= 1
                    if right_cnt[v] == 0:
                        del right_cnt[v]
                    left_sum += v
                diff = 2 * left_sum - total       # left_sum - right_sum
                if diff == 0:
                    return True
                if diff > 0:                      # discard from left section
                    lw = j + 1
                    corners = (grid[0][0], grid[m - 1][0]) if lw == 1 else \
                              (grid[0][0], grid[0][j]) if m == 1 else ()
                    if can_discard(diff, left_cnt, m, lw, corners):
                        return True
                else:                             # discard from right section
                    rw = n - j - 1
                    corners = (grid[0][n - 1], grid[m - 1][n - 1]) if rw == 1 else \
                              (grid[0][j + 1], grid[0][n - 1]) if m == 1 else ()
                    if can_discard(-diff, right_cnt, m, rw, corners):
                        return True

        return False
# @lc code=end

