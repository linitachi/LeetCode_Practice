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
        def mergeTwoLists(l1, l2):
            answer = ListNode(0)
            temp = answer
            while l1 and l2:
                if l1.val < l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
                temp = temp.next
            temp.next = l1 if l1 is not None else l2
            return answer.next
        lists_length = len(lists)
        interval = 1
        while lists_length > interval:
            for i in range(0, lists_length - interval, interval * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        if lists_length > 0:
            return lists[0]
        else:
            None


# @lc code=end
