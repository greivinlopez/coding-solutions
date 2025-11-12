# ------------------------------------------------
# 668. Kth Smallest Number in Multiplication Table
# ------------------------------------------------

# Problem: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table
#
# Nearly everyone has used the Multiplication Table. The multiplication table of
# size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).
# 
# Given three integers m, n, and k, return the kth smallest element in the m x n
# multiplication table.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/05/02/multtable1-grid.jpg
# 
# Input: m = 3, n = 3, k = 5
# Output: 3
# 
# Explanation: The 5th smallest number is 3.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/05/02/multtable2-grid.jpg
# 
# Input: m = 2, n = 3, k = 6
# Output: 6
# 
# Explanation: The 6th smallest number is 6.
# 
# 
# Constraints:
#         1 <= m, n <= 3 * 10⁴
#         1 <= k <= m * n


# Solution: https://algo.monster/liteproblems/668
# Credit: AlgoMonster
def find_kth_number(m, n, k):
    # Binary search range: minimum value is 1, maximum value is m * n
    left, right = 1, m * n
    
    # Binary search to find the kth smallest value
    while left < right:
        # Calculate middle value of current search range
        mid = (left + right) // 2
        
        # Count how many numbers in the multiplication table are <= mid
        count = 0
        for row in range(1, m + 1):
            # For each row i, elements are: i, 2i, 3i, ..., n*i
            # Number of elements <= mid in row i is min(mid // i, n)
            count += min(mid // row, n)
        
        # If count >= k, the kth number is at most mid
        if count >= k:
            right = mid
        # If count < k, the kth number is greater than mid
        else:
            left = mid + 1
    
    # When left == right, we've found the kth smallest number
    return left
    # Time: O(m * log(m * n))
    # Space: O(1)


def main():
    result = find_kth_number(m = 3, n = 3, k = 5)
    print(result) # 3

    result = find_kth_number(m = 2, n = 3, k = 6)
    print(result) # 6

if __name__ == "__main__":
    main()
