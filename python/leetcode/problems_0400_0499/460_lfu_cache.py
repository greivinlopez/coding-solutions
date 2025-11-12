# --------------
# 460. LFU Cache
# --------------

# Problem: https://leetcode.com/problems/lfu-cache/
#
# Design and implement a data structure for a Least Frequently Used (LFU) cache.
# 
# Implement the LFUCache class:
#        
#   * LFUCache(int capacity) Initializes the object with the capacity of the
#     data structure.
#   * int get(int key) Gets the value of the key if the key exists in the
#     cache. Otherwise, returns -1.
#   * void put(int key, int value) Update the value of the key if present, or
#     inserts the key if not already present. When the cache reaches its capacity, it
#     should invalidate and remove the least frequently used key before inserting a
#     new item. For this problem, when there is a tie (i.e., two or more keys with the
#     same frequency), the least recently used key would be invalidated.
# 
# To determine the least frequently used key, a use counter is maintained for each
# key in the cache. The key with the smallest use counter is the least frequently
# used key.
# 
# When a key is first inserted into the cache, its use counter is set to 1 (due to
# the put operation). The use counter for a key in the cache is incremented either
# a get or put operation is called on it.
# 
# The functions get and put must each run in O(1) average time complexity.
# 
# Example 1:
# 
# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get",
# "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
# 
# Explanation
# # cnt(x) = the use counter for key x
# # cache=[] will show the last used order for tiebreakers (leftmost element is
# most recent)
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   # cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   # cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      # return 1
#                  # cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   # 2 is the LFU key because cnt(2)=1 is the smallest,
# invalidate 2.
#                  # cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      # return -1 (not found)
# lfu.get(3);      # return 3
#                  # cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
#                  # cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      # return -1 (not found)
# lfu.get(3);      # return 3
#                  # cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      # return 4
#                  # cache=[4,3], cnt(4)=2, cnt(3)=3
# Constraints:
#         1 <= capacity <= 10^4
#         0 <= key <= 10^5
#         0 <= value <= 10^9
#         At most 2 * 10^5 calls will be made to get and put.

import collections

# Solution: https://youtu.be/bLEIHn-DgoA
# Credit: Navdeep Singh founder of NeetCode
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.map = {}

    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val, None)

    def popLeft(self):
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res
    
    def update(self, val):
        self.pop(val)
        self.pushRight(val)

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0
        self.valMap = {} # Map key -> val
        self.countMap = collections.defaultdict(int) # Map key -> count
        self.listMap = collections.defaultdict(LinkedList) # Map count of key -> linkedlist

    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].pushRight(key)

        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]
    
    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.lfuCnt].popLeft()
            self.valMap.pop(res)
            self.countMap.pop(res)

        self.valMap[key] = value
        self.counter(key)
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])

def main():
    lfu = LFUCache(2)
    lfu.put(1, 1)   # cache=[1,_], cnt(1)=1
    lfu.put(2, 2)   # cache=[2,1], cnt(2)=1, cnt(1)=1
    v = lfu.get(1)  # return 1
    print(v)
                    # cache=[1,2], cnt(2)=1, cnt(1)=2
    lfu.put(3, 3)   # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                    # cache=[3,1], cnt(3)=1, cnt(1)=2
    v = lfu.get(2)  # return -1 (not found)
    print(v)
    v = lfu.get(3)  # return 3
    print(v)
                    # cache=[3,1], cnt(3)=2, cnt(1)=2
    lfu.put(4, 4)   # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                    # cache=[4,3], cnt(4)=1, cnt(3)=2
    lfu.get(1)      # return -1 (not found)
    lfu.get(3)      # return 3
                    # cache=[3,4], cnt(4)=1, cnt(3)=3
    lfu.get(4)      # return 4
                    # cache=[4,3], cnt(4)=2, cnt(3)=3

if __name__ == "__main__":
    main()
