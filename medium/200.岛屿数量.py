#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (50.68%)
# Likes:    835
# Dislikes: 0
# Total Accepted:    172K
# Total Submissions: 338.6K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
#
# 示例 1：
#
#
# 输入：grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# 输出：1
#
#
# 示例 2：
#
#
# 输入：grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# 输出：3
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1
# grid[i][j] 的值为 '0' 或 '1'
#
#
#

# @lc code=start


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(grid, i, j):
            if i != 0 and grid[i - 1][j] == "1":
                grid[i - 1][j] = "a"
                helper(grid, i-1, j)
            if i != m-1 and grid[i+1][j] == "1":
                grid[i + 1][j] = "a"
                helper(grid, i+1, j)
            if j != 0 and grid[i][j-1] == "1":
                grid[i][j - 1] = "a"
                helper(grid, i, j-1)
            if j != n-1 and grid[i][j+1] == "1":
                grid[i][j + 1] = "a"
                helper(grid, i, j+1)

        m = len(grid)  # Y軸
        n = len(grid[0][:])  # X軸
        numberOfIlands = 0
        i = 0
        while i < m:
            j = 0
            while j < n:
                if grid[i][j] != "0":
                    if grid[i][j] == "1":
                        numberOfIlands += 1
                    grid[i][j] = "a"
                    helper(grid, i, j)
                j += 1
            i += 1
        return numberOfIlands
    # @lc code=end
