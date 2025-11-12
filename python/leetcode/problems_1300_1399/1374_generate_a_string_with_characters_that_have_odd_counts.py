# ------------------------------------------------------------
# 1374. Generate a String With Characters That Have Odd Counts
# ------------------------------------------------------------

# Problem: https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts
#
# Given an integer n, return a string with n characters such that each character
# in such string occurs an odd number of times.
# 
# The returned string must contain only lowercase English letters. If there are
# multiples valid strings, return any of them. 
# 
# Example 1:
# 
# Input: n = 4
# Output: "pppz"
# 
# Explanation: "pppz" is a valid string since the character 'p' occurs three times
# and the character 'z' occurs once. Note that there are many other valid strings
# such as "ohhh" and "love".
# 
# Example 2:
# 
# Input: n = 2
# Output: "xy"
# 
# Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once.
# Note that there are many other valid strings such as "ag" and "ur".
# 
# Example 3:
# 
# Input: n = 7
# Output: "holasss"
# 
# 
# Constraints:
#         1 <= n <= 500


# Solution: https://algo.monster/liteproblems/1374
# Credit: AlgoMonster
def generate_the_string(n):
    # Check if n is odd using bitwise AND operation
    if n & 1:  # n is odd
        # If n is odd, return n 'a's (odd count)
        return 'a' * n
    else:  # n is even
        # If n is even, return (n-1) 'a's and 1 'b'
        # This ensures 'a' appears odd times (n-1) and 'b' appears odd times (1)
        return 'a' * (n - 1) + 'b'
    # Time: O(n)
    # Space: O(n)


def main():
    result = generate_the_string(n = 4)
    print(result) # "aaab"

    result = generate_the_string(n = 2)
    print(result) # "ab"

    result = generate_the_string(n = 7)
    print(result) # "aaaaaaa"

if __name__ == "__main__":
    main()
