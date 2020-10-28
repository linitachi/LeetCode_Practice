#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (50.84%)
# Likes:    947
# Dislikes: 0
# Total Accepted:    106K
# Total Submissions: 207.9K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +'[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
#
#
# 进阶:
#
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
#
#
# 示例:
#
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得关键字 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得关键字 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#
#
#

# @lc code=start


class DLinkListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self._first = DLinkListNode(None, None)
        self._last = DLinkListNode(None, None)
        self._first.next = self._last
        self._last.prev = self._first
        self._capacity = capacity

    def get(self, key: int) -> int:
        thisnode = self._first.next
        while thisnode.key is not None:
            if thisnode.key == key:  # 如果有找到
                self.moveToBack(thisnode)
                return thisnode.value
            thisnode = thisnode.next
        return -1

    def put(self, key: int, value: int) -> None:
        thisnode = self._first.next
        count = 0
        while thisnode.key is not None:
            count += 1
            if thisnode.key == key:  # 如果有找到 就更新值
                thisnode.value = value
                self.moveToBack(thisnode)
                return
            thisnode = thisnode.next
        new_node = DLinkListNode(key, value)
        if self._capacity > count:
            self.addToList(new_node)
        else:
            self.deleteNode(self._first.next)
            self.addToList(new_node)

    def moveToBack(self, node):
        self.deleteNode(node)
        self.addToList(node)

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToList(self, node):
        node.prev = self._last.prev
        node.next = self._last
        self._last.prev.next = node
        self._last.prev = node
        # @lc code=end
