#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#
# https://leetcode-cn.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (46.76%)
# Likes:    104
# Dislikes: 0
# Total Accepted:    42.8K
# Total Submissions: 90.9K
# Testcase Example:  '10\n6'
#
# 猜数字游戏的规则如下：
#
#
# 每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
# 如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
#
#
# 你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：
#
#
# -1：我选出的数字比你猜的数字小 pick < num
# 1：我选出的数字比你猜的数字大 pick > num
# 0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
#
#
# 返回我选出的数字。
#
#
#
# 示例 1：
#
#
# 输入：n = 10, pick = 6
# 输出：6
#
#
# 示例 2：
#
#
# 输入：n = 1, pick = 1
# 输出：1
#
#
# 示例 3：
#
#
# 输入：n = 2, pick = 1
# 输出：1
#
#
# 示例 4：
#
#
# 输入：n = 2, pick = 2
# 输出：2
#
#
#
#
# 提示：
#
#
# 1
# 1
#
#
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n+1

        while 1:
            midle = (right+left)//2
            if 0 == guess(midle):
                return midle
            elif guess(midle) == 1:
                left = midle+1
            elif guess(midle) == -1:
                right = midle-1
                # @lc code=end
