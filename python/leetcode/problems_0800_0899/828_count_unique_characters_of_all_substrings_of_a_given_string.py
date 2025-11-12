# ----------------------------------------------------------------
# 828. Count Unique Characters of All Substrings of a Given String
# ----------------------------------------------------------------

# Problem: https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string
#
# Let's define a function countUniqueChars(s) that returns the number of unique
# characters in s.
#         
#   * For example, calling countUniqueChars(s) if s = "LEETCODE" then "L",
#     "T", "C", "O", "D" are the unique characters since they appear only once in s,
#     therefore countUniqueChars(s) = 5.
# 
# Given a string s, return the sum of countUniqueChars(t) where t is a substring
# of s. The test cases are generated such that the answer fits in a 32-bit
# integer.
# 
# Notice that some substrings can be repeated so in this case you have to count
# the repeated ones too.
# 
# Example 1:
# 
# Input: s = "ABC"
# Output: 10
# 
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Every substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
# 
# Example 2:
# 
# Input: s = "ABA"
# Output: 8
# 
# Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
# 
# Example 3:
# Input: s = "LEETCODE"
# Output: 92
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s consists of uppercase English letters only.

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/828
# Credit: AlgoMonster
def unique_letter_string(s):
    # Dictionary to store all positions where each character appears
    char_positions = defaultdict(list)
    
    # Record the index position for each character in the string
    for index, char in enumerate(s):
        char_positions[char].append(index)
    
    total_count = 0
    
    # For each unique character, calculate its contribution to all substrings
    for positions in char_positions.values():
        # Add boundary markers: -1 at start and len(s) at end
        # This helps calculate the range where each occurrence is unique
        positions_with_bounds = [-1] + positions + [len(s)]
        
        # For each occurrence of the character, calculate how many substrings
        # contain this occurrence as the unique instance of that character
        for i in range(1, len(positions_with_bounds) - 1):
            # Left distance: from previous occurrence (or start boundary)
            left_distance = positions_with_bounds[i] - positions_with_bounds[i - 1]
            # Right distance: to next occurrence (or end boundary)
            right_distance = positions_with_bounds[i + 1] - positions_with_bounds[i]
            # Total substrings where this character occurrence is unique
            total_count += left_distance * right_distance
    
    return total_count
    # Time: O(n)
    # Space: O(n)


def main():
    result = unique_letter_string(s = "ABC")
    print(result) # 10

    result = unique_letter_string(s = "ABA")
    print(result) # 8

    result = unique_letter_string(s = "LEETCODE")
    print(result) # 92

if __name__ == "__main__":
    main()
