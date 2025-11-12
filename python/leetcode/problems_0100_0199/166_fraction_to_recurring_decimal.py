# -------------------------------------
# 166. Fraction to Recurring Decimal 🧮
# -------------------------------------

# Problem: https://leetcode.com/problems/fraction-to-recurring-decimal
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
# 
# If the fractional part is repeating, enclose the repeating part in parentheses.
# 
# If multiple answers are possible, return any of them.
# 
# It is guaranteed that the length of the answer string is less than 104 for all
# the given inputs.
# 
# Example 1:
# 
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# 
# Example 2:
# 
# Input: numerator = 2, denominator = 1
# Output: "2"
# 
# Example 3:
# 
# Input: numerator = 4, denominator = 333
# Output: "0.(012)"
# 
# 
# Constraints:
#         -2³¹ <= numerator, denominator <= 2³¹ - 1
#         denominator != 0


# Solution: https://leetcode.com/problems/fraction-to-recurring-decimal/solutions/7219090/simple-approach-beats-100-java-c-python
# Credit: Kedar Bhawthankar -> https://leetcode.com/u/kedarbhawthankar/
def fraction_to_decimal(numerator, denominator):
    if numerator == 0:
        return "0"

    res = []
    # Handle sign
    if (numerator < 0) ^ (denominator < 0):
        res.append("-")

    num, den = abs(numerator), abs(denominator)
    res.append(str(num // den))
    remainder = num % den
    if remainder == 0:
        return "".join(res)

    res.append(".")
    seen = {}
    while remainder:
        if remainder in seen:
            idx = seen[remainder]
            res.insert(idx, "(")
            res.append(")")
            return "".join(res)
        seen[remainder] = len(res)
        remainder *= 10
        res.append(str(remainder // den))
        remainder %= den

    return "".join(res)
    # Time: O(n)
    # Space: O(n)


def main():
    result = fraction_to_decimal(numerator = 1, denominator = 2)
    print(result) # "0.5"

    result = fraction_to_decimal(numerator = 2, denominator = 1)
    print(result) # "2"

    result = fraction_to_decimal(numerator = 4, denominator = 333)
    print(result) # "0.(012)"

if __name__ == "__main__":
    main()
