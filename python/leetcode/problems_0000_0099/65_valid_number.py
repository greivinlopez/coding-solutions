# ----------------
# 65. Valid Number
# ----------------

# Problem: https://leetcode.com/problems/valid-number
#
# Given a string s, return whether s is a valid number.
# 
# For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14",
# "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while
# the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6",
# "-+3", "95a54e53".
# 
# Formally, a valid number is defined using one of the following definitions:
#         
#   * An integer number followed by an optional exponent.
#   * A decimal number followed by an optional exponent.
# 
# An integer number is defined with an optional sign '-' or '+' followed by
# digits.
# 
# A decimal number is defined with an optional sign '-' or '+' followed by one of
# the following definitions:
# 
#         Digits followed by a dot '.'.
#         Digits followed by a dot '.' followed by digits.
#         A dot '.' followed by digits.
# 
# An exponent is defined with an exponent notation 'e' or 'E' followed by an
# integer number.
# 
# The digits are defined as one or more digits.
# 
# Example 1:
# 
# Input: s = "0"
# Output: true
# 
# Example 2:
# 
# Input: s = "e"
# Output: false
# 
# Example 3:
# 
# Input: s = "."
# Output: false
# 
# 
# Constraints:
#         1 <= s.length <= 20
#         s consists of only English letters (both uppercase and lowercase),
# digits (0-9), plus '+', minus '-', or dot '.'.

import re

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def is_number_re(s):
    pattern = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$')
    return bool(pattern.match(s))
    # Time: O(n)
    # Space: O(1)


# Alternative Solution
def is_number(s):
    if not s:
        return False
    
    s = s.strip()  # Remove leading/trailing whitespace
    if not s:
        return False
    
    i = 0
    n = len(s)
    
    # Helper function to check if character is a digit
    def is_digit(c):
        return '0' <= c <= '9'
    
    # Handle optional sign
    if i < n and s[i] in '+-':
        i += 1
    
    # Track what we've seen
    has_digit = False
    has_dot = False
    
    # Parse the number part (before 'e'/'E')
    while i < n and (is_digit(s[i]) or s[i] == '.'):
        if s[i] == '.':
            if has_dot:  # Second dot is invalid
                return False
            has_dot = True
        else:  # It's a digit
            has_digit = True
        i += 1
    
    # Must have at least one digit before 'e'/'E'
    if not has_digit:
        return False
    
    # Handle optional exponent part
    if i < n and s[i] in 'eE':
        i += 1
        
        # Exponent must have optional sign followed by digits
        if i < n and s[i] in '+-':
            i += 1
        
        # Must have at least one digit in exponent
        has_exp_digit = False
        while i < n and is_digit(s[i]):
            has_exp_digit = True
            i += 1
        
        if not has_exp_digit:
            return False
    
    # Must have consumed entire string
    return i == n
    # Time: O(n)
    # Space: O(1)

def main():
    result = is_number(s = "0")
    print(result) # True

    result = is_number(s = "e")
    print(result) # False

    result = is_number(s = ".")
    print(result) # False

if __name__ == "__main__":
    main()
