#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (25.41%)
# Likes:    1823
# Dislikes: 0
# Total Accepted:    159.5K
# Total Submissions: 623.4K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        i = 0
        head = 1
        tail = len(nums) - 1
        answers = []
        while 1:
            number = nums[i] + nums[head] + nums[tail]
            if number < 0:
                head += 1
                while nums[head] == nums[head - 1]and head < tail:
                    head += 1
            elif number > 0:
                tail -= 1
                while nums[tail] == nums[tail + 1]and head < tail:
                    tail -= 1
            else:
                answers.append([nums[i], nums[head], nums[tail]])
                head += 1
                while nums[head] == nums[head - 1] and head < tail:
                    head += 1

                tail -= 1
                while nums[tail] == nums[tail + 1]and head < tail:
                    tail -= 1

            if head >= tail:
                tem = i
                for j in range(i, len(nums)-2):
                    if nums[i] != nums[j]:
                        i = j
                        head = i+1
                        tail = len(nums) - 1
                        break
                if tem == i:
                    break
        return answers

        # @lc code=end
