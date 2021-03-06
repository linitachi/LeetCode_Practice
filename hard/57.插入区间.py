#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# https://leetcode-cn.com/problems/insert-interval/description/
#
# algorithms
# Hard (36.78%)
# Likes:    110
# Dislikes: 0
# Total Accepted:    16.7K
# Total Submissions: 45.2K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
# 示例 1:
#
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
#
#
# 示例 2:
#
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
#
#
#

# @lc code=start


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals):
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
        intervals.append(newInterval)
        return merge(intervals)

# @lc code=end
