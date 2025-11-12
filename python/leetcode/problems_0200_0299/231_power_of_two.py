# -----------------
# 231. Power Of Two
# -----------------

# Problem: https://youtu.be/H2bjttEV4Vc
# 
# Given an integer n, return true if it is a power of two. Otherwise, 
# return false.
# 
# An integer n is a power of two, if there exists an integer x such 
# that n == 2x.
# 
#  
# Example 1:
# 
# Input: n = 1
# Output: true
# Explanation: 20 = 1
# 
# 
# Example 2:
# 
# Input: n = 16
# Output: true
# Explanation: 24 = 16
# 
# 
# Example 3:
# 
# Input: n = 3
# Output: false
# 
#  
# Constraints:
# 
# 	-231 <= n <= 231 - 1
#  
# Follow up: Could you solve it without loops/recursion?


# Solution: https://youtu.be/H2bjttEV4Vc
# Credit: Navdeep Singh founder of NeetCode

# iterative
def is_power_of_two_iter(n):
    x = 1
    while x < n:
        x *= 2
    return x == n        

# Bit manipulation
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Bit manipulation
def is_power_of_two_bit(n):
    return n > 0 and ((1 << 30) % n) == 0


def main():
    result = is_power_of_two(1)
    print(result) # True

    result = is_power_of_two(16)
    print(result) # True

    result = is_power_of_two(3)
    print(result) # False

if __name__ == "__main__":
    main()
