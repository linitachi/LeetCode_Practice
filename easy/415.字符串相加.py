#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (51.87%)
# Likes:    274
# Dislikes: 0
# Total Accepted:    82.5K
# Total Submissions: 159K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
#
#
# 提示：
#
#
# num1 和num2 的长度都小于 5100
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
#
#
#

# @lc code=start


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        answer = 0
        times = 1
        dig = -1
        for i in range(max(len(num1), len(num2)) - 1, -1, -1):
            try:
                tem = int(num1[dig]) + int(num2[dig])
            except:
                try:
                    tem = int(num1[dig])
                except:
                    tem = int(num2[dig])
            answer += tem * times
            dig -= 1
            times *= 10
        return str(answer)
# @lc code=end
