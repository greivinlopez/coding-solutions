# -------------------------------------------------------------
# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
# -------------------------------------------------------------

# Problem: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers
#
# A decimal number is called deci-binary if each of its digits is either 0 or 1
# without any leading zeros. For example, 101 and 1100 are deci-binary, while 112
# and 3001 are not.
# 
# Given a string n that represents a positive decimal integer, return the minimum
# number of positive deci-binary numbers needed so that they sum up to n.
# 
# Example 1:
# 
# Input: n = "32"
# Output: 3
# 
# Explanation: 10 + 11 + 11 = 32
# 
# Example 2:
# 
# Input: n = "82734"
# Output: 8
# 
# Example 3:
# 
# Input: n = "27346209830709182346"
# Output: 9
# 
# 
# Constraints:
#         1 <= n.length <= 10⁵
#         n consists of only digits.
#         n does not contain any leading zeros and represents a positive integer.


# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def min_partitions(n):
    # Find the maximum digit in the string representation of n
    # This works because each deci-binary number can contribute at most 1 to each digit position
    # Therefore, we need at least as many numbers as the largest digit value
    max_digit = max(n)
    
    # Convert the character digit to integer and return
    return int(max_digit)
    # Time: O(n)
    # Space: O(1)


def main():
    result = min_partitions(n = "32")
    print(result) # 3

    result = min_partitions(n = "82734")
    print(result) # 8

    result = min_partitions(n = "27346209830709182346")
    print(result) # 9

if __name__ == "__main__":
    main()
