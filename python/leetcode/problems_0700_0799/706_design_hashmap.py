# -------------------
# 706. Design Hashmap
# -------------------

# Problem: https://leetcode.com/problems/design-hashmap/
# 
# Design a HashMap without using any built-in hash table libraries.
# 
# Implement the MyHashMap class:
# 
#   * MyHashMap() initializes the object with an empty map.
#   * void put(int key, int value) inserts a (key, value) pair into the HashMap. 
#     If the key already exists in the map, update the corresponding value.
#   * int get(int key) returns the value to which the specified key is mapped, 
#     or -1 if this map contains no mapping for the key.
#   * void remove(key) removes the key and its corresponding value if the map 
#     contains the mapping for the key.
# 
#  
# Example 1:
# 
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]
# 
# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
#  
# 
# Constraints:
# 
#   0 <= key, value <= 10^6
#   At most 10^4 calls will be made to put, get, and remove.


# Solution: https://youtu.be/cNWsgbKwwoU
# Credit: Navdeep Singh founder of NeetCode
class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for i in range(1000)]
        
    def hashcode(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hashcode(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)
         
    def get(self, key: int) -> int:
        cur = self.map[self.hashcode(key)].next
        while cur and cur.key != key:
            cur = cur.next
        if cur:
            return cur.val
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hashcode(key)]
        while cur.next and cur.next.key != key:
            cur = cur.next
        if cur and cur.next:
            cur.next = cur.next.next


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
