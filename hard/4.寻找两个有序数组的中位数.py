#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (36.74%)
# Likes:    2150
# Dislikes: 0
# Total Accepted:    141K
# Total Submissions: 383.7K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
#
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
#
#

# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def help(list1):
            if len(list1) % 2 != 0:
                return list1[int(len(nums1)/2+0.5)-1]
            else:
                return (list1[int(len(nums1)/2)]+list1[int(len(nums1)/2)-1])/2
        nums1.extend(nums2)
        nums1.sort()
        return help(nums1)

# @lc code=end
