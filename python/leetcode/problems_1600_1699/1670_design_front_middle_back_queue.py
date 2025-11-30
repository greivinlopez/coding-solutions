# ------------------------------------
# 1670. Design Front Middle Back Queue
# ------------------------------------

# Problem: https://leetcode.com/problems/design-front-middle-back-queue
#
# Design a queue that supports push and pop operations in the front, middle, and
# back.
# 
# Implement the FrontMiddleBack class:
#         
#   * FrontMiddleBack() Initializes the queue.
#   * void pushFront(int val) Adds val to the front of the queue.
#   * void pushMiddle(int val) Adds val to the middle of the queue.
#   * void pushBack(int val) Adds val to the back of the queue.
#   * int popFront() Removes the front element of the queue and returns it. 
#     If the queue is empty, return -1.
#   * int popMiddle() Removes the middle element of the queue and returns it.
#     If the queue is empty, return -1.
#   * int popBack() Removes the back element of the queue and returns it.
#     If the queue is empty, return -1.
# 
# Notice that when there are two middle position choices, the operation is
# performed on the frontmost middle position choice. For example:
#         
#   * Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
#   * Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].
# 
# Example 1:
# 
# Input:
# ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle",
# "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
# [[], [1], [2], [3], [4], [], [], [], [], []]
# Output:
# [null, null, null, null, null, 1, 3, 4, 2, -1]
# 
# Explanation:
# FrontMiddleBackQueue q = new FrontMiddleBackQueue();
# q.pushFront(1);   // [1]
# q.pushBack(2);    // [1, 2]
# q.pushMiddle(3);  // [1, 3, 2]
# q.pushMiddle(4);  // [1, 4, 3, 2]
# q.popFront();     // return 1 -> [4, 3, 2]
# q.popMiddle();    // return 3 -> [4, 2]
# q.popMiddle();    // return 4 -> [2]
# q.popBack();      // return 2 -> []
# q.popFront();     // return -1 -> [] (The queue is empty)
# 
# 
# Constraints:
#   1 <= val <= 10⁹
#   At most 1000 calls will be made to pushFront, pushMiddle, pushBack,
#   popFront, popMiddle, and popBack.


# Solution: https://algo.monster/liteproblems/1670
# Credit: AlgoMonster
from collections import deque

class FrontMiddleBackQueue:
    """
    A queue data structure that supports operations at front, middle, and back positions.
    Uses two deques to maintain balance and enable O(1) middle operations.
  
    Invariant: len(q1) == len(q2) or len(q1) == len(q2) - 1
    - q1 contains the front half of elements
    - q2 contains the back half of elements
    """
  
    def __init__(self) -> None:
        """Initialize two deques to represent the front and back halves of the queue."""
        self.front_half = deque()  # Stores front portion of the queue
        self.back_half = deque()   # Stores back portion of the queue

    def pushFront(self, val: int) -> None:
        """
        Add an element to the front of the queue.
      
        Args:
            val: The value to be inserted at the front
        """
        self.front_half.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val: int) -> None:
        """
        Add an element to the middle of the queue.
      
        Args:
            val: The value to be inserted at the middle position
        """
        # Adding to the end of front_half puts it right at the middle
        self.front_half.append(val)
        self._rebalance()

    def pushBack(self, val: int) -> None:
        """
        Add an element to the back of the queue.
      
        Args:
            val: The value to be inserted at the back
        """
        self.back_half.append(val)
        self._rebalance()

    def popFront(self) -> int:
        """
        Remove and return the element from the front of the queue.
      
        Returns:
            The front element, or -1 if the queue is empty
        """
        # Check if queue is empty
        if not self.front_half and not self.back_half:
            return -1
      
        # Pop from front_half if it exists, otherwise from back_half
        if self.front_half:
            result = self.front_half.popleft()
        else:
            result = self.back_half.popleft()
      
        self._rebalance()
        return result

    def popMiddle(self) -> int:
        """
        Remove and return the middle element from the queue.
      
        Returns:
            The middle element, or -1 if the queue is empty
        """
        # Check if queue is empty
        if not self.front_half and not self.back_half:
            return -1
      
        # If equal lengths, middle is at the end of front_half
        # If back_half is longer by 1, middle is at the start of back_half
        if len(self.front_half) == len(self.back_half):
            result = self.front_half.pop()
        else:
            result = self.back_half.popleft()
      
        self._rebalance()
        return result

    def popBack(self) -> int:
        """
        Remove and return the element from the back of the queue.
      
        Returns:
            The back element, or -1 if the queue is empty
        """
        # Check if back_half is empty (queue could be empty or have only 1 element in front_half)
        if not self.back_half:
            return -1
      
        result = self.back_half.pop()
        self._rebalance()
        return result

    def _rebalance(self) -> None:
        """
        Maintain the invariant that front_half and back_half differ in size by at most 1.
        Ensures: len(front_half) == len(back_half) or len(front_half) == len(back_half) - 1
        """
        # If front_half has more elements, move one to back_half
        if len(self.front_half) > len(self.back_half):
            self.back_half.appendleft(self.front_half.pop())
      
        # If back_half has more than 1 extra element, move one to front_half
        if len(self.back_half) > len(self.front_half) + 1:
            self.front_half.append(self.back_half.popleft())


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
