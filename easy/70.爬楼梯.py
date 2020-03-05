#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (47.88%)
# Likes:    864
# Dislikes: 0
# Total Accepted:    144K
# Total Submissions: 299.8K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#
#
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n, anwser_list):
            if n == 1:
                return 1
            if n == 2:
                return 2
            elif n == 3:
                return 3
            else:
                if anwser_list.get(n - 2) == None:
                    anwser_list[n-2] = helper(n-2, anwser_list)
                if anwser_list.get(n - 1) == None:
                    anwser_list[n-1] = helper(n-1, anwser_list)
                anwser_list[n] = anwser_list[n-2]+anwser_list[n-1]
            return anwser_list[n]
        anwser_list = {}
        return helper(n, anwser_list)
        # @lc code=end
