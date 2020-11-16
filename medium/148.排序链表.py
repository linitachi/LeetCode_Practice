#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (67.16%)
# Likes:    819
# Dislikes: 0
# Total Accepted:    102.8K
# Total Submissions: 153.2K
# Testcase Example:  '[4,2,1,3]'
#
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
# 进阶：
#
#
# 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
#
#
#
#
# 示例 1：
#
#
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#
#
# 示例 2：
#
#
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#
#
# 示例 3：
#
#
# 输入：head = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 5 * 10^4] 内
# -10^5 
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode-cn.com/problems/sort-list/solution/pai-xu-lian-biao-di-gui-die-dai-xiang-jie-by-cherr/


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def getListlength(head: ListNode) -> int:
            count = 0
            while head:
                count += 1
                head = head.next
            return count

        def cut_list(head, steps):
            # steps切成幾個node
            # 把鏈結切成兩邊
            if not head:
                return None
            while head and head.next and steps > 1:
                steps -= 1
                head = head.next
            right = head.next
            head.next = None
            return right

        def mergeTwoLists(l1, l2):
            if not l1 and not l2:
                return None
            elif l1 == None:
                return l2
            elif l2 == None:
                return l1
            if l1.val < l2.val:
                answer = l1
                l1 = l1.next
            else:
                answer = l2
                l2 = l2.next

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
            return answer

        length = getListlength(head)
        i = 1
        dummy = ListNode(0)
        dummy.next = head
        while i < length:
            pre = dummy
            cur = dummy.next
            # 跌代 將鏈結分成i布一份
            while cur:
                left = cur
                right = cut_list(cur, i)
                # 剩餘的節點
                cur = cut_list(right, i)
                # 將分割好的兩份合併
                tem = mergeTwoLists(left, right)
                # 合併完後，接起來(第一次接在dummy後面，後來則接在已排序好的鏈結後面)
                pre.next = tem
                while pre.next:
                    pre = pre.next
            i *= 2
        return dummy.next
        # @lc code=end
