#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (66.78%)
# Likes:    638
# Dislikes: 0
# Total Accepted:    154.3K
# Total Submissions: 231.1K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def exchange(element, front, behind):
            if element.next:
                # 交換節點
                change = element.next
                change.next = element
                change.next.next = behind
                front.next = change
            return change.next, behind
        if head:
            if head.next is None:
                return head
            begin = head.next
            tem = head
            head = ListNode(0)
            while tem and tem.next:
                head, tem = exchange(tem, head, tem.next.next)
            return begin
        else:
            return []
# @lc code=end
