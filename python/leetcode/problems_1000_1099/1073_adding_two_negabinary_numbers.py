# -----------------------------------
# 1073. Adding Two Negabinary Numbers
# -----------------------------------

# Problem: https://leetcode.com/problems/adding-two-negabinary-numbers
#
# Given two numbers arr1 and arr2 in base -2, return the result of adding them
# together.
# 
# Each number is given in array format:  as an array of 0s and 1s, from most
# significant bit to least significant bit.  For example, arr = [1,1,0,1]
# represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array,
# format is also guaranteed to have no leading zeros: either arr == [0] or 
# arr[0] == 1.
# 
# Return the result of adding arr1 and arr2 in the same format: as an array of 0s
# and 1s with no leading zeros.
# 
# Example 1:
# 
# Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
# Output: [1,0,0,0,0]
# 
# Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.
# 
# Example 2:
# 
# Input: arr1 = [0], arr2 = [0]
# Output: [0]
# 
# Example 3:
# 
# Input: arr1 = [0], arr2 = [1]
# Output: [1]
# 
# 
# Constraints:
#         1 <= arr1.length, arr2.length <= 1000
#         arr1[i] and arr2[i] are 0 or 1
#         arr1 and arr2 have no leading zeros


# Solution: https://algo.monster/liteproblems/1073
# Credit: AlgoMonster
def add_negabinary(arr1, arr2):
    # Initialize pointers to the least significant bits (rightmost elements)
    index1 = len(arr1) - 1
    index2 = len(arr2) - 1
    
    # Initialize carry value for addition
    carry = 0
    
    # Result list to store the sum digits
    result = []
    
    # Process digits from right to left, including any remaining carry
    while index1 >= 0 or index2 >= 0 or carry != 0:
        # Get current digit from arr1, or 0 if we've exhausted arr1
        digit1 = 0 if index1 < 0 else arr1[index1]
        
        # Get current digit from arr2, or 0 if we've exhausted arr2
        digit2 = 0 if index2 < 0 else arr2[index2]
        
        # Calculate sum of current position including carry
        current_sum = digit1 + digit2 + carry
        
        # Reset carry for next iteration
        carry = 0
        
        # Handle negabinary addition rules
        if current_sum >= 2:
            # If sum is 2 or more, subtract 2 and set negative carry
            current_sum -= 2
            carry = -1
        elif current_sum == -1:
            # If sum is -1, set digit to 1 and positive carry
            current_sum = 1
            carry = 1
        
        # Append the computed digit to result
        result.append(current_sum)
        
        # Move pointers to the next more significant digits
        index1 -= 1
        index2 -= 1
    
    # Remove leading zeros from the result (except if result is just [0])
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    # Reverse the result since we built it from least to most significant
    return result[::-1]
    # Time: O(max(n, m))
    # Space: O(max(n, m))


def main():
    result = add_negabinary(arr1 = [1,1,1,1,1], arr2 = [1,0,1])
    print(result) # [1,0,0,0,0]

    result = add_negabinary(arr1 = [0], arr2 = [0])
    print(result) # [0]

    result = add_negabinary(arr1 = [0], arr2 = [1])
    print(result) # [1]

if __name__ == "__main__":
    main()
