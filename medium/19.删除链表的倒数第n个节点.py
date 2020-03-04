#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (37.38%)
# Likes:    706
# Dislikes: 0
# Total Accepted:    129.4K
# Total Submissions: 342.8K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
#
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tem = head
        answer_list = []
        while tem is not None:
            answer_list.append(tem)
            tem = tem.next
        if len(answer_list) == 1:
            return None
        if n == len(answer_list):
            return head.next
        if n > 1:
            answer_list[len(answer_list) - n -
                        1].next = answer_list[len(answer_list) - n + 1]
        else:
            answer_list[len(answer_list) - n -
                        1].next = None
        return head

        # @lc code=end
