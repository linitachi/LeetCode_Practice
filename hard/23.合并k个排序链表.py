#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (48.68%)
# Likes:    497
# Dislikes: 0
# Total Accepted:    75.8K
# Total Submissions: 154.9K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        i = -1
        while 1:
            i += 1
            if not lists:
                return None
            elif not lists[i]:
                lists.pop(i)
                i -= 1
            else:
                break

        answer = ListNode(0)

        tem = answer
        tem.next = None
        while len(lists):
            j = 0
            tem.next = lists[0]
            i = 1
            while i != len(lists):
                if lists[i] == None:
                    lists.pop(i)
                    i -= 1
                if lists[j].val > lists[i].val:
                    tem.next = lists[i]
                    j = i
                i += 1
            lists[j] = lists[j].next
            tem = tem.next
            if lists[j] == None:
                lists.pop(j)
            if len(lists) == 1:
                tem.next = lists[0]
                break
        return answer.next


# @lc code=end
