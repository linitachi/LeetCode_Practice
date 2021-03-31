#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (61.71%)
# Likes:    520
# Dislikes: 0
# Total Accepted:    93.4K
# Total Submissions: 148.1K
# Testcase Example:  '[1,2,2]'
#
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#
#
# 示例 2：
#
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
# 提示：
#
#
# 1
# -10
#
#
#
#
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(ans, deep_length):
            if (deep_length == len(nums)):
                tem = ans.copy()
                tem.sort()
                if tem not in ans_list:
                    ans_list.append(tem[:])
                return
            helper(ans, deep_length + 1)
            ans.append(nums[deep_length])
            helper(ans, deep_length + 1)
            ans.pop()

        ans_list = []
        helper([], 0)
        return ans_list


# @lc code=end
