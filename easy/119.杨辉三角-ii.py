#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (61.91%)
# Likes:    181
# Dislikes: 0
# Total Accepted:    71.2K
# Total Submissions: 115.1K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]
#
#
# 进阶：
#
# 你可以优化你的算法到 O(k) 空间复杂度吗？
#
#

# @lc code=start


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def calculate_next_row(input_list):
            next_list = [1] * (len(input_list)+1)
            for i in range(1, len(next_list)-1):
                next_list[i] = input_list[i - 1] + input_list[i]
            return next_list
        if rowIndex:
            temp_list = [1]
            while rowIndex > 0:
                temp_list = calculate_next_row(temp_list)
                rowIndex -= 1
            return temp_list
        elif rowIndex == 0:
            return [1]
        else:
            return []

        # @lc code=end
