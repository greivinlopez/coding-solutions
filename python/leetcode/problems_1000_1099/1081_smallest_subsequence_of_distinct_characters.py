# -------------------------------------------------
# 1081. Smallest Subsequence of Distinct Characters
# -------------------------------------------------

# Problem: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters
#
# Given a string s, return the lexicographically smallest subsequence of s that
# contains all the distinct characters of s exactly once.
# 
# Example 1:
# 
# Input: s = "bcabc"
# Output: "abc"
# 
# Example 2:
# 
# Input: s = "cbacdcbc"
# Output: "acdb"
# 
# 
# Constraints:
#         1 <= s.length <= 1000
#         s consists of lowercase English letters.
# 
# Note: This question is the same as 316: 
# https://leetcode.com/problems/remove-duplicate-letters/


# Solution: https://algo.monster/liteproblems/1081
# Credit: AlgoMonster
def smallest_subsequence(s):
    # Create a dictionary to store the last occurrence index of each character
    last_occurrence = {char: index for index, char in enumerate(s)}
    
    # Stack to build the result string
    stack = []
    
    # Set to track which characters are already in the stack
    visited = set()
    
    # Iterate through each character in the string
    for index, char in enumerate(s):
        # Skip if character is already in our result
        if char in visited:
            continue
        
        # Remove characters from stack that are:
        # 1. Greater than current character (lexicographically)
        # 2. Will appear again later in the string
        while stack and stack[-1] > char and last_occurrence[stack[-1]] > index:
            removed_char = stack.pop()
            visited.remove(removed_char)
        
        # Add current character to stack and mark as visited
        stack.append(char)
        visited.add(char)
    
    # Join the stack to form the final result string
    return "".join(stack)
    # Time: O(n)
    # Space: O(1)


def main():
    result = smallest_subsequence(s = "bcabc")
    print(result) # "abc"

    result = smallest_subsequence(s = "cbacdcbc")
    print(result) # "acdb"

if __name__ == "__main__":
    main()
