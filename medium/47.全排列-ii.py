#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (62.12%)
# Likes:    505
# Dislikes: 0
# Total Accepted:    116.8K
# Total Submissions: 188K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
#
#

# @lc code=start


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def DFS(k, stack, input, answer):
            if len(stack) == k and stack[:] not in answer:
                answer.append(stack[:])
                return
            for i in input:
                stack.append(i)
                tem = input.copy()
                tem.pop(tem.index(i))
                DFS(k, stack, tem, answer)
                stack.pop()
        if nums:
            answer = []
            DFS(len(nums), [], nums, answer)
            return answer
        else:
            return []
# @lc code=end
