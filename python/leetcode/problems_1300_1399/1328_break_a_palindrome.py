# ------------------------
# 1328. Break a Palindrome
# ------------------------

# Problem: https://leetcode.com/problems/break-a-palindrome
#
# Given a palindromic string of lowercase English letters palindrome, replace
# exactly one character with any lowercase English letter so that the resulting
# string is not a palindrome and that it is the lexicographically smallest one
# possible.
# 
# Return the resulting string. If there is no way to replace a character to make
# it not a palindrome, return an empty string.
# 
# A string a is lexicographically smaller than a string b (of the same length) if
# in the first position where a and b differ, a has a character strictly smaller
# than the corresponding character in b. For example, "abcc" is lexicographically
# smaller than "abcd" because the first position they differ is at the fourth
# character, and 'c' is smaller than 'd'.
# 
# Example 1:
# 
# Input: palindrome = "abccba"
# Output: "aaccba"
# 
# Explanation: There are many ways to make "abccba" not a palindrome, such as
# "zbccba", "aaccba", and "abacba".
# Of all the ways, "aaccba" is the lexicographically smallest.
# 
# Example 2:
# 
# Input: palindrome = "a"
# Output: ""
# 
# Explanation: There is no way to replace a single character to make "a" not a
# palindrome, so return an empty string.
# 
# 
# Constraints:
#         1 <= palindrome.length <= 1000
#         palindrome consists of only lowercase English letters.


# Solution: https://algo.monster/liteproblems/1328
# Credit: AlgoMonster
def break_palindrome(palindrome):
    n = len(palindrome)
    
    # Single character palindrome cannot be broken
    if n == 1:
        return ""
    
    # Convert string to list for character modification
    chars = list(palindrome)
    
    # Try to find the first non-'a' character in the first half
    # We only check the first half because it's a palindrome
    i = 0
    while i < n // 2 and chars[i] == 'a':
        i += 1
    
    if i == n // 2:
        # All characters in the first half are 'a'
        # Change the last character to 'b' to get lexicographically smallest result
        chars[-1] = 'b'
    else:
        # Found a non-'a' character in the first half
        # Change it to 'a' to get lexicographically smallest result
        chars[i] = 'a'
    
    # Convert list back to string and return
    return "".join(chars)
    # Time: O(n)
    # Space: O(n)


def main():
    result = break_palindrome(palindrome = "abccba")
    print(result) # "aaccba"

    result = break_palindrome(palindrome = "a")
    print(result) # ""

if __name__ == "__main__":
    main()
