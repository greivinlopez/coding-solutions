# ------------------------
# 227. Basic Calculator II
# ------------------------

# Problem: https://leetcode.com/problems/basic-calculator-ii
#
# Given a string s which represents an expression, evaluate this expression and
# return its value. 
# 
# The integer division should truncate toward zero.
# 
# You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-2³¹, 2³¹ - 1].
# 
# Note: You are not allowed to use any built-in function which evaluates strings
# as mathematical expressions, such as eval().
# 
# Example 1:
# 
# Input: s = "3+2*2"
# Output: 7
# 
# Example 2:
# 
# Input: s = " 3/2 "
# Output: 1
# 
# Example 3:
# 
# Input: s = " 3+5 / 2 "
# Output: 5
# 
# 
# Constraints:
#   1 <= s.length <= 3 * 10⁵
#   s consists of integers and operators ('+', '-', '*', '/') separated by some 
#   number of spaces.
#   s represents a valid expression.
#   All the integers in the expression are non-negative integers in the range [0, 2³¹ - 1].
#   The answer is guaranteed to fit in a 32-bit integer.

import math

# Solution: https://leetcode.com/problems/basic-calculator-ii/solutions/507990/python-3-runtime-76ms-stack-approach
# Credit: Tim Zeng -> https://leetcode.com/u/timzeng/
def calculate(s):
    num, presign, stack=0, "+", []
    for i in s+'+':
        if i.isdigit():
            num = num*10 +int(i)
        elif i in '+-*/':
            if presign =='+':
                stack.append(num)
            if presign =='-':
                stack.append(-num)
            if presign =='*':
                stack.append(stack.pop()*num)
            if presign == '/':
                stack.append(math.trunc(stack.pop()/num))
            presign = i
            num = 0
    return sum(stack)
    # Time: O(n)
    # Space: O(n)


def main():
    result = calculate("3+2*2")
    print(result) # 7

    result = calculate(" 3/2 ")
    print(result) # 1

    result = calculate(" 3+5 / 2 ")
    print(result) # 5

if __name__ == "__main__":
    main()
