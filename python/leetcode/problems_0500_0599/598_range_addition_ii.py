# ----------------------
# 598. Range Addition II
# ----------------------

# Problem: https://leetcode.com/problems/range-addition-ii
#
# You are given an m x n matrix M initialized with all 0's and an array of
# operations ops, where ops[i] = [aᵢ, bᵢ] means M[x][y] should be incremented by
# one for all 0 <= x < aᵢ and 0 <= y < bᵢ.
# 
# Count and return the number of maximum integers in the matrix after performing
# all the operations.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/10/02/ex1.jpg
# 
# Input: m = 3, n = 3, ops = [[2,2],[3,3]]
# Output: 4
# 
# Explanation: The maximum integer in M is 2, and there are four of it in M. So
# return 4.
# 
# Example 2:
# 
# Input: m = 3, n = 3, ops =
# [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
# Output: 4
# 
# Example 3:
# 
# Input: m = 3, n = 3, ops = []
# Output: 9
# 
# 
# Constraints:
#         1 <= m, n <= 4 * 10⁴
#         0 <= ops.length <= 10⁴
#         ops[i].length == 2
#         1 <= aᵢ <= m
#         1 <= bᵢ <= n


# Solution: https://algo.monster/liteproblems/598
# Credit: AlgoMonster
def max_count(m, n, ops):
    # The maximum value will always be in the intersection of all operation ranges
    # This intersection is defined by the minimum row and column limits
    min_row_limit = m
    min_col_limit = n
    
    # Find the smallest operation range that covers all operations
    for row_limit, col_limit in ops:
        min_row_limit = min(min_row_limit, row_limit)
        min_col_limit = min(min_col_limit, col_limit)
    
    # The area of the intersection rectangle contains all maximum values
    return min_row_limit * min_col_limit
    # Time: O(k)
    # Space: O(1)


def main():
    result = max_count(m = 3, n = 3, ops = [[2,2],[3,3]])
    print(result) # 4

    result = max_count(m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]])
    print(result) # 4

    result = max_count(m = 3, n = 3, ops = [])
    print(result) # 9

if __name__ == "__main__":
    main()
