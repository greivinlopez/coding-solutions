# --------------------------
# 761. Special Binary String
# --------------------------

# Problem: https://leetcode.com/problems/special-binary-string
#
# Special binary strings are binary strings with the following two properties:
#         
#   * The number of 0's is equal to the number of 1's.
#   * Every prefix of the binary string has at least as many 1's as 0's.
# 
# You are given a special binary string s.
# 
# A move consists of choosing two consecutive, non-empty, special substrings of s,
# and swapping them. Two strings are consecutive if the last character of the
# first string is exactly one index before the first character of the second
# string.
# 
# Return the lexicographically largest resulting string possible after applying
# the mentioned operations on the string.
# 
# Example 1:
# 
# Input: s = "11011000"
# Output: "11100100"
# 
# Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are
# swapped.
# This is the lexicographically largest string possible after some number of
# swaps.
# 
# Example 2:
# 
# Input: s = "10"
# Output: "10"
# 
# 
# Constraints:
#         1 <= s.length <= 50
#         s[i] is either '0' or '1'.
#         s is a special binary string.


# Solution: https://algo.monster/liteproblems/761
# Credit: AlgoMonster
def make_largest_special(s):
    # Base case: empty string returns empty
    if not s:
        return ''
    
    # List to store special substrings found at the current level
    substrings = []
    
    # Counter to track balance of '1's and '0's
    balance = 0
    
    # Start index of current special substring
    start = 0
    
    # Iterate through the string to find special substrings
    for i in range(len(s)):
        # Increment balance for '1', decrement for '0'
        balance += 1 if s[i] == '1' else -1
        
        # When balance returns to 0, we've found a complete special substring
        if balance == 0:
            # Recursively process the inner content (excluding first '1' and last '0')
            # Then wrap it with '1' at start and '0' at end
            inner_content = make_largest_special(s[start + 1:i])
            special_substring = '1' + inner_content + '0'
            substrings.append(special_substring)
            
            # Move start pointer to begin searching for next special substring
            start = i + 1
    
    # Sort all special substrings in descending order (lexicographically largest first)
    substrings.sort(reverse=True)
    
    # Concatenate all sorted substrings to form the final result
    return ''.join(substrings)
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = make_largest_special(s = "11011000")
    print(result) # "11100100"

    result = make_largest_special(s = "10")
    print(result) # "10"

if __name__ == "__main__":
    main()
