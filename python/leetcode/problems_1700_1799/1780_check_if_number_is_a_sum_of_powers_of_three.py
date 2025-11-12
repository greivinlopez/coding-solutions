# -------------------------------------------------
# 1780. Check if Number is a Sum of Powers of Three
# -------------------------------------------------

# Problem: https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three
#
# Given an integer n, return true if it is possible to represent n as the sum of
# distinct powers of three. Otherwise, return false.
# 
# An integer y is a power of three if there exists an integer x such that y == 3x.
# 
# Example 1:
# 
# Input: n = 12
# Output: true
# 
# Explanation: 12 = 3^1 + 3^2
# 
# Example 2:
# 
# Input: n = 91
# Output: true
# 
# Explanation: 91 = 3^0 + 3^2 + 3^4
# 
# Example 3:
# 
# Input: n = 21
# Output: false
# 
# 
# Constraints:
#         1 <= n <= 10^7


# Solution: https://youtu.be/99ExTh_0Ycg
# Credit: Navdeep Singh founder of NeetCode
def check_powers_of_three(n):
    i = 0
    while 3**(i + 1) <= n:
        i += 1
    
    while i >= 0:
        power = 3**i
        if power <= n:
            n -= power
        if power <= n:
            return False
        i -= 1
    
    return n == 0
    # Time: O(log(n))
    # Space: O(1)


def main():
    result = check_powers_of_three(12)
    print(result) # True

    result = check_powers_of_three(91)
    print(result) # True

    result = check_powers_of_three(21)
    print(result) # False

if __name__ == "__main__":
    main()
