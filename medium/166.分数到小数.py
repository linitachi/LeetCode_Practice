#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#
# https://leetcode-cn.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (27.85%)
# Likes:    178
# Dislikes: 0
# Total Accepted:    16.7K
# Total Submissions: 59.8K
# Testcase Example:  '1\n2'
#
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。
#
# 如果小数部分为循环小数，则将循环的部分括在括号内。
#
# 如果存在多个答案，只需返回 任意一个 。
#
# 对于所有给定的输入，保证 答案字符串的长度小于 10^4 。
#
#
#
# 示例 1：
#
#
# 输入：numerator = 1, denominator = 2
# 输出："0.5"
#
#
# 示例 2：
#
#
# 输入：numerator = 2, denominator = 1
# 输出："2"
#
#
# 示例 3：
#
#
# 输入：numerator = 2, denominator = 3
# 输出："0.(6)"
#
#
# 示例 4：
#
#
# 输入：numerator = 4, denominator = 333
# 输出："0.(012)"
#
#
# 示例 5：
#
#
# 输入：numerator = 1, denominator = 5
# 输出："0.2"
#
#
#
#
# 提示：
#
#
# -2^31
# denominator != 0
#
#
#

# @lc code=start


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:  # 分子為0
            return "0"
        answer = ""
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):  # 判斷正負號
            answer += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        Quotient, Remainder = divmod(numerator, denominator)
        answer += str(Quotient)
        if Remainder == 0:  # 判斷是否整除
            return answer
        # 沒有整除的話 Remainder的數字一定比denominator小 因此開始處理小數點後面
        answer += "."

        Remainder_dict = {}
        while True:  # 小數點後面
            if Remainder in Remainder_dict:
                answer = list(answer)
                answer.insert(Remainder_dict[Remainder], "(")
                answer.append(")")
                return "".join(answer)
            Remainder_dict[Remainder] = len(answer)
            Remainder *= 10
            Quotient, Remainder = divmod(Remainder, denominator)
            answer += str(Quotient)
            if Remainder == 0:  # 整除的話
                return answer


# @lc code=end
