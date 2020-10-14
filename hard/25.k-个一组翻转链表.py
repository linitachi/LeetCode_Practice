#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (63.13%)
# Likes:    756
# Dislikes: 0
# Total Accepted:    105.5K
# Total Submissions: 167K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
#
#
# 示例：
#
# 给你这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
#
#
# 说明：
#
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def helper(head, iteration):
            if iteration == 1:  # 元素足夠的時候
                return head, head, head.next, False
            if head.next == None:  # 元素不足夠的時候
                return head, head, None, True
            pre, last, next, isend = helper(head.next, iteration-1)
            last.next = head
            head.next = next
            return pre, head, next, isend
        if k == 1:
            return head
        elif head == None:
            return None
        last = head
        next_node = head
        first = 0
        front = ListNode(0)
        isend = False
        while last.next is not None:
            rt, last, next_node, isend = helper(next_node, k)
            if isend:
                rt, last, next_node, isend = helper(rt, k)
                last.next = next_node
                front.next = rt
                break
            front.next = rt
            front = last
            last.next = next_node
            if first == 0:
                first_node = rt
                first = 1
        return first_node
# @lc code=end
