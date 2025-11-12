# -----------------------------
# 556. Next Greater Element III
# -----------------------------

# Problem: https://leetcode.com/problems/next-greater-element-iii
#
# Given a positive integer n, find the smallest integer which has exactly the same
# digits existing in the integer n and is greater in value than n. If no such
# positive integer exists, return -1.
# 
# Note that the returned integer should fit in 32-bit integer, if there is a valid
# answer but it does not fit in 32-bit integer, return -1.
# 
# Example 1:
# 
# Input: n = 12
# Output: 21
# 
# Example 2:
# 
# Input: n = 21
# Output: -1
# 
# 
# Constraints:
#         1 <= n <= 2³¹ - 1


# Solution: https://algo.monster/liteproblems/556
# Credit: AlgoMonster
def next_greater_element(n):
    # Convert integer to list of digit characters for manipulation
    digits = list(str(n))
    length = len(digits)
    
    # Step 1: Find the rightmost digit that is smaller than its successor
    # This is the pivot point where we need to make a change
    pivot_index = length - 2
    while pivot_index >= 0 and digits[pivot_index] >= digits[pivot_index + 1]:
        pivot_index -= 1
    
    # If no such digit exists, the number is already the largest permutation
    if pivot_index < 0:
        return -1
    
    # Step 2: Find the smallest digit to the right of pivot that is larger than pivot
    # This digit will be swapped with the pivot
    swap_index = length - 1
    while digits[pivot_index] >= digits[swap_index]:
        swap_index -= 1
    
    # Step 3: Swap the pivot with the found digit
    digits[pivot_index], digits[swap_index] = digits[swap_index], digits[pivot_index]
    
    # Step 4: Reverse all digits after the pivot position to get the smallest permutation
    # This ensures we get the next greater number, not just any greater number
    digits[pivot_index + 1:] = digits[pivot_index + 1:][::-1]
    
    # Convert the digit list back to an integer
    result = int(''.join(digits))
    
    # Check if the result fits in a 32-bit signed integer
    # Return -1 if it exceeds the maximum value (2^31 - 1)
    return -1 if result > 2**31 - 1 else result
    # Time: O(d)
    # Space: O(d)
    # d = the number of digits in the input number


def main():
    result = next_greater_element(12)
    print(result) # 21

    result = next_greater_element(21)
    print(result) # -1

if __name__ == "__main__":
    main()
