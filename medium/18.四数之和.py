#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (37.06%)
# Likes:    395
# Dislikes: 0
# Total Accepted:    60.3K
# Total Submissions: 161.7K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#
#
#

# @lc code=start


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def threeSum(nums, remineder, index, answers):
            i = index+1
            head = i+1
            tail = len(nums) - 1
            while 1:
                number = nums[i] + nums[head] + nums[tail]
                if number < remineder:
                    head += 1
                    while nums[head] == nums[head - 1]and head < tail:
                        head += 1
                elif number > remineder:
                    tail -= 1
                    while nums[tail] == nums[tail + 1]and head < tail:
                        tail -= 1
                else:
                    answers.append(
                        [nums[index], nums[i], nums[head], nums[tail]])
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
        if len(nums) < 4:
            return []
        nums.sort()
        index = 0
        remineder = target-nums[index]
        answers = []
        while 1:
            threeSum(nums, remineder, index, answers)
            tem = index
            for j in range(index, len(nums)-3):
                if nums[index] != nums[j]:
                    index = j
                    break
            remineder = target-nums[index]
            if tem == index:
                break
        return answers
# @lc code=end
