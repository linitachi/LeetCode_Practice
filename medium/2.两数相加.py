#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (36.56%)
# Likes:    3876
# Dislikes: 0
# Total Accepted:    319.7K
# Total Submissions: 874.3K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0

        def helper(a, b, carry):
            if a == None and b == None:
                if carry == 1:
                    return ListNode(1)
            else:
                a = a if a else ListNode(0)
                b = b if b else ListNode(0)
                if carry == 1:
                    a.val = a.val+b.val+1
                else:
                    a.val = a.val+b.val
                if a.val > 9:
                    carry = 1
                    a.val = a.val % 10
                else:
                    carry = 0
                a.next = helper(a.next, b.next, carry)
                return a

        return helper(l1, l2, carry)


# @lc code=end
