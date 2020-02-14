#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (66.88%)
# Likes:    762
# Dislikes: 0
# Total Accepted:    153.9K
# Total Submissions: 230.1K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(head):
            if head == None or head.next == None:
                return head, head
            else:
                pre, last = helper(head.next)
                pre.next = head
                head.next = None
                return head, last
        _, answer = helper(head)
        return answer
# @lc code=end
