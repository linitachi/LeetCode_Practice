#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
# https://leetcode-cn.com/problems/permutation-sequence/description/
#
# algorithms
# Hard (51.53%)
# Likes:    421
# Dislikes: 0
# Total Accepted:    66.5K
# Total Submissions: 129K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
# 给定 n 和 k，返回第 k 个排列。
#
# 说明：
#
#
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
#
#
# 示例 1:
#
# 输入: n = 3, k = 3
# 输出: "213"
#
#
# 示例 2:
#
# 输入: n = 4, k = 9
# 输出: "2314"
#
#
#

# @lc code=start


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def DFS(k, stack, input, answer, final):
            if len(stack) == k:
                answer.append(stack[:])
                return
            for i in input:
                stack.append(i)
                tem = input.copy()
                tem.pop(tem.index(i))
                DFS(k, stack, tem, answer, final)
                stack.pop()
                if len(answer) == final:
                    return answer[final-1]
        answer = []
        DFS(n, [], [i for i in range(1, n + 1)], answer, k)
        final_string = ""
        for i in answer[k - 1]:
            final_string += str(i)
        return final_string
        # @lc code=end
