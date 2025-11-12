# ---------------------------
# 972. Equal Rational Numbers
# ---------------------------

# Problem: https://leetcode.com/problems/equal-rational-numbers
#
# Given two strings s and t, each of which represents a non-negative rational
# number, return true if and only if they represent the same number. The strings
# may use parentheses to denote the repeating part of the rational number.
# 
# A rational number can be represented using up to three parts: <IntegerPart>,
# <NonRepeatingPart>, and a <RepeatingPart>. The number will be represented in one
# of the following three ways:
#         
#   <IntegerPart>
#       For example, 12, 0, and 123.
#   <IntegerPart><.><NonRepeatingPart>
#       For example, 0.5, 1., 2.12, and 123.0001.
#   <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)>
#       For example, 0.1(6), 1.(9), 123.00(1212).
# 
# The repeating portion of a decimal expansion is conventionally denoted within a
# pair of round brackets. For example:
# 
#         1/6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66).
# 
# Example 1:
# 
# Input: s = "0.(52)", t = "0.5(25)"
# Output: true
# 
# Explanation: Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents
# 0.52525252525..... , the strings represent the same number.
# 
# Example 2:
# 
# Input: s = "0.1666(6)", t = "0.166(66)"
# Output: true
# 
# Example 3:
# 
# Input: s = "0.9(9)", t = "1."
# Output: true
# 
# Explanation: "0.9(9)" represents 0.999999999... repeated forever, which equals
# 1.  [See this link for an explanation.]
# "1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and
# (NonRepeatingPart) = "".
# 
# 
# Constraints:
#         Each part consists only of digits.
#         The <IntegerPart> does not have leading zeros (except for the zero itself).
#         1 <= <IntegerPart>.length <= 4
#         0 <= <NonRepeatingPart>.length <= 4
#         1 <= <RepeatingPart>.length <= 4


# Solution: https://leetcode.com/problems/equal-rational-numbers/solutions/3532970/solution
def is_rational_equal(S, T):
    def f(s):
        i = s.find('(')
        if i >= 0:
            s = s[:i] + s[i + 1:-1] * 20
        return float(s[:20])
    return f(S) == f(T)
    # Time: O(n)
    # Space: O(n)
    # n = the length of the input strings.

# Alternative Solution: https://algo.monster/liteproblems/972
# Credit: AlgoMonster
def is_rational_equal_alt(s, t):
    def value(s):
        if '(' not in s:
            return float(s)
        i = s.index('(')
        nonRepeating, repeating = s[:i], s[i + 1:-1]
        return float(nonRepeating) + float(repeating) / (10 ** len(repeating) - 1) / 10 ** (i - s.index('.') - 1)
    return abs(value(s) - value(t)) < 1e-9
    # Time: O(n)
    # Space: O(n)
    # n = the maximum length of s and t


def main():
    result = is_rational_equal("0.(52)", "0.5(25)")
    print(result) # True

    result = is_rational_equal("0.1666(6)", "0.166(66)")
    print(result) # True

    result = is_rational_equal("0.9(9)", "1.")
    print(result) # True

if __name__ == "__main__":
    main()
