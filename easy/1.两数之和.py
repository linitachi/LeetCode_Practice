#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力法
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
        # a = {}
        # for i in range(len(nums)):
        #     Remaining = target - nums[i]
        #     if a.get(nums[i]) != None:
        #         return [a.get(nums[i]), i]
        #     else:
        #         a[Remaining] = i


# @lc code=end
