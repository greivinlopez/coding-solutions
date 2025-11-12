# --------------------------------------
# 592. Fraction Addition and Subtraction
# --------------------------------------

# Problem: https://leetcode.com/problems/fraction-addition-and-subtraction
#
# Given a string expression representing an expression of fraction addition and
# subtraction, return the calculation result in string format.
# 
# The final result should be an irreducible fraction. If your final result is an
# integer, change it to the format of a fraction that has a denominator 1. So in
# this case, 2 should be converted to 2/1.
# 
# Example 1:
# 
# Input: expression = "-1/2+1/2"
# Output: "0/1"
# 
# Example 2:
# 
# Input: expression = "-1/2+1/2+1/3"
# Output: "1/3"
# 
# Example 3:
# 
# Input: expression = "1/3-1/2"
# Output: "-1/6"
# 
# 
# Constraints:
#         
#   * The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
#   * Each fraction (input and output) has the format ±numerator/denominator.
#     If the first input fraction or the output is positive, then '+' will be omitted.
#   * The input only contains valid irreducible fractions, where the numerator
#     and denominator of each fraction will always be in the range [1, 10]. If the
#     denominator is 1, it means this fraction is actually an integer in a fraction
#     format defined above.
#   * The number of given fractions will be in the range [1, 10].
#   * The numerator and denominator of the final result are guaranteed to be valid and 
#     in the range of 32-bit int.

from math import gcd

# Solution: https://algo.monster/liteproblems/592
# Credit: AlgoMonster
def fraction_addition(expression):
    # Initialize numerator and common denominator
    # Using LCM of 1-10 as common denominator (2520)
    numerator = 0
    common_denominator = 6 * 7 * 8 * 9 * 10  # 2520
    
    # Handle case where expression starts with a positive fraction
    # Add '+' sign to maintain consistent parsing pattern
    if expression[0].isdigit():
        expression = '+' + expression
    
    # Parse and process each fraction in the expression
    index = 0
    expression_length = len(expression)
    
    while index < expression_length:
        # Determine sign of current fraction
        sign = -1 if expression[index] == '-' else 1
        index += 1
        
        # Find the end of current fraction (next sign or end of string)
        fraction_end = index
        while fraction_end < expression_length and expression[fraction_end] not in '+-':
            fraction_end += 1
        
        # Extract and parse the fraction
        fraction_string = expression[index:fraction_end]
        fraction_numerator, fraction_denominator = fraction_string.split('/')
        
        # Add current fraction to accumulated result
        # Convert to common denominator before adding
        numerator += sign * int(fraction_numerator) * common_denominator // int(fraction_denominator)
        
        # Move to next fraction
        index = fraction_end
    
    # Simplify the final fraction by dividing by GCD
    greatest_common_divisor = gcd(numerator, common_denominator)
    numerator //= greatest_common_divisor
    common_denominator //= greatest_common_divisor
    
    # Return the simplified fraction as string
    return f'{numerator}/{common_denominator}'


def main():
    result = fraction_addition("-1/2+1/2")
    print(result) # "0/1"

    result = fraction_addition("-1/2+1/2+1/3")
    print(result) # "1/3"

    result = fraction_addition("1/3-1/2")
    print(result) # "-1/6"

if __name__ == "__main__":
    main()
