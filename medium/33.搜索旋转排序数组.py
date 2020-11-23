#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (39.29%)
# Likes:    1075
# Dislikes: 0
# Total Accepted:    192.6K
# Total Submissions: 486.3K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 给你一个整数数组 nums ，和一个整数 target 。
#
# 该整数数组原本是按升序排列，但输入时在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2]
# ）。
#
# 请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
#
# 示例 1：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#
#
# 示例 2：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
#
# 示例 3：
#
#
# 输入：nums = [1], target = 0
# 输出：-1
#
#
#
#
# 提示：
#
#
# 1
# -10^4
# nums 中的每个值都 独一无二
# nums 肯定会在某个点上旋转
# -10^4
#
#
#

# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 使用二分搜尋法
        # 先用mid將nums切成兩半
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 當中間值小於尾端值時，代表mid~right之間一定是升序數列
            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                # 當中間值大於尾端值時，代表left~mid之間一定是升序數列
                if target >= nums[left] and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
        return -1
# @lc code=end
