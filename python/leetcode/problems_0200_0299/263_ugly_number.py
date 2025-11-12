# ----------------
# 263. Ugly Number
# ----------------

# Problem: https://leetcode.com/problems/ugly-number/
# 
# An ugly number is a positive integer which does not have a prime factor other 
# than 2, 3, and 5.
# 
# Given an integer n, return true if n is an ugly number.
# 
#  
# Example 1:
# 
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# 
# 
# Example 2:
# 
# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors.
# 
# 
# Example 3:
# 
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
# 
# 
# Constraints:
# 
# 	-231 <= n <= 231 - 1


# Solution: https://youtu.be/M0Zay1Qr9ws
# Credit: Navdeep Singh founder of NeetCode
def is_ugly(n):
    if n <= 0:
        return False
    
    for p in [2, 3, 5]:
        while n % p == 0:
            n = n // p
    return n == 1



def main():
    result = is_ugly(6)
    print(result) # True

    result = is_ugly(1)
    print(result) # True

    result = is_ugly(14)
    print(result) # False

if __name__ == "__main__":
    main()
