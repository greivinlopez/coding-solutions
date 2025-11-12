# ----------------------------------------------------------------------
# 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons
# ----------------------------------------------------------------------

# Problem: https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons
#
# You are given three integers n, m and k. Consider the following algorithm to
# find the maximum element of an array of positive integers:
# 
# https://assets.leetcode.com/uploads/2020/04/02/e.png
# 
# You should build the array arr which has the following properties:
#         
#   * arr has exactly n integers.
#   * 1 <= arr[i] <= m where (0 <= i < n).
#   * After applying the mentioned algorithm to arr, the value search_cost is
#     equal to k.
# 
# Return the number of ways to build the array arr under the mentioned conditions.
# 
# As the answer may grow large, the answer must be computed modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: n = 2, m = 3, k = 1
# Output: 6
# 
# Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3,
# 3]
# 
# Example 2:
# 
# Input: n = 5, m = 2, k = 3
# Output: 0
# 
# Explanation: There are no possible arrays that satisfy the mentioned conditions.
# 
# Example 3:
# 
# Input: n = 9, m = 1, k = 1
# Output: 1
# 
# Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
# 
# 
# Constraints:
#         1 <= n <= 50
#         1 <= m <= 100
#         0 <= k <= n

from functools import cache

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def num_of_arrays(n, m, k):
    @cache
    
    def dp(i, max_so_far, remain):
        if i == n:
            if remain == 0:
                return 1
            return 0
        
        ans = (max_so_far * dp(i+1, max_so_far, remain)) % MOD
        
        for num in range(max_so_far + 1, m + 1):
            ans = ( ans + dp(i+1, num, remain - 1)) % MOD
        
        return ans
    
    MOD = 10 ** 9 + 7
    
    return dp(0, 0 , k)
    # Time: O(n * m² * k)
    # Space: O(n * m * k)


def main():
    result = num_of_arrays(n = 2, m = 3, k = 1)
    print(result) # 6

    result = num_of_arrays(n = 5, m = 2, k = 3)
    print(result) # 0

    result = num_of_arrays(n = 9, m = 1, k = 1)
    print(result) # 1

if __name__ == "__main__":
    main()
