# ------------------
# 342. Power of Four
# ------------------

# Problem: https://leetcode.com/problems/power-of-four
#
# Given an integer n, return true if it is a power of four. Otherwise, return
# false.
# 
# An integer n is a power of four, if there exists an integer x such that n == 4x.
# 
# Example 1:
# 
# Input: n = 16
# Output: true
# 
# Example 2:
# 
# Input: n = 5
# Output: false
# 
# Example 3:
# 
# Input: n = 1
# Output: true
# 
# 
# Constraints:
#         -2^31 <= n <= 2^31 - 1
# 
# Follow up: Could you solve it without loops/recursion?

import math

# Solution: https://youtu.be/qEYZPwnlM0U
# Credit: Navdeep Singh founder of NeetCode
def is_power_of_four(n):
    if n == 1:
        return True
    if n <= 0 or n % 4:
        return False
    return is_power_of_four(n // 4)
    # Time: O(log₄ n)
    # Space: O(log₄ n)

def is_power_of_four_alt(n):
    # More efficient solution
    return n > 0 and math.log(n, 4) % 1 == 0

def main():
    result = is_power_of_four(16)
    print(result) # True

    result = is_power_of_four(5)
    print(result) # False

    result = is_power_of_four(1)
    print(result) # True

if __name__ == "__main__":
    main()
