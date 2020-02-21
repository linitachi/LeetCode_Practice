#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (42.85%)
# Likes:    365
# Dislikes: 0
# Total Accepted:    74.7K
# Total Submissions: 173.7K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
#
#

# @lc code=start


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return []
        nums.sort()
        i = 0
        head = 1
        tail = len(nums) - 1
        answer = 999999
        while 1:
            number = nums[i] + nums[head] + nums[tail]-target
            if number < 0:
                head += 1
                while nums[head] == nums[head - 1]and head < tail:
                    head += 1
            elif number > 0:
                tail -= 1
                while nums[tail] == nums[tail + 1]and head < tail:
                    tail -= 1
            else:
                return target
            answer = number+target if abs(
                answer-target) > abs(number) else answer
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
        return answer
# @lc code=end
