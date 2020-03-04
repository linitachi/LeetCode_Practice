#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (52.17%)
# Likes:    316
# Dislikes: 0
# Total Accepted:    66.1K
# Total Submissions: 126.7K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#
#

# @lc code=start


class Solution:

    def addBinary(self, a: str, b: str) -> str:
        anwser = ""
        carry = 0
        if len(a) > len(b):
            longer = a
            shorter = b
        else:
            longer = b
            shorter = a
        longer_index = len(longer) - 1
        shorter_index = len(shorter) - 1
        for i in range(shorter_index, -1, -1):
            if shorter[shorter_index] == "1" and longer[longer_index] == "1":
                if carry:
                    anwser = "1" + anwser
                else:
                    anwser = "0"+anwser
                    carry = 1
            elif shorter[shorter_index] == "1" or longer[longer_index] == "1":
                if carry:
                    anwser = "0" + anwser
                else:
                    anwser = "1"+anwser
            else:
                if carry:
                    anwser = "1"+anwser
                    carry = 0
                else:
                    anwser = "0"+anwser
            shorter_index -= 1
            longer_index -= 1
        for i in range(longer_index, -1, -1):
            if longer[longer_index] == "1" and carry == 1:
                anwser = "0"+anwser
            elif longer[longer_index] == "0" and carry == 1:
                anwser = "1"+anwser
                carry = 0
            elif longer[longer_index] == "1" and carry == 0:
                anwser = "1"+anwser
            elif longer[longer_index] == "0" and carry == 0:
                anwser = "0"+anwser
            longer_index -= 1
        if carry:
            anwser = "1" + anwser
        return anwser

        # @lc code=end
