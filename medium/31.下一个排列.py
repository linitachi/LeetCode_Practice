#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (32.77%)
# Likes:    391
# Dislikes: 0
# Total Accepted:    43.8K
# Total Submissions: 133.1K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#

# @lc code=start


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return None

        for i in range(len(nums) - 1, 0, -1):
            # 當發生 i>i-1時，代表要交換了
            if nums[i] > nums[i - 1]:
                for j in range(i, len(nums)):
                    # 從i開始看到尾巴，找到一個比i-1小或相等的數字，那麼j-1就比i-1的數字大一點，就可以交換跟reverse
                    if nums[j] <= nums[i - 1]:
                        nums[j - 1], nums[i - 1] = nums[i - 1], nums[j - 1]
                        nums[i: len(nums)] = nums[len(nums) - 1:i-1:-1]
                        return None
                # 如果上面的都沒找到，可能像是132這種輸入，1小於其他的3、2，因此我們判斷尾巴是否大於i-1，如果有那麼就交換跟reverse
                if nums[len(nums) - 1] > nums[i - 1]:
                    nums[len(nums) - 1], nums[i - 1] = nums[i -
                                                            1], nums[len(nums) - 1]
                    nums[i: len(nums)] = nums[len(nums) - 1: i - 1:-1]
                    return None
                # 如果都沒發生上面那種情況，就直接交換即可
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                return None
        # 都找不到，那麼就直接reverse
        nums[::] = nums[::-1]
        return None


# @lc code=end
