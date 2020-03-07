#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (40.14%)
# Likes:    302
# Dislikes: 0
# Total Accepted:    57.8K
# Total Submissions: 142.6K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#

# @lc code=start


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        index = 1
        compare = 0
        while index < len(intervals):
            if intervals[compare][0] <= intervals[index][1] and intervals[compare][1] >= intervals[index][0]:
                tem = [min(intervals[compare][0], intervals[index][0]),
                       max(intervals[compare][1], intervals[index][1])]
                index += 1
                compare += 1
                intervals[compare] = tem
            else:
                answer.append(intervals[compare])
                index += 1
                compare += 1
        if compare == len(intervals):
            return answer
        answer.append(intervals[compare])
        return answer
        # @lc code=end
