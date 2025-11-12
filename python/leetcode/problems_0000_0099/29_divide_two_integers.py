# -----------------------
# 29. Divide Two Integers
# -----------------------

# Problem: https://leetcode.com/problems/divide-two-integers
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator.
# 
# The integer division should truncate toward zero, which means losing its
# fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would
# be truncated to -2.
# 
# Return the quotient after dividing dividend by divisor.
# 
# Note: Assume we are dealing with an environment that could only store integers
# within the 32-bit signed integer range: [−2³¹, 2³¹ − 1]. For this problem, if
# the quotient is strictly greater than 231 - 1, then return 2³¹ - 1, and if the
# quotient is strictly less than -2³¹, then return -2³¹.
# 
# Example 1:
# 
# Input: dividend = 10, divisor = 3
# Output: 3
# 
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# 
# Example 2:
# 
# Input: dividend = 7, divisor = -3
# Output: -2
# 
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
# 
# 
# Constraints:
#         -2³¹ <= dividend, divisor <= 2³¹ - 1
#         divisor != 0


# Solution: https://youtu.be/xefkgtd44hg
# Credit: CheatCode Ninja
def divide_alt(dividend, divisor):
    a = abs(dividend)
    b = abs(divisor)
    
    negative = (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0)
    
    output = 0
    
    while a >= b:
        counter = 1
        decrement = b
        
        while a >= decrement:
            a -= decrement
            
            output += counter
            counter += counter
            decrement += decrement
    
    output = output if not negative else -output
    
    return min(max(-2147483648, output), 2147483647)
    # Time: O(log²n)
    # Space: O(1)

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def divide(dividend, divisor):
    if dividend == 0:
        return 0
    if divisor == 1:
        return min(max(dividend, -2**31), 2**31 - 1)
    if divisor == -1:
        return min(max(-dividend, -2**31), 2**31 - 1)

    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0
    
    while dividend >= divisor:
        temp, multiple = divisor, 1
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        dividend -= temp
        quotient += multiple

    quotient *= sign
    return min(max(quotient, -2**32), 2**31-1)
    # Time: O(log²n)
    # Space: O(1)


def main():
    result = divide(dividend = 10, divisor = 3)
    print(result) # 3

    result = divide(dividend = 7, divisor = -3)
    print(result) # -2

if __name__ == "__main__":
    main()
