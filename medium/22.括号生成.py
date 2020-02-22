#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (73.16%)
# Likes:    760
# Dislikes: 0
# Total Accepted:    76K
# Total Submissions: 103.6K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#
#

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(n):
            if n == 0:
                return [""]
            elif n == 1:
                return ["()"]
            elif n == 2:
                return ["()()", "(())"]
            else:
                answer = []
                for i in range(n):
                    tem = helper(i)
                    tem2 = helper(n - 1 - i)
                    for j in tem:
                        for k in tem2:
                            answer.extend(["("+j+")"+k])
                return answer
        return helper(n)
        # @lc code=end
