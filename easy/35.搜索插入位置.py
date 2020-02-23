#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (45.07%)
# Likes:    435
# Dislikes: 0
# Total Accepted:    120.4K
# Total Submissions: 266.4K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。
#
# 示例 1:
#
# 输入: [1,3,5,6], 5
# 输出: 2
#
#
# 示例 2:
#
# 输入: [1,3,5,6], 2
# 输出: 1
#
#
# 示例 3:
#
# 输入: [1,3,5,6], 7
# 输出: 4
#
#
# 示例 4:
#
# 输入: [1,3,5,6], 0
# 输出: 0
#
#
#

# @lc code=start


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = (left + right) // 2
        if nums[right] < target:
            return len(nums)
        elif nums[left] > target:
            return 0
        while 1:
            if nums[mid] == target:
                return mid
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            # 往大的走
            elif nums[mid] < target:
                left = mid
            # 往小的走
            elif nums[mid] > target:
                right = mid
            mid = (left + right) // 2
            if mid == left:
                return left+1
            elif mid == right:
                return right

        #  暴力法
        # for i in range(len(nums)):
        #     if nums[i] >= target:
        #         return i
        # return len(nums)

# @lc code=end
