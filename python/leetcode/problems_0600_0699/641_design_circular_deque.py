# --------------------------
# 641. Design Circular Deque
# --------------------------

# Problem: https://leetcode.com/problems/design-circular-deque
#
# Design your implementation of the circular double-ended queue (deque).
# 
# Implement the MyCircularDeque class:
#         
#   * MyCircularDeque(int k) Initializes the deque with a maximum size of k.
#   * boolean insertFront() Adds an item at the front of Deque. Returns true
#     if the operation is successful, or false otherwise.
#   * boolean insertLast() Adds an item at the rear of Deque. Returns true if
#     the operation is successful, or false otherwise.
#   * boolean deleteFront() Deletes an item from the front of Deque. Returns
#     true if the operation is successful, or false otherwise.
#   * boolean deleteLast() Deletes an item from the rear of Deque. Returns
#     true if the operation is successful, or false otherwise.
#   * int getFront() Returns the front item from the Deque. Returns -1 if the
#     deque is empty.
#   * int getRear() Returns the last item from Deque. Returns -1 if the deque
#     is empty.
#   * boolean isEmpty() Returns true if the deque is empty, or false otherwise.
#   * boolean isFull() Returns true if the deque is full, or false otherwise.
# 
# Example 1:
# 
# Input
# ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront",
# "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 2, true, true, true, 4]
# 
# Explanation
# MyCircularDeque myCircularDeque = new MyCircularDeque(3);
# myCircularDeque.insertLast(1);  // return True
# myCircularDeque.insertLast(2);  // return True
# myCircularDeque.insertFront(3); // return True
# myCircularDeque.insertFront(4); // return False, the queue is full.
# myCircularDeque.getRear();      // return 2
# myCircularDeque.isFull();       // return True
# myCircularDeque.deleteLast();   // return True
# myCircularDeque.insertFront(4); // return True
# myCircularDeque.getFront();     // return 4
# 
# 
# Constraints:
#   1 <= k <= 1000
#   0 <= value <= 1000
#   At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast,
#   getFront, getRear, isEmpty, isFull.


# Solution: https://algo.monster/liteproblems/641
# Credit: AlgoMonster
class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize the circular deque with a fixed capacity.
      
        Args:
            k: Maximum capacity of the deque
        """
        # Pre-allocate array with fixed size for O(1) operations
        self.buffer = [0] * k
        # Index pointing to the front element
        self.front_index = 0
        # Current number of elements in the deque
        self.current_size = 0
        # Maximum capacity of the deque
        self.max_capacity = k

    def insertFront(self, value: int) -> bool:
        """
        Insert an element at the front of the deque.
      
        Args:
            value: The value to insert
          
        Returns:
            True if insertion was successful, False if deque is full
        """
        # Check if deque has space for new element
        if self.isFull():
            return False
      
        # Move front pointer backward circularly only if deque is not empty
        # If empty, we insert at current front_index position
        if not self.isEmpty():
            self.front_index = (self.front_index - 1 + self.max_capacity) % self.max_capacity
      
        # Place the new value at the front position
        self.buffer[self.front_index] = value
        # Increment the size counter
        self.current_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Insert an element at the rear of the deque.
      
        Args:
            value: The value to insert
          
        Returns:
            True if insertion was successful, False if deque is full
        """
        # Check if deque has space for new element
        if self.isFull():
            return False
      
        # Calculate the rear position using front_index and size
        rear_index = (self.front_index + self.current_size) % self.max_capacity
        # Place the new value at the rear position
        self.buffer[rear_index] = value
        # Increment the size counter
        self.current_size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Remove the front element from the deque.
      
        Returns:
            True if deletion was successful, False if deque is empty
        """
        # Cannot delete from empty deque
        if self.isEmpty():
            return False
      
        # Move front pointer forward circularly
        self.front_index = (self.front_index + 1) % self.max_capacity
        # Decrement the size counter
        self.current_size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Remove the rear element from the deque.
      
        Returns:
            True if deletion was successful, False if deque is empty
        """
        # Cannot delete from empty deque
        if self.isEmpty():
            return False
      
        # Simply decrement size; the rear position is calculated dynamically
        self.current_size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the value of the front element without removing it.
      
        Returns:
            The front element value, or -1 if deque is empty
        """
        # Return -1 for empty deque as per problem specification
        if self.isEmpty():
            return -1
      
        # Return the element at front_index
        return self.buffer[self.front_index]

    def getRear(self) -> int:
        """
        Get the value of the rear element without removing it.
      
        Returns:
            The rear element value, or -1 if deque is empty
        """
        # Return -1 for empty deque as per problem specification
        if self.isEmpty():
            return -1
      
        # Calculate rear position: front + size - 1 (wrapped around)
        rear_index = (self.front_index + self.current_size - 1) % self.max_capacity
        return self.buffer[rear_index]

    def isEmpty(self) -> bool:
        """
        Check if the deque is empty.
      
        Returns:
            True if deque contains no elements, False otherwise
        """
        return self.current_size == 0

    def isFull(self) -> bool:
        """
        Check if the deque is at maximum capacity.
      
        Returns:
            True if deque cannot accept more elements, False otherwise
        """
        return self.current_size == self.max_capacity


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
