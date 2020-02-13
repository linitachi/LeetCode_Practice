#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start


class Solution:
    def reverse(self, x: int) -> int:
        # if x < 0:
        #     x = -x
        #     x = '-'+str(x)[::-1]
        # else:
        #     x = str(x)[::-1]
        # x = int(x)
        # if x < -2**(31) or x > 2**31-1:
        #     x = 0
        # return x
        if x < 0:
            x = -x
            a = list(map(int, str(x)))
            degree = 0
            final = 0
            for i in a:
                final = final - i * (10 ** degree)
                degree += 1
                if final < -2**(31):
                    final = 0
            return final
        else:
            a = list(map(int, str(x)))
            degree = 0
            final = 0
            for i in a:
                final = final + i * (10 ** degree)
                degree += 1
            if final > 2**31-1:
                final = 0
            return final

        # @lc code=end
