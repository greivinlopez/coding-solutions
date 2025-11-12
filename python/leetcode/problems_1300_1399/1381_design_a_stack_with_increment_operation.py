# ---------------------------------------------
# 1381. Design a Stack With Increment Operation
# ---------------------------------------------

# Problem: https://leetcode.com/problems/design-a-stack-with-increment-operation
#
# Design a stack that supports increment operations on its elements.
# 
# Implement the CustomStack class:
#         
#   * CustomStack(int maxSize) Initializes the object with maxSize which is
#     the maximum number of elements in the stack.
#   * void push(int x) Adds x to the top of the stack if the stack has not
#     reached the maxSize.
#   * int pop() Pops and returns the top of the stack or -1 if the stack is empty.
#   * void inc(int k, int val) Increments the bottom k elements of the stack by 
#     val. If there are less than k elements in the stack, increment all the
#     elements in the stack.
# 
# Example 1:
# 
# Input
# ["CustomStack","push","push","pop","push","push","push","increment","increment",
# "pop","pop","pop","pop"]
# [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
# 
# Output
# [null,null,null,2,null,null,null,null,null,103,202,201,-1]
# 
# Explanation
# CustomStack stk = new CustomStack(3); // Stack is Empty []
# stk.push(1);                          // stack becomes [1]
# stk.push(2);                          // stack becomes [1, 2]
# stk.pop();                            // return 2 --> Return top of the stack 2,
# stack becomes [1]
# stk.push(2);                          // stack becomes [1, 2]
# stk.push(3);                          // stack becomes [1, 2, 3]
# stk.push(4);                          // stack still [1, 2, 3], Do not add
# another elements as size is 4
# stk.increment(5, 100);                // stack becomes [101, 102, 103]
# stk.increment(2, 100);                // stack becomes [201, 202, 103]
# stk.pop();                            // return 103 --> Return top of the stack
# 103, stack becomes [201, 202]
# stk.pop();                            // return 202 --> Return top of the stack
# 202, stack becomes [201]
# stk.pop();                            // return 201 --> Return top of the stack
# 201, stack becomes []
# stk.pop();                            // return -1 --> Stack is empty return -1.
# 
# 
# Constraints:
#         1 <= maxSize, x, k <= 1000
#         0 <= val <= 100
#         At most 1000 calls will be made to each method of increment, push and
#         pop each separately.


# Solution: 
# Credit: Navdeep Singh founder of NeetCode
class CustomStack:
    def __init__(self, maxSize: int):
        """
        Initialize the custom stack with a maximum size.
      
        Args:
            maxSize: Maximum number of elements the stack can hold
        """
        # Pre-allocate arrays for stack elements and increment values
        self.stack = [0] * maxSize
        # Lazy propagation array to store pending increments
        self.increment_values = [0] * maxSize
        # Current size of the stack (points to next empty position)
        self.current_size = 0

    def push(self, x: int) -> None:
        """
        Push an element onto the stack if not full.
      
        Args:
            x: Element to push onto the stack
        """
        # Only push if stack is not full
        if self.current_size < len(self.stack):
            self.stack[self.current_size] = x
            self.current_size += 1

    def pop(self) -> int:
        """
        Pop and return the top element from the stack.
      
        Returns:
            The top element value (with accumulated increments), or -1 if stack is empty
        """
        # Return -1 if stack is empty
        if self.current_size <= 0:
            return -1
      
        # Move pointer to the top element
        self.current_size -= 1
      
        # Calculate the actual value including any pending increments
        result = self.stack[self.current_size] + self.increment_values[self.current_size]
      
        # Propagate the increment value to the element below (if exists)
        if self.current_size > 0:
            self.increment_values[self.current_size - 1] += self.increment_values[self.current_size]
      
        # Clear the increment value for this position
        self.increment_values[self.current_size] = 0
      
        return result

    def increment(self, k: int, val: int) -> None:
        """
        Increment the bottom k elements of the stack by val.
        Uses lazy propagation for O(1) time complexity.
      
        Args:
            k: Number of bottom elements to increment
            val: Value to add to each element
        """
        # Find the index of the k-th element (or top if stack has fewer than k elements)
        target_index = min(k, self.current_size) - 1
      
        # Apply increment only if there are elements to increment
        if target_index >= 0:
            # Add to the increment array at the topmost affected position
            # This value will propagate down during pop operations
            self.increment_values[target_index] += val

def main():
    print("TO DO")

if __name__ == "__main__":
    main()
