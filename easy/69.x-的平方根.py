#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (37.56%)
# Likes:    317
# Dislikes: 0
# Total Accepted:    100.4K
# Total Submissions: 267K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
#
#
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
# 由于返回类型是整数，小数部分将被舍去。
#
#
#

# @lc code=start


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x // 2
        midle = (left + right) // 2
        if x == 1:
            return 1
        while 1:
            if midle ** 2 <= x and (midle + 1) ** 2 > x:
                return midle
            else:
                if midle ** 2 <= x:
                    left = midle
                    midle = (left + right) // 2
                else:
                    right = midle
                    midle = (left + right) // 2
                if midle == left or midle == right:
                    return right

# @lc code=end
