# --------------------------------------------------------------
# 1866. Number of Ways to Rearrange Sticks With K Sticks Visible
# --------------------------------------------------------------

# Problem: https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible
#
# There are n uniquely-sized sticks whose lengths are integers from 1 to n. You
# want to arrange the sticks such that exactly k sticks are visible from the left.
# A stick is visible from the left if there are no longer sticks to the left of it.
# 
#   For example, if the sticks are arranged [1,3,2,5,4], then the sticks
#   with lengths 1, 3, and 5 are visible from the left.
# 
# Given n and k, return the number of such arrangements. Since the answer may be
# large, return it modulo 109 + 7.
# 
# Example 1:
# 
# Input: n = 3, k = 2
# Output: 3
# 
# Explanation: [1,3,2], [2,3,1], and [2,1,3] are the only arrangements such that
# exactly 2 sticks are visible.
# The visible sticks are underlined.
# 
# Example 2:
# 
# Input: n = 5, k = 5
# Output: 1
# 
# Explanation: [1,2,3,4,5] is the only arrangement such that all 5 sticks are
# visible.
# The visible sticks are underlined.
# 
# Example 3:
# 
# Input: n = 20, k = 11
# Output: 647427950
# 
# Explanation: There are 647427950 (mod 109 + 7) ways to rearrange the sticks such
# that exactly 11 sticks are visible.
# 
# 
# Constraints:
#         1 <= n <= 1000
#         1 <= k <= n


# Solution: https://youtu.be/O761YBjGxGA
# Credit: Navdeep Singh founder of NeetCode
def rearrange_sticks(n, k):
    dp = {}

    def dfs(N, K):
        if N == K:
            return 1
        if N == 0 or K == 0:
            return 0
        if (N, K) in dp:
            return dp[(N, K)]

        dp[(N, K)] = dfs(N - 1, K - 1) + (N - 1) * dfs(N - 1, K)
        return dp[(N, K)]

    return dfs(n, k) % (10**9 + 7)
    # Time: O(n * k)
    # Space: O(n * k)


def main():
    result = rearrange_sticks(n = 3, k = 2)
    print(result) # 3

    result = rearrange_sticks(n = 5, k = 5)
    print(result) # 1

    result = rearrange_sticks(n = 20, k = 11)
    print(result) # 647427950

if __name__ == "__main__":
    main()
