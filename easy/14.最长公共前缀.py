#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (36.06%)
# Likes:    880
# Dislikes: 0
# Total Accepted:    186.9K
# Total Submissions: 516.9K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        shortest = min(strs, key=lambda x: len(x))
        answer = ""
        for i in range(len(shortest)):
            for j in range(len(strs)):
                if strs[j][:i+1:].find(shortest[:i+1:]) == -1:
                    return answer
            answer = shortest[:i+1:]
        return answer

        # @lc code=end
