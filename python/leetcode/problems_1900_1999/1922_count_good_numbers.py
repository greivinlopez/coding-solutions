# ------------------------
# 1922. Count Good Numbers
# ------------------------

# Problem: https://leetcode.com/problems/count-good-numbers
#
# A digit string is good if the digits (0-indexed) at even indices are even and
# the digits at odd indices are prime (2, 3, 5, or 7).
#         
#   * For example, "2582" is good because the digits (2 and 8) at even positions 
#     are even and the digits (5 and 2) at odd positions are prime. However,
#     "3245" is not good because 3 is at an even index but is not even.
# 
# Given an integer n, return the total number of good digit strings of length n.
# Since the answer may be large, return it modulo 10^9 + 7.
# 
# A digit string is a string consisting of digits 0 through 9 that may contain
# leading zeros.
# 
# Example 1:
# 
# Input: n = 1
# Output: 5
# 
# Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
# 
# Example 2:
# 
# Input: n = 4
# Output: 400
# 
# Example 3:
# 
# Input: n = 50
# Output: 564908303
# 
# 
# Constraints:
#    1 <= n <= 10^15

from math import ceil

# Solution: https://youtu.be/y_XVeVUpdP4
# Credit: Navdeep Singh founder of NeetCode
def count_good_numbers(n):
    MOD = 10**9 + 7

    def pow(x, n):
        # 5^8
        # 25^4
        # 625^2
        # (625^2)^1
        res = 1
        while n > 0:
            if n % 2:
                res = (res * x) % MOD
            n = n // 2
            x = (x * x) % MOD
        return res

    even = ceil(n / 2)
    odd = n // 2
    return (pow(5, even) * pow(4, odd)) % MOD
    # Time: O(log(n))
    # Space: O(1)


def main():
    result = count_good_numbers(1)
    print(result) # 5

    result = count_good_numbers(4)
    print(result) # 400

    result = count_good_numbers(50)
    print(result) # 564908303

if __name__ == "__main__":
    main()
