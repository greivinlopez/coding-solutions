# ---------------------
# 7. Reverse Integer ⬅️
# ---------------------

# Problem: https://leetcode.com/problems/reverse-integer
#
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing
# x causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ - 1], 
# then return 0.
# 
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
# 
# Example 1:
# 
# Input: x = 123
# Output: 321
# 
# Example 2:
# 
# Input: x = -123
# Output: -321
# 
# Example 3:
# 
# Input: x = 120
# Output: 21
# 
# 
# Constraints:
#         -2³¹ <= x <= 2³¹ - 1

# Solution: https://youtu.be/HAgLH58IgJQ
# Credit: Navdeep Singh founder of NeetCode 
import math
def reverse_alt(x):
    # Integer.MAX_VALUE = 2147483647 (end with 7)
    # Integer.MIN_VALUE = -2147483648 (end with -8 )
    MIN = -2147483648  # -2^31,
    MAX = 2147483647  #  2^31 - 1

    res = 0
    while x:
        digit = int(math.fmod(x, 10))  # (python dumb) -1 %  10 = 9
        x = int(x / 10)  # (python dumb) -1 // 10 = -1

        if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
            return 0
        if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
            return 0
        res = (res * 10) + digit

    return res
    # Time: O(log|x|)
    # Space: O(1)

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def reverse(x):
    is_negative = False
    if x < 0:
        is_negative = True
        x = -x

    # Reverse the integer
    reversed_x = 0
    while x > 0:
        reversed_x = reversed_x * 10 + x % 10
        x //= 10

    # Check for overflow
    if is_negative:
        reversed_x = -reversed_x

    if reversed_x > 2**31 - 1 or reversed_x < -2**31:
        return 0 

    return reversed_x
    # Time: O(log|x|)
    # Space: O(1)


def main():
    result = reverse(123) # 321
    print(result)
    result = reverse(-123) # -321
    print(result)
    result = reverse(120) # 21
    print(result)

if __name__ == "__main__":
    main()