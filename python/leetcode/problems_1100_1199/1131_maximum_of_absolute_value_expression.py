# ------------------------------------------
# 1131. Maximum of Absolute Value Expression
# ------------------------------------------

# Problem: https://leetcode.com/problems/maximum-of-absolute-value-expression
#
# Given two arrays of integers with equal lengths, return the maximum value of:
# |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
# where the maximum is taken over all 0 <= i, j < arr1.length.
# 
# Example 1:
# 
# Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
# Output: 13
# 
# Example 2:
# 
# Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
# Output: 20
# 
# 
# Constraints:
#         2 <= arr1.length == arr2.length <= 40000
#         -10⁶ <= arr1[i], arr2[i] <= 10⁶

# This will only works in Python 3.10+
from itertools import pairwise

# Solution: https://algo.monster/liteproblems/1131
# Credit: AlgoMonster
def max_abs_val_expr(arr1, arr2):
    # Direction coefficients for handling absolute value cases
    # Each pair represents coefficients for arr1[i] and arr2[i]
    # The 4 cases handle all combinations when removing absolute values
    direction_coefficients = (1, -1, -1, 1, 1)
    
    max_result = float('-inf')
    
    # Iterate through pairs of coefficients using pairwise
    # This gives us (1, -1), (-1, -1), (-1, 1), (1, 1)
    for coeff_arr1, coeff_arr2 in pairwise(direction_coefficients):
        max_value = float('-inf')
        min_value = float('inf')
        
        # Process each index and corresponding values from both arrays
        for index, (value1, value2) in enumerate(zip(arr1, arr2)):
            # Calculate the expression for current coefficients
            current_expression = coeff_arr1 * value1 + coeff_arr2 * value2 + index
            
            # Track maximum and minimum values for this coefficient combination
            max_value = max(max_value, current_expression)
            min_value = min(min_value, current_expression)
            
            # Update the global maximum with the difference
            # The difference represents the maximum absolute value expression
            max_result = max(max_result, max_value - min_value)
    
    return max_result
    # Time: O(n)
    # Space: O(1)


def main():
    result = max_abs_val_expr(arr1 = [1,2,3,4], arr2 = [-1,4,5,6])
    print(result) # 13

    result = max_abs_val_expr(arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4])
    print(result) # 20

if __name__ == "__main__":
    main()
