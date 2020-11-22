#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (70.15%)
# Likes:    1587
# Dislikes: 0
# Total Accepted:    297K
# Total Submissions: 422.4K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,1]
# 输出: 1
#
#
# 示例 2:
#
# 输入: [4,1,2,1,2]
# 输出: 4
#
#

# @lc code=start


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 透過字典來確認元素是否重複 有重複的都會先加進來再刪除，留下來的就是沒重複的元素
        num_dict = {}
        for num in nums:
            if num_dict.get(num) != None:
                del num_dict[num]
            else:
                num_dict[num] = 1
        return list(num_dict.keys())[0]
        # 透過exclusive or來做
        # return reduce(lambda x, y: x ^ y, nums)

# @lc code=end
