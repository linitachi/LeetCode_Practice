#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (67.61%)
# Likes:    712
# Dislikes: 0
# Total Accepted:    157.7K
# Total Submissions: 233K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#
#
#

# @lc code=start


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 因為只能往右或是往下走，因此距離只需考慮左邊跟上面即可
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    # 最上面一排 最短距離一定都是前一步的距離+自己的距離
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    # 最左邊一排 最短距離一定都是前一步的距離+自己的距離
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    # 最短距離是左邊跟上面取最小值+自己的距離
                    grid[i][j] = min(grid[i - 1][j], grid[i]
                                     [j - 1]) + grid[i][j]
        return grid[-1][-1]
        # @lc code=end
