# ---------------------
# 224. Basic Calculator
# ---------------------

# Problem: https://leetcode.com/problems/basic-calculator
#
# Given a string s representing a valid expression, implement a basic calculator
# to evaluate it, and return the result of the evaluation.
# 
# Note: You are not allowed to use any built-in function which evaluates strings
# as mathematical expressions, such as eval().
# 
# Example 1:
# 
# Input: s = "1 + 1"
# Output: 2
# 
# Example 2:
# 
# Input: s = " 2-1 + 2 "
# Output: 3
# 
# Example 3:
# 
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# 
# 
# Constraints:
#         1 <= s.length <= 3 * 10⁵
#         s consists of digits, '+', '-', '(', ')', and ' '.
#         s represents a valid expression.
#         '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
#         '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
#         There will be no two consecutive operators in the input.
#         Every number and running calculation will fit in a signed 32-bit integer.


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def calculate(s):
    ans = 0
    num = 0
    sign = 1
    
    stack = [sign]
    
    for c in s:
        if c.isdigit():
            num = num * 10 + (ord(c) - ord('0'))
        elif c == "(":
            stack.append(sign)
        elif c == ")":
            stack.pop()
        elif c == "+" or c == "-":
            ans += sign * num
            sign = (1 if c == "+" else -1) *stack[-1]
            num = 0
            
    return ans + sign * num
    # Time: O(n)
    # Space: O(d)
    # d = the maximum depth of nested parentheses.


def main():
    result = calculate(s = "1 + 1")
    print(result) # 2

    result = calculate(s = " 2-1 + 2 ")
    print(result) # 3

    result = calculate(s = "(1+(4+5+2)-3)+(6+8)")
    print(result) # 23

if __name__ == "__main__":
    main()
