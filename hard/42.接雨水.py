#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (48.39%)
# Likes:    873
# Dislikes: 0
# Total Accepted:    55.6K
# Total Submissions: 114.1K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#
#

# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        left_index, right_index = 0, len(height) - 1
        left_max, right_max = 0, 0
        answer = 0
        while left_index < right_index:
            if height[left_index] < left_max:
                answer += left_max - height[left_index]
            else:
                left_max = height[left_index]
            if height[right_index] < right_max:
                answer += right_max - height[right_index]
            else:
                right_max = height[right_index]
            if height[left_index] > height[right_index]:
                right_index -= 1
            elif height[left_index] <= height[right_index]:
                left_index += 1
        return answer
        # @lc code=end
