#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.76%)
# Likes:    1385
# Dislikes: 0
# Total Accepted:    204.5K
# Total Submissions: 500.6K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        answer_dict = {"{": "}", "(": ")", "[": "]"}
        answer_list = []
        if s == "":
            return True
        for i in range(len(s)):
            # 如果是{ [ (
            if answer_dict.get(s[i]):
                answer_list.append(answer_dict.get(s[i]))
            else:
                try:
                    if answer_list.pop() != s[i]:
                        return False
                except:
                    return False
        if len(answer_list) > 0:
            return False
        return True

        # @lc code=end
