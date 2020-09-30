#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (76.98%)
# Likes:    924
# Dislikes: 0
# Total Accepted:    201K
# Total Submissions: 261K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def DFS(k, stack, input, answer):
            if len(stack) == k:
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
