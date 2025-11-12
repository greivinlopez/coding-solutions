# -------------------
# 326. Power of Three
# -------------------

# Problem: https://leetcode.com/problems/power-of-three
#
# Given an integer n, return true if it is a power of three. Otherwise, return
# false.
# 
# An integer n is a power of three, if there exists an integer x such that n == 3x.
# 
# Example 1:
# 
# Input: n = 27
# Output: true
# 
# Explanation: 27 = 33
# 
# Example 2:
# 
# Input: n = 0
# Output: false
# 
# Explanation: There is no x where 3x = 0.
# 
# Example 3:
# 
# Input: n = -1
# Output: false
# 
# Explanation: There is no x where 3x = (-1).
# 
# 
# Constraints:
#         -2³¹ <= n <= 2³¹ - 1
# 
# Follow up: Could you solve it without loops/recursion?


# Solution: https://leetcode.com/problems/power-of-three/solutions/7073228/100-fast-easy-power-of-three-check-lightning-fast-intuitive-solution
# Credit: Sandesh Naik -> https://leetcode.com/u/Sandesh_naik07/
def is_power_of_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1
    # Time: O(log₃(n))
    # Space: O(1)


def main():
    result = is_power_of_three(27)
    print(result) # True

    result = is_power_of_three(0)
    print(result) # False

    result = is_power_of_three(-1)
    print(result) # False

if __name__ == "__main__":
    main()
