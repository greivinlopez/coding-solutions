# --------------------
# 279. Perfect Squares
# --------------------

# Problem: https://leetcode.com/problems/perfect-squares
#
# Given an integer n, return the least number of perfect square numbers that sum
# to n.
# 
# A perfect square is an integer that is the square of an integer; in other words,
# it is the product of some integer with itself. For example, 1, 4, 9, and 16 are
# perfect squares while 3 and 11 are not.
# 
# Example 1:
# 
# Input: n = 12
# Output: 3
# 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# Input: n = 13
# Output: 2
# 
# Explanation: 13 = 4 + 9.
# 
# 
# Constraints:
#         1 <= n <= 10⁴


# Solution: https://youtu.be/HLZLwjzIVGo
# Credit: Navdeep Singh founder of NeetCode
def num_squares(n):
    dp = [n] * (n + 1)
    dp[0] = 0

    for target in range(1, n + 1):
        for s in range(1, target + 1):
            square = s * s
            if target - square < 0:
                break
            dp[target] = min(dp[target], 1 + dp[target - square])

    return dp[n]
    # Time: O(n * √n)
    # Space: O(n)


def main():
    result = num_squares(12)
    print(result) # 3

    result = num_squares(13)
    print(result) # 2

if __name__ == "__main__":
    main()
