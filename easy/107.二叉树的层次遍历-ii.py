#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (64.30%)
# Likes:    230
# Dislikes: 0
# Total Accepted:    55.7K
# Total Submissions: 85.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回其自底向上的层次遍历为：
#
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        vallist = []
        temlist = []
        processQueue = Queue()
        processQueue.put(root)
        temQueue = Queue()
        while root is not None:
            root = processQueue.get()
            temlist.append(root.val)
            if root.left is not None:
                temQueue.put(root.left)
            if root.right is not None:
                temQueue.put(root.right)
            if processQueue.empty():
                while not temQueue.empty():
                    processQueue.put(temQueue.get())
                vallist.append(temlist.copy())
                temlist.clear()
            if processQueue.empty() and temQueue.empty():
                break
        vallist.reverse()
        return vallist

        # @lc code=end
