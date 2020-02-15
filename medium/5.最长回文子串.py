#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (28.40%)
# Likes:    1751
# Dislikes: 0
# Total Accepted:    181.7K
# Total Submissions: 638K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
#
#

# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(s, length):
            for i in range(len(s)-length+1):
                if s[i: i + length] == s[i + length - 1: i-1:-1]:
                    return (s[i: i + length])
                elif i == 0 and s[i: i + length] == s[i + length - 1::-1]:
                    return (s[i: i + length])
            return ""
        if len(s) == 1:
            return s
        elif len(s) == 0:
            return ""
        for i in range(len(s), 0, -1):
            if helper(s, i) != "":
                return helper(s, i)
        return s[0]

# @lc code=end
