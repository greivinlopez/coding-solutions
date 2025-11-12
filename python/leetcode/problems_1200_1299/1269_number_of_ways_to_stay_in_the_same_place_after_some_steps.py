# ---------------------------------------------------------------
# 1269. Number of Ways to Stay in the Same Place After Some Steps
# ---------------------------------------------------------------

# Problem: https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps
#
# You have a pointer at index 0 in an array of size arrLen. At each step, you can
# move 1 position to the left, 1 position to the right in the array, or stay in
# the same place (The pointer should not be placed outside the array at any time).
# 
# Given two integers steps and arrLen, return the number of ways such that your
# pointer is still at index 0 after exactly steps steps. Since the answer may be
# too large, return it modulo 10^9 + 7.
# 
# Example 1:
# 
# Input: steps = 3, arrLen = 2
# Output: 4
# Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
# Right, Left, Stay
# Stay, Right, Left
# Right, Stay, Left
# Stay, Stay, Stay
# 
# Example 2:
# 
# Input: steps = 2, arrLen = 4
# Output: 2
# Explanation: There are 2 differents ways to stay at index 0 after 2 steps
# Right, Left
# Stay, Stay
# 
# Example 3:
# 
# Input: steps = 4, arrLen = 2
# Output: 8
# 
# 
# Constraints:
#         1 <= steps <= 500
#         1 <= arrLen <= 10^6


# Solution: https://youtu.be/8YBGXG-8sRI
# Credit: Navdeep Singh founder of NeetCode
def num_ways(steps, arrLen):
    mod = 10**9 + 7
    dp = {}

    def dfs(i, steps):
        if steps == 0:
            return i == 0
        if (i, steps) in dp:
            return dp[(i, steps)]

        res = dfs(i, steps - 1) % mod
        if i > 0:
            res = (res + dfs(i - 1, steps - 1)) % mod
        if i < arrLen - 1:
            res = (res + dfs(i + 1, steps - 1)) % mod

        dp[(i, steps)] = res
        return res

    return dfs(0, steps)
    # Time: O(n * min(n, m))

def num_ways_alt(steps, arrLen):
    mod = 10**9 + 7
    arrLen = min(steps, arrLen)
    dp = [0] * arrLen
    dp[0] = 1

    for steps in range(1, steps + 1):
        next_dp = [0] * arrLen
        for i in range(arrLen):
            next_dp[i] = dp[i]

            if i > 0:
                next_dp[i] = (next_dp[i] + dp[i - 1]) % mod
            if i < arrLen - 1:
                next_dp[i] = (next_dp[i] + dp[i + 1]) % mod
        dp = next_dp

    return dp[0]
    # Time: O(n * m)

def main():
    result = num_ways_alt(steps = 3, arrLen = 2)
    print(result) # 4

    result = num_ways_alt(steps = 2, arrLen = 4)
    print(result) # 2

    result = num_ways_alt(steps = 4, arrLen = 2)
    print(result) # 8

if __name__ == "__main__":
    main()
