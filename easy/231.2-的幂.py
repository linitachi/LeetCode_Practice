#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (48.67%)
# Likes:    257
# Dislikes: 0
# Total Accepted:    84.7K
# Total Submissions: 173.9K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
# 示例 1:
#
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
#
# 示例 2:
#
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
#
# 示例 3:
#
# 输入: 218
# 输出: false
#
#

# @lc code=start


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ''' 
        因為是2的次方，以二進位來看，只會有一個1。
        2=0010
        4=0100
        8=01000
        所以如果不是只有一個1的話，就不是2的次方。
        如: 6=0110
        因此n的負數如果和n做and，就會等於原本的n
        如:8=01000
        -8=11001
        做and後，等於8
        '''
        if n == 0:
            return False
        return (n & -n) == n
        # @lc code=end
