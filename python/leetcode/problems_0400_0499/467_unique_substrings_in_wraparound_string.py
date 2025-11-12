# -------------------------------------------
# 467. Unique Substrings in Wraparound String
# -------------------------------------------

# Problem: https://leetcode.com/problems/unique-substrings-in-wraparound-string
#
# We define the string base to be the infinite wraparound string of
# "abcdefghijklmnopqrstuvwxyz", so base will look like this:
# 
#       "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
# 
# Given a string s, return the number of unique non-empty substrings of s are
# present in base.
# 
# Example 1:
# 
# Input: s = "a"
# Output: 1
# 
# Explanation: Only the substring "a" of s is in base.
# 
# Example 2:
# 
# Input: s = "cac"
# Output: 2
# 
# Explanation: There are two substrings ("a", "c") of s in base.
# 
# Example 3:
# 
# Input: s = "zab"
# Output: 6
# 
# Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of
# s in base.
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s consists of lowercase English letters.

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/467
# Credit: AlgoMonster
def find_substring_in_wrapround_string(s):
    # Dictionary to store the maximum length of substring ending with each character
    max_length_ending_with = defaultdict(int)
    
    # Current consecutive substring length
    consecutive_length = 0
    
    for index, char in enumerate(s):
        # Check if current character follows the previous one in alphabetical order
        # (considering wraparound: 'z' -> 'a')
        if index > 0 and (ord(char) - ord(s[index - 1])) % 26 == 1:
            # Extend the current consecutive substring
            consecutive_length += 1
        else:
            # Start a new consecutive substring
            consecutive_length = 1
        
        # Update the maximum length of substring ending with current character
        # max_length_ending_with[char] = k means there are k unique substrings 
        # (of length 1 to k) ending with 'char' that are valid wrap-around substrings.
        max_length_ending_with[char] = max(max_length_ending_with[char], consecutive_length)
    
    # Sum all maximum lengths to get total unique substrings
    # Example: If max_length_ending_with['c'] is 3, it counts "c", "bc", and "abc".
    return sum(max_length_ending_with.values())
    # Time: O(n)
    # Space: O(1)


def main():
    result = find_substring_in_wrapround_string(s = "a")
    print(result) # True

    result = find_substring_in_wrapround_string(s = "cac")
    print(result) # True

    result = find_substring_in_wrapround_string(s = "zab")
    print(result) # False

if __name__ == "__main__":
    main()
