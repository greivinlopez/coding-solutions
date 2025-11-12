# -----------------------
# 1416. Restore The Array
# -----------------------

# Problem: https://leetcode.com/problems/restore-the-array
#
# A program was supposed to print an array of integers. The program forgot to
# print whitespaces and the array is printed as a string of digits s and all we
# know is that all integers in the array were in the range [1, k] and there are no
# leading zeros in the array.
# 
# Given the string s and the integer k, return the number of the possible arrays
# that can be printed as s using the mentioned program. Since the answer may be
# very large, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: s = "1000", k = 10000
# Output: 1
# 
# Explanation: The only possible array is [1000]
# 
# Example 2:
# 
# Input: s = "1000", k = 10
# Output: 0
# 
# Explanation: There cannot be an array that was printed this way and has all
# integer >= 1 and <= 10.
# 
# Example 3:
# 
# Input: s = "1317", k = 2000
# Output: 8
# 
# Explanation: Possible arrays are
# [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s consists of only digits and does not contain leading zeros.
#         1 <= k <= 10⁹


# Solution: https://algo.monster/liteproblems/1416
# Credit: AlgoMonster
def number_of_arrays(s, k):
    mod = 10 ** 9 + 7
    dp = [0] * (len(s) + 1)
    dp[-1] = 1

    for i in range(len(s) - 1, -1, -1):
        dp[i], curr = 0, 0
        for j in range(i, len(s)):
            if curr == 0 and s[i] == '0':  # Leading zeros is not allowed
                break
            curr = 10 * curr + int(s[j])
            if curr > k:  # If it exceeds, end the inner loop
                break
            dp[i] += dp[j + 1]
            dp[i] %= mod

    return dp[0]
    # Time: O(n * dₖ)
    # Space: O(n)
    # dₖ = the number of digits in the integer k, which is dₖ = ⌈log₁₀(k+1)⌉.


def main():
    result = number_of_arrays(s = "1000", k = 10000)
    print(result) # 1

    result = number_of_arrays(s = "1000", k = 10)
    print(result) # 0

    result = number_of_arrays(s = "1317", k = 2000)
    print(result) # 8

if __name__ == "__main__":
    main()
