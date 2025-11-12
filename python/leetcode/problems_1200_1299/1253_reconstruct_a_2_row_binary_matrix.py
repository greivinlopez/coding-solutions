# ---------------------------------------
# 1253. Reconstruct a 2-Row Binary Matrix
# ---------------------------------------

# Problem: https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix
#
# Given the following details of a matrix with n columns and 2 rows :
#         
#   * The matrix is a binary matrix, which means each element in the matrix
#     can be 0 or 1.
#   * The sum of elements of the 0-th(upper) row is given as upper.
#   * The sum of elements of the 1-st(lower) row is given as lower.
#   * The sum of elements in the i-th column(0-indexed) is colsum[i], where
#     colsum is given as an integer array with length n.
# 
# Your task is to reconstruct the matrix with upper, lower and colsum.
# 
# Return it as a 2-D integer array.
# 
# If there are more than one valid solution, any of them will be accepted.
# 
# If no valid solution exists, return an empty 2-D array.
# 
# Example 1:
# 
# Input: upper = 2, lower = 1, colsum = [1,1,1]
# Output: [[1,1,0],[0,0,1]]
# 
# Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
# 
# Example 2:
# 
# Input: upper = 2, lower = 3, colsum = [2,2,1,1]
# Output: []
# 
# Example 3:
# 
# Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
# Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
# 
# 
# Constraints:
#         1 <= colsum.length <= 10^5
#         0 <= upper, lower <= colsum.length
#         0 <= colsum[i] <= 2


# Solution: https://algo.monster/liteproblems/1253
# Credit: AlgoMonster
def reconstruct_matrix(upper, lower, colsum):
    n = len(colsum)
    # Initialize a 2x n matrix filled with zeros
    matrix = [[0] * n for _ in range(2)]
    
    # Track remaining sums for upper and lower rows
    upper_remaining = upper
    lower_remaining = lower
    
    # Process each column based on its sum requirement
    for col_idx, col_sum in enumerate(colsum):
        if col_sum == 2:
            # Column sum is 2: both rows must have 1 in this column
            matrix[0][col_idx] = 1
            matrix[1][col_idx] = 1
            upper_remaining -= 1
            lower_remaining -= 1
            
        elif col_sum == 1:
            # Column sum is 1: exactly one row should have 1 in this column
            # Greedily assign to the row with more remaining sum
            if upper_remaining > lower_remaining:
                matrix[0][col_idx] = 1
                upper_remaining -= 1
            else:
                matrix[1][col_idx] = 1
                lower_remaining -= 1
        
        # Check if we've exceeded the row sum constraints
        if upper_remaining < 0 or lower_remaining < 0:
            return []
    
    # Verify that we've used exactly the required sums for both rows
    if upper_remaining == 0 and lower_remaining == 0:
        return matrix
    else:
        return []
    # Time: O(n)
    # Space: O(1)


def main():
    result = reconstruct_matrix(upper = 2, lower = 1, colsum = [1,1,1])
    print(result) # [[1, 0, 1], [0, 1, 0]]

    result = reconstruct_matrix(upper = 2, lower = 3, colsum = [2,2,1,1])
    print(result) # []

    result = reconstruct_matrix(upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1])
    print(result) # [[1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]]

if __name__ == "__main__":
    main()
