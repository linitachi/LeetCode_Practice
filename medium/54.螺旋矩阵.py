#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (38.65%)
# Likes:    312
# Dislikes: 0
# Total Accepted:    43.8K
# Total Submissions: 112.7K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
#
#
# 示例 2:
#
# 输入:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#

# @lc code=start


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m為長度、n為高度
        if not matrix:
            return []
        n = len(matrix)
        m = len(matrix[0])

        anwser_list = []
        n_head = 0
        m_head = 0
        while 1:
            for i in range(m_head, m):
                anwser_list.append(matrix[m_head][i])
            n_head += 1
            if n_head == n:
                break

            for i in range(n_head, n):
                anwser_list.append(matrix[i][m-1])
            m -= 1
            if m == m_head:
                break
            for i in range(m-1, m_head-1, -1):
                anwser_list.append(matrix[n-1][i])

            n -= 1
            if n == n_head:
                break
            for i in range(n-1, n_head-1, -1):
                anwser_list.append(matrix[i][m_head])
            m_head += 1
            if m_head == m:
                break
        return anwser_list
        print(anwser_list)

# @lc code=end
