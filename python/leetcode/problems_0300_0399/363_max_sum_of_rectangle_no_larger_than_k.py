# ------------------------------------------
# 363. Max Sum of Rectangle No Larger Than K
# ------------------------------------------

# Problem: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k
#
# Given an m x n matrix matrix and an integer k, return the max sum of a rectangle
# in the matrix such that its sum is no larger than k.
# 
# It is guaranteed that there will be a rectangle with a sum no larger than k.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/03/18/sum-grid.jpg
# 
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# 
# Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2
# is the max number no larger than k (k = 2).
# 
# Example 2:
# 
# Input: matrix = [[2,2,-1]], k = 3
# Output: 3
# 
# 
# Constraints:
#         m == matrix.length
#         n == matrix[i].length
#         1 <= m, n <= 100
#         -100 <= matrix[i][j] <= 100
#         -10⁵ <= k <= 10⁵
# 
# Follow up: What if the number of rows is much larger than the number of columns?

import bisect

# Solution: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/solutions/1314119/python3-bisect-prefix-row-sum-sol-for-reference
# Credit: Venkata Ratnam Vadhri -> https://leetcode.com/u/vadhri_venkat/
def csum_less_than_k(nums, k):
    ans = float('-inf')
    slist = [0]

    for x in range(1, len(nums)):
        nums[x] += nums[x-1]

    for p in nums:
        idx = bisect.bisect_left(slist, p-k)
        if idx < len(slist):
            ans = max(ans, p-slist[idx])

        bisect.insort(slist, p)

    return ans

def max_sum_submatrix(matrix, k):
    R = len(matrix)
    C = len(matrix[0])
    ans = float('-inf')

    for r in range(R):
        for c in range(1, C):
            matrix[r][c] += matrix[r][c-1]

    for left_edge in range(C):
        for right_edge in range(left_edge, C):
            ledge = lambda i: matrix[i][left_edge-1] if left_edge > 0 else 0
            one_d_array = [matrix[i][right_edge]-ledge(i) for i in range(R)]
            ans = max(ans, csum_less_than_k(one_d_array, k))

    return ans
    # Time: O(c² * r² * log(r))
    # Space: O(c + r)
    # r = number of rows
    # c = number of columns


def main():
    result = max_sum_submatrix(matrix = [[1,0,1],[0,-2,3]], k = 2)
    print(result) # 2

    result = max_sum_submatrix(matrix = [[2,2,-1]], k = 3)
    print(result) # 3

if __name__ == "__main__":
    main()
