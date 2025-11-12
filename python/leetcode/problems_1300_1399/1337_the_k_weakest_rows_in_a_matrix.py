# ------------------------------------
# 1337. The K Weakest Rows in a Matrix
# ------------------------------------

# Problem: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix
#
# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's
# (representing civilians). The soldiers are positioned in front of the civilians.
# That is, all the 1's will appear to the left of all the 0's in each row.
# 
# A row i is weaker than a row j if one of the following is true:
#         
#   * The number of soldiers in row i is less than the number of soldiers in row j.
#   * Both rows have the same number of soldiers and i < j.
# 
# Return the indices of the k weakest rows in the matrix ordered from weakest to
# strongest.
# 
# Example 1:
# 
# Input: mat =
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]],
# k = 3
# Output: [2,0,3]
# 
# Explanation:
# The number of soldiers in each row is:
# - Row 0: 2
# - Row 1: 4
# - Row 2: 1
# - Row 3: 2
# - Row 4: 5
# The rows ordered from weakest to strongest are [2,0,3,1,4].
# 
# Example 2:
# 
# Input: mat =
# [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,0],
#  [1,0,0,0]],
# k = 2
# Output: [0,2]
# 
# Explanation:
# The number of soldiers in each row is:
# - Row 0: 1
# - Row 1: 4
# - Row 2: 1
# - Row 3: 1
# The rows ordered from weakest to strongest are [0,2,3,1].
# 
# 
# Constraints:
#         m == mat.length
#         n == mat[i].length
#         2 <= n, m <= 100
#         1 <= k <= m
#         matrix[i][j] is either 0 or 1.

import bisect

# Solution: https://algo.monster/liteproblems/1337
# Credit: AlgoMonster
def k_weakest_rows_alt(mat, k):
    # Get dimensions of the matrix
    num_rows, num_cols = len(mat), len(mat[0])
    
    # Calculate soldier count for each row
    # Since rows have 1s (soldiers) followed by 0s (civilians),
    # reversing the row and finding rightmost position of 0 gives soldier count
    soldier_counts = [num_cols - bisect.bisect_right(row[::-1], 0) for row in mat]
    
    # Create list of row indices
    row_indices = list(range(num_rows))
    
    # Sort row indices based on soldier count (weakest to strongest)
    # In case of tie, smaller index comes first (naturally preserved by stable sort)
    row_indices.sort(key=lambda i: soldier_counts[i])
    
    # Return the first k weakest row indices
    return row_indices[:k]
    # Time: O(m * n + m * log(m))
    # Space: O(m)
    # m is the number of rows
    # n is the number of columns

# Solution: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/solutions/496647/python-3-one-line-beats-100-by-junaidman-oh0j
# Credit: Junaid Mansuri -> https://leetcode.com/u/junaidmansuri/
def k_weakest_rows(mat, k):
    import heapq
    return [ r[1] for r in heapq.nsmallest(k, [ [sum(g),i] for i,g in enumerate(mat) ]) ]
    # Time: O(r * c + r * log(k)) or O(r * c + r) as log(k) is constant
    # Space: O(r)
    # r = be the number of rows in the matrix mat
    # c = the number of columns in the matrix mat


def main():
    mat = [[1,1,0,0,0],
           [1,1,1,1,0],
           [1,0,0,0,0],
           [1,1,0,0,0],
           [1,1,1,1,1]]
    result = k_weakest_rows(mat, 3)
    print(result) # [2, 0, 3]

    mat = [[1,0,0,0],
           [1,1,1,1],
           [1,0,0,0],
           [1,0,0,0]]
    result = k_weakest_rows(mat, 2)
    print(result) # [0, 2]

if __name__ == "__main__":
    main()
