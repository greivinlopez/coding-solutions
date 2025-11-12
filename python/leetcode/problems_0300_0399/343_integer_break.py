# ------------------
# 343. Integer Break
# ------------------

# Problem: https://leetcode.com/problems/integer-break
#
# Given an integer n, break it into the sum of k positive integers, where k >= 2,
# and maximize the product of those integers.
# 
# Return the maximum product you can get.
# 
# Example 1:
# 
# Input: n = 2
# Output: 1
# 
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# 
# Example 2:
# 
# Input: n = 10
# Output: 36
# 
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# 
# 
# Constraints:
#         2 <= n <= 58


# Solution: https://youtu.be/in6QbUPMJ3I
# Credit: Navdeep Singh founder of NeetCode
def integer_break(n):
    dp = {1: 1}

    def dfs(num):
        if num in dp:
            return dp[num]

        res = 0 if num == n else num
        for i in range(1, num):
            val = dfs(i) * dfs(num - i)
            res = max(res, val)

        dp[num] = res
        return res

    return dfs(n)
    # Time: O(n ^ 2)
    # Space: O(n)


def integer_break_dp(n):
    dp = {1: 1}

    for num in range(2, n + 1):
        dp[num] = 0 if num == n else num
        for i in range(1, num):
            val = dp[i] * dp[num - i]
            dp[num] = max(dp[num], val)
    
    def dfs(num):
        if num in dp:
            return dp[num]

        res = 0 if num == n else num
        for i in range(1, num):
            val = dfs(i) * dfs(num - i)
            res = max(res, val)

        dp[num] = res
        return res

    return dfs(n)

def main():
    result = integer_break(2)
    print(result) # 1

    result = integer_break(10)
    print(result) # 36

if __name__ == "__main__":
    main()
