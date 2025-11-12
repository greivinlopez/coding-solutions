# ---------------------
# 1006. Clumsy Factorial
# ---------------------

# Problem: https://leetcode.com/problems/clumsy-factorial
#
# The factorial of a positive integer n is the product of all positive integers
# less than or equal to n.
#         
#   * For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
# 
# We make a clumsy factorial using the integers in decreasing order by swapping
# out the multiply operations for a fixed rotation of operations with multiply
# '*', divide '/', add '+', and subtract '-' in this order.
#         
#   * For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
# 
# However, these operations are still applied using the usual order of operations
# of arithmetic. We do all multiplication and division steps before any addition
# or subtraction steps, and multiplication and division steps are processed left
# to right.
# 
# Additionally, the division that we use is floor division such that 10 * 9 / 8 =
# 90 / 8 = 11.
# 
# Given an integer n, return the clumsy factorial of n.
# 
# Example 1:
# 
# Input: n = 4
# Output: 7
# 
# Explanation: 7 = 4 * 3 / 2 + 1
# 
# Example 2:
# 
# Input: n = 10
# Output: 12
# 
# Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
# 
# 
# Constraints:
#         1 <= n <= 10⁴


# Solution: https://algo.monster/liteproblems/1006
# Credit: AlgoMonster
def clumsy(n):
    # Initialize operation index (0: multiply, 1: divide, 2: add, 3: subtract)
    operation_index = 0
    
    # Stack to store intermediate results
    # Start with n as the first operand
    stack = [n]
    
    # Process remaining numbers from n-1 down to 1
    for current_num in range(n - 1, 0, -1):
        if operation_index == 0:
            # Multiply: pop last value, multiply with current number, push result
            stack.append(stack.pop() * current_num)
        elif operation_index == 1:
            # Divide: pop last value, perform integer division, push result
            # Using int() for truncation towards zero (Python's // floors for negative)
            stack.append(int(stack.pop() / current_num))
        elif operation_index == 2:
            # Add: push positive number to stack
            stack.append(current_num)
        else:  # operation_index == 3
            # Subtract: push negative number to stack (will be added in final sum)
            stack.append(-current_num)
        
        # Cycle through operations (0, 1, 2, 3, 0, 1, ...)
        operation_index = (operation_index + 1) % 4
    
    # Sum all values in the stack to get the final result
    return sum(stack)
    # Time: O(n)
    # Space: O(n)


def main():
    result = clumsy(n = 4)
    print(result) # 7

    result = clumsy(n = 10)
    print(result) # 12

if __name__ == "__main__":
    main()
