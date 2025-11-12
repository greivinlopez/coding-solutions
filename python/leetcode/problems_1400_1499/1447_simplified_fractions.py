# --------------------------
# 1447. Simplified Fractions
# --------------------------

# Problem: https://leetcode.com/problems/simplified-fractions
#
# Given an integer n, return a list of all simplified fractions between 0 and 1
# (exclusive) such that the denominator is less-than-or-equal-to n. You can return
# the answer in any order.
# 
# Example 1:
# 
# Input: n = 2
# Output: ["1/2"]
# 
# Explanation: "1/2" is the only unique fraction with a denominator less-than-or-
# equal-to 2.
# 
# Example 2:
# 
# Input: n = 3
# Output: ["1/2","1/3","2/3"]
# 
# Example 3:
# 
# Input: n = 4
# Output: ["1/2","1/3","1/4","2/3","3/4"]
# 
# Explanation: "2/4" is not a simplified fraction because it can be simplified to
# "1/2".
#
#
#  Constraints:
#         1 <= n <= 100


# Solution: https://algo.monster/liteproblems/1447
# Credit: AlgoMonster
def simplified_fractions(n):
    from math import gcd
    # List comprehension to generate all valid simplified fractions
    return [
        f'{numerator}/{denominator}'  # Format fraction as string
        for numerator in range(1, n)  # Numerator from 1 to n-1
        for denominator in range(numerator + 1, n + 1)  # Denominator from numerator+1 to n
        if gcd(numerator, denominator) == 1  # Only include if fraction is in simplified form
    ]
    # Time: O(n² * log(min(i, j)))
    # Space: O(n²)


def main():
    result = simplified_fractions(2)
    print(result) # ['1/2']

    result = simplified_fractions(3)
    print(result) # ['1/2', '1/3', '2/3']

    result = simplified_fractions(4)
    print(result) # ['1/2', '1/3', '1/4', '2/3', '3/4']

if __name__ == "__main__":
    main()
