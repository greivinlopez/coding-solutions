# -------------------------
# 1172. Dinner Plate Stacks
# -------------------------

# Problem: https://leetcode.com/problems/dinner-plate-stacks
#
# You have an infinite number of stacks arranged in a row and numbered (left to
# right) from 0, each of the stacks has the same maximum capacity.
# 
# Implement the DinnerPlates class:
#         
#   * DinnerPlates(int capacity) Initializes the object with the maximum
#     capacity of the stacks capacity.
#   * void push(int val) Pushes the given integer val into the leftmost stack
#     with a size less than capacity.
#   * int pop() Returns the value at the top of the rightmost non-empty stack
#     and removes it from that stack, and returns -1 if all the stacks are empty.
#   * int popAtStack(int index) Returns the value at the top of the stack with
#     the given index index and removes it from that stack or returns -1 if the stack
#     with that given index is empty.
# 
# Example 1:
# 
# Input
# ["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push",
# "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"]
# [[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]
# Output
# [null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]
# 
# Explanation:
# DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
# D.push(1);
# D.push(2);
# D.push(3);
# D.push(4);
# D.push(5);         // The stacks are now:  2  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 2.  The stacks are now:     4
#                                                        1  3  5
#                                                        ﹈ ﹈ ﹈
# D.push(20);        // The stacks are now: 20  4
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.push(21);        // The stacks are now: 20  4 21
#                                            1  3  5
#                                            ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈
# D.popAtStack(2);   // Returns 21.  The stacks are now:     4
#                                                         1  3  5
#                                                         ﹈ ﹈ ﹈
# D.pop()            // Returns 5.  The stacks are now:      4
#                                                         1  3
#                                                         ﹈ ﹈
# D.pop()            // Returns 4.  The stacks are now:   1  3
#                                                         ﹈ ﹈
# D.pop()            // Returns 3.  The stacks are now:   1
#                                                         ﹈
# D.pop()            // Returns 1.  There are no stacks.
# D.pop()            // Returns -1.  There are still no stacks.
# 
# 
# Constraints:
#         1 <= capacity <= 2 * 10⁴
#         1 <= val <= 2 * 10⁴
#         0 <= index <= 10⁵
#         At most 2 * 10⁵ calls will be made to push, pop, and popAtStack.

from sortedcontainers import SortedSet

# Solution: https://algo.monster/liteproblems/1172
# Credit: AlgoMonster
class DinnerPlates:
    def __init__(self, capacity: int):
        """
        Initialize the DinnerPlates data structure.
      
        Args:
            capacity: Maximum number of values each stack can hold
        """
        self.capacity = capacity
        self.stacks = []  # List of stacks to store plates
        self.not_full = SortedSet()  # Sorted set of indices of non-full stacks
  
    def push(self, val: int) -> None:
        """
        Push a value onto the leftmost stack with available capacity.
      
        Args:
            val: The value to push onto a stack
        """
        if not self.not_full:
            # No non-full stacks exist, create a new stack
            self.stacks.append([val])
          
            # If the new stack still has room, add its index to not_full set
            if self.capacity > 1:
                self.not_full.add(len(self.stacks) - 1)
        else:
            # Push to the leftmost non-full stack
            index = self.not_full[0]
            self.stacks[index].append(val)
          
            # If stack is now full, remove it from not_full set
            if len(self.stacks[index]) == self.capacity:
                self.not_full.discard(index)
  
    def pop(self) -> int:
        """
        Pop a value from the rightmost non-empty stack.
      
        Returns:
            The popped value, or -1 if all stacks are empty
        """
        return self.popAtStack(len(self.stacks) - 1)
  
    def popAtStack(self, index: int) -> int:
        """
        Pop a value from a specific stack at the given index.
      
        Args:
            index: The index of the stack to pop from
          
        Returns:
            The popped value, or -1 if the operation is invalid
        """
        # Check if index is valid and stack at index is not empty
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1
      
        # Pop the value from the specified stack
        val = self.stacks[index].pop()
      
        if index == len(self.stacks) - 1 and not self.stacks[-1]:
            # If we popped from the last stack and it's now empty,
            # remove all trailing empty stacks
            while self.stacks and not self.stacks[-1]:
                self.not_full.discard(len(self.stacks) - 1)
                self.stacks.pop()
        else:
            # Stack at index now has space, add to not_full set
            self.not_full.add(index)
      
        return val


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
