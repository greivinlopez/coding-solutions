# ----------------------------------------------------------
# 1281. Subtract the Product and Sum of Digits of an Integer
# ----------------------------------------------------------

# Problem: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer
#
# Given an integer number n, return the difference between the product of its
# digits and the sum of its digits.
# 
# Example 1:
# 
# Input: n = 234
# Output: 15
# 
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15
# 
# Example 2:
# 
# Input: n = 4421
# Output: 21
# 
# Explanation:
# Product of digits = 4 * 4 * 2 * 1 = 32
# Sum of digits = 4 + 4 + 2 + 1 = 11
# Result = 32 - 11 = 21
# 
# 
# Constraints:
#         1 <= n <= 10^5


# Solution: https://algo.monster/liteproblems/1281
# Credit: AlgoMonster
def subtract_product_and_sum(n):
    product = 1  # Initialize product to 1 (multiplicative identity)
    digit_sum = 0  # Initialize sum to 0 (additive identity)
    
    # Extract each digit from right to left
    while n > 0:
        # Get the last digit using divmod
        # divmod(n, 10) returns (quotient, remainder)
        n, digit = divmod(n, 10)
        
        # Update product by multiplying with current digit
        product *= digit
        
        # Update sum by adding current digit
        digit_sum += digit
    
    # Return the difference between product and sum
    return product - digit_sum
    # Time: O(log n)
    # Space: O(1)

# Solution: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/solutions/468188/python-3-two-solutions-faster-than-9591-q1twa
# Credit: Denis Rasulev -> https://leetcode.com/u/denisrasulev/
from functools import reduce

def subtract_product_and_sum_alt(n):
    a = [int(x) for x in str(n)]
    return reduce((lambda x, y: x * y), a) - reduce((lambda x, y: x + y), a)
    # Time: O((log n)²)
    # Space: O(log n)


def main():
    result = subtract_product_and_sum(n = 234)
    print(result) # 15

    result = subtract_product_and_sum(n = 4421)
    print(result) # 21

if __name__ == "__main__":
    main()
