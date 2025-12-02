# -------------------------------------------
# 1738. Find Kth Largest XOR Coordinate Value
# -------------------------------------------

# Problem: https://leetcode.com/problems/find-kth-largest-xor-coordinate-value
#
# You are given a 2D matrix of size m x n, consisting of non-negative integers.
# You are also given an integer k.
# 
# The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j]
# where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).
# 
# Find the kᵗʰ largest value (1-indexed) of all the coordinates of matrix.
# 
# Example 1:
# 
# Input: matrix = [[5,2],[1,6]], k = 1
# Output: 7
# 
# Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest
# value.
# 
# Example 2:
# 
# Input: matrix = [[5,2],[1,6]], k = 2
# Output: 5
# 
# Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest
# value.
# 
# Example 3:
# 
# Input: matrix = [[5,2],[1,6]], k = 3
# Output: 4
# 
# Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd
# largest value.
# 
# 
# Constraints:
#         m == matrix.length
#         n == matrix[i].length
#         1 <= m, n <= 1000
#         0 <= matrix[i][j] <= 10⁶
#         1 <= k <= m * n


# Solution: https://algo.monster/liteproblems/1738
# Credit: AlgoMonster
def kth_largest_value(matrix, k):
    from heapq import nlargest

    # Get dimensions of the matrix
    rows, cols = len(matrix), len(matrix[0])
    
    # Create a 2D prefix XOR array with padding for easier calculation
    # prefix_xor[i][j] represents XOR of all elements in rectangle from (0,0) to (i-1,j-1)
    prefix_xor = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    # Store all XOR values to find kth largest
    all_xor_values = []
    
    # Build prefix XOR array
    for i in range(rows):
        for j in range(cols):
            # Calculate XOR value for current position using inclusion-exclusion principle
            # Current = left XOR + top XOR - diagonal XOR + current element
            # Since XOR is its own inverse: a ^ a = 0, we use XOR instead of addition/subtraction
            prefix_xor[i + 1][j + 1] = (prefix_xor[i + 1][j] ^ 
                                        prefix_xor[i][j + 1] ^ 
                                        prefix_xor[i][j] ^ 
                                        matrix[i][j])
            
            # Add current XOR value to list
            all_xor_values.append(prefix_xor[i + 1][j + 1])
    
    # Find k largest elements and return the kth one (last element in the k largest)
    return nlargest(k, all_xor_values)[-1]
    # Time: O(m * n)
    # Space: O(m * n)


def main():
    result = kth_largest_value(matrix = [[5,2],[1,6]], k = 1)
    print(result) # 7

    result = kth_largest_value(matrix = [[5,2],[1,6]], k = 2)
    print(result) # 5

    result = kth_largest_value(matrix = [[5,2],[1,6]], k = 3)
    print(result) # 4

if __name__ == "__main__":
    main()
