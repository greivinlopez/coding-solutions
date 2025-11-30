# ------------------------------------------------
# 1663. Smallest String With A Given Numeric Value
# ------------------------------------------------

# Problem: https://leetcode.com/problems/smallest-string-with-a-given-numeric-value
#
# The numeric value of a lowercase character is defined as its position
# (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value
# of b is 2, the numeric value of c is 3, and so on.
# 
# The numeric value of a string consisting of lowercase characters is defined as
# the sum of its characters' numeric values. For example, the numeric value of the
# string "abe" is equal to 1 + 2 + 5 = 8.
# 
# You are given two integers n and k. Return the lexicographically smallest string
# with length equal to n and numeric value equal to k.
# 
# Note that a string x is lexicographically smaller than string y if x comes
# before y in dictionary order, that is, either x is a prefix of y, or if i is the
# first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic
# order.
# 
# Example 1:
# 
# Input: n = 3, k = 27
# Output: "aay"
# 
# Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the
# smallest string with such a value and length equal to 3.
# 
# Example 2:
# 
# Input: n = 5, k = 73
# Output: "aaszz"
# 
# 
# Constraints:
#         1 <= n <= 10⁵
#         n <= k <= 26 * n


# Solution: https://algo.monster/liteproblems/1663
# Credit: AlgoMonster
def get_smallest_string(n, k):
    # Initialize result array with all 'a's (smallest possible characters)
    result = ['a'] * n
    
    # Start from the rightmost position
    position = n - 1
    
    # Calculate the excess value we need to distribute
    # (k - n) because we already have n 'a's, each worth 1
    excess_value = k - n
    
    # Greedily place 'z' characters from right to left
    # Each 'z' adds 25 to the value (since 'z'=26 and 'a'=1)
    while excess_value > 25:
        result[position] = 'z'
        excess_value -= 25
        position -= 1
    
    # Place the remaining value at the current position
    # Convert the character at current position from 'a' to the required character
    result[position] = chr(ord(result[position]) + excess_value)
    
    # Convert list to string and return
    return ''.join(result)
    # Time: O(n)
    # Space: O(n)


def main():
    result = get_smallest_string(n = 3, k = 27)
    print(result) # "aay"

    result = get_smallest_string(n = 5, k = 73)
    print(result) # "aaszz"

if __name__ == "__main__":
    main()
