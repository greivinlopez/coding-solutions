# -----------------------
# 879. Profitable Schemes
# -----------------------

# Problem: https://leetcode.com/problems/profitable-schemes
#
# There is a group of n members, and a list of various crimes they could commit.
# The ith crime generates a profit[i] and requires group[i] members to participate
# in it. If a member participates in one crime, that member can't participate in
# another crime.
# 
# Let's call a profitable scheme any subset of these crimes that generates at
# least minProfit profit, and the total number of members participating in that
# subset of crimes is at most n.
# 
# Return the number of schemes that can be chosen. Since the answer may be very
# large, return it modulo 10^9 + 7.
# 
# Example 1:
# 
# Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# Output: 2
# 
# Explanation: To make a profit of at least 3, the group could either commit
# crimes 0 and 1, or just crime 1.
# In total, there are 2 schemes.
# 
# Example 2:
# 
# Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
# Output: 7
# 
# Explanation: To make a profit of at least 5, the group could commit any crimes,
# as long as they commit one.
# There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
# 
# Constraints:
#         1 <= n <= 100
#         0 <= minProfit <= 100
#         1 <= group.length <= 100
#         1 <= group[i] <= 100
#         profit.length == group.length
#         0 <= profit[i] <= 100

from collections import defaultdict

# Solution: https://youtu.be/CcLKQLKvOl8
# Credit: Navdeep Singh founder of NeetCode
def profitable_schemes_memo(n, min_profit, group, profit):
    # Memoization
    mod = 10**9 + 7

    dp = {}
    def dfs(i, n, p):
        if i == len(group):
            return 1 if p >= min_profit else 0

        if (i, n, p) in dp:
            return dp[(i, n, p)]

        dp[(i, n, p)] = dfs(i + 1, n, p)
        if n - group[i] >= 0:
            dp[(i, n, p)] += dfs(i + 1, n - group[i], p + profit[i]) % mod

        return dp[(i, n, p)]

    return dfs(0, n, 0)
    # Time: O(n * m * p) where m is the length of the group and p is the minimum profit


def profitable_schemes(n, min_profit, group, profit):
    mod = 10**9 + 7

    dp = defaultdict(int)

    for m in range(n + 1):
        dp[(len(group), m, min_profit)] = 1

    for i in range(len(group) - 1, -1, -1):
        for m in range(n + 1):
            for p in range(min_profit + 1):
                dp[(i, m, p)] = dp[(i + 1, m, p)]
                if m + group[i] <= n:
                    dp[(i, m, p)] += dp[(i + 1, m + group[i], min(min_profit, p + profit[i]))] % mod

    return dp[(0, 0, 0)] % mod


def main():
    result = profitable_schemes(n = 5, min_profit = 3, group = [2,2], profit = [2,3])
    print(result) # 2

    result = profitable_schemes(n = 10, min_profit = 5, group = [2,3,5], profit = [6,7,8])
    print(result) # 7

if __name__ == "__main__":
    main()
