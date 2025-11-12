# -------------------
# 705. Design Hashset
# -------------------

# Problem: https://leetcode.com/problems/design-hashset/
# 
# Design a HashSet without using any built-in hash table libraries.
# 
# Implement MyHashSet class:
# 
#   * void add(key) Inserts the value key into the HashSet.
#   * bool contains(key) Returns whether the value key exists in the HashSet 
#     or not.
#   * void remove(key) Removes the value key in the HashSet. If key does not 
#     exist in the HashSet, do nothing.
# 
#  
# Example 1:
# 
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
# 
# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
#  
# 
# Constraints:
# 
#   0 <= key <= 10^6
#   At most 10^4 calls will be made to add, remove, and contains.


# Solution: https://youtu.be/VymjPQUXjL8
# Credit: Navdeep Singh founder of NeetCode
class MyHashSet:
    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.hashset else False


def main():
    hs = MyHashSet()
    hs.add(1)               # set = [1]
    hs.add(2)               # set = [1, 2]
    print(hs.contains(1))   # return True
    print(hs.contains(3))   # return False, (not found)
    hs.add(2)               # set = [1, 2]
    print(hs.contains(2))   # return True
    hs.remove(2)            # set = [1]
    print(hs.contains(2))   # return False, (already removed)

if __name__ == "__main__":
    main()
