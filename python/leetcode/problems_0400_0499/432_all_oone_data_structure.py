# -----------------------------
# 432. All O`one Data Structure
# -----------------------------

# Problem: https://leetcode.com/problems/all-oone-data-structure
#
# Design a data structure to store the strings' count with the ability to return
# the strings with minimum and maximum counts.
# 
# Implement the AllOne class:    
#   * AllOne() Initializes the object of the data structure.
#   * inc(String key) Increments the count of the string key by 1. If key does
#     not exist in the data structure, insert it with count 1.
#   * dec(String key) Decrements the count of the string key by 1. If the
#     count of key is 0 after the decrement, remove it from the data structure. It is
#     guaranteed that key exists in the data structure before the decrement.
#   * getMaxKey() Returns one of the keys with the maximal count. If no element exists,
#     return an empty string "".
#   * getMinKey() Returns one of the keys with the minimum count. If no
#     element exists, return an empty string "".
# 
# Note that each function must run in O(1) average time complexity.
# 
# Example 1:
# 
# Input
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey",
# "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# Output
# [null, null, null, "hello", "hello", null, "hello", "leet"]
# 
# Explanation
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "leet"
# 
# 
# Constraints:
#   1 <= key.length <= 10
#   key consists of lowercase English letters.
#   It is guaranteed that for each call to dec, key is existing in the data structure.
#   At most 5 * 10⁴ calls will be made to inc, dec, getMaxKey, and getMinKey.


# Solution: https://leetcode.com/problems/all-oone-data-structure/solutions/5846003/python-doubly-linked-list-ordered-hashing
class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        # Initialize the doubly linked list with dummy head and tail
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_node_map = {}  # Maps keys to their corresponding node

    def _add_node(self, prev_node, freq):
        """Add a new node with given frequency after the prev_node."""
        new_node = Node(freq)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node
        return new_node

    def _remove_node_if_empty(self, node):
        """Remove the node if it has no keys."""
        if not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key in self.key_node_map:
            current_node = self.key_node_map[key]
            current_node.keys.remove(key)

            next_freq = current_node.freq + 1
            next_node = current_node.next

            # If the next node doesn't exist or doesn't have the right frequency, create it
            if next_node == self.tail or next_node.freq != next_freq:
                next_node = self._add_node(current_node, next_freq)

            next_node.keys.add(key)
            self.key_node_map[key] = next_node

            # Remove the current node if empty
            self._remove_node_if_empty(current_node)
        else:
            # If key is new, add it to the first node (freq=1) or create it
            first_node = self.head.next
            if first_node == self.tail or first_node.freq != 1:
                first_node = self._add_node(self.head, 1)
            first_node.keys.add(key)
            self.key_node_map[key] = first_node

    def dec(self, key: str) -> None:
        if key not in self.key_node_map:
            return

        current_node = self.key_node_map[key]
        current_node.keys.remove(key)

        if current_node.freq == 1:
            # If the frequency is 1, remove the key entirely
            del self.key_node_map[key]
        else:
            prev_freq = current_node.freq - 1
            prev_node = current_node.prev

            # If the previous node doesn't exist or doesn't have the right frequency, create it
            if prev_node == self.head or prev_node.freq != prev_freq:
                prev_node = self._add_node(current_node.prev, prev_freq)

            prev_node.keys.add(key)
            self.key_node_map[key] = prev_node

        # Remove the current node if empty
        self._remove_node_if_empty(current_node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))  # Get any key from the max frequency node

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))  # Get any key from the min frequency node


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
