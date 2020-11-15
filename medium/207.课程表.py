#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# https://leetcode-cn.com/problems/course-schedule/description/
#
# algorithms
# Medium (54.40%)
# Likes:    628
# Dislikes: 0
# Total Accepted:    82.4K
# Total Submissions: 151.3K
# Testcase Example:  '2\n[[1,0]]'
#
# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
#
# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
#
#
#
# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
#
# 示例 2:
#
# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
#
#
#
# 提示：
#
#
# 输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 1 <= numCourses <= 10^5
#
#
#

# @lc code=start


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 每一個list元素對應的都是各自課程的先修數量，
        # 如numCoursesOfPrerequisites[0]代表 課程編號0的先修課程數量
        numCoursesOfPrerequisites = [0 for i in range(numCourses)]
        # 每一個list的元素的先修課程為該index
        # FollowUpCourese[0]，代表這些元素的先修課程皆為編號0
        FollowUpCourese = [[] for i in range(numCourses)]

        # 先把所有先修課程數量，元素都建立好
        for course, prerequisite in prerequisites:
            numCoursesOfPrerequisites[course] += 1
            FollowUpCourese[prerequisite].append(course)
        queue = []

        # 並且從不用先修課程的課程開始修課
        for i in range(len(numCoursesOfPrerequisites)):
            if numCoursesOfPrerequisites[i] == 0:
                queue.append(i)

        while queue:
            study = queue.pop(0)

            numCourses -= 1

            # 把修課後，該堂課的後續課程的先修數量-1
            for i in FollowUpCourese[study]:
                numCoursesOfPrerequisites[i] -= 1
                # 檢查修完課後，是否有課程的先修數量變為0
                if numCoursesOfPrerequisites[i] == 0:
                    queue.append(i)

        return not numCourses

# @lc code=end
