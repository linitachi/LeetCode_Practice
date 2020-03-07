#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (47.58%)
# Likes:    259
# Dislikes: 0
# Total Accepted:    28.2K
# Total Submissions: 58.6K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
#

# @lc code=start


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        max_len = 1
        tem = 1
        for number in nums_set:
            if number - 1 not in nums_set:
                while 1:
                    if number + 1 not in nums_set:
                        break
                    tem += 1
                    number += 1
                if tem > max_len:
                    max_len = tem
                tem = 1
        return max_len
        # @lc code=end
