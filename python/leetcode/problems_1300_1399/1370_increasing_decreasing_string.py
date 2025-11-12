# ----------------------------------
# 1370. Increasing Decreasing String
# ----------------------------------

# Problem: https://leetcode.com/problems/increasing-decreasing-string
#
# You are given a string s. Reorder the string using the following algorithm:
#         
#   1. Remove the smallest character from s and append it to the result.
#   2. Remove the smallest character from s that is greater than the last
#      appended character, and append it to the result.
#   3. Repeat step 2 until no more characters can be removed.
#   4. Remove the largest character from s and append it to the result.
#   5. Remove the largest character from s that is smaller than the last
#      appended character, and append it to the result.
#   6. Repeat step 5 until no more characters can be removed.
#   7. Repeat steps 1 through 6 until all characters from s have been removed.
# 
# If the smallest or largest character appears more than once, you may choose any
# occurrence to append to the result.
# 
# Return the resulting string after reordering s using this algorithm.
# 
# Example 1:
# 
# Input: s = "aaaabbbbcccc"
# Output: "abccbaabccba"
# 
# Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
# After steps 4, 5 and 6 of the first iteration, result = "abccba"
# First iteration is done. Now s = "aabbcc" and we go back to step 1
# After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
# After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
# 
# Example 2:
# 
# Input: s = "rat"
# Output: "art"
# 
# Explanation: The word "rat" becomes "art" after re-ordering it with the
# mentioned algorithm.
# 
# 
# Constraints:
#         1 <= s.length <= 500
#         s consists of only lowercase English letters.

from collections import Counter
from string import ascii_lowercase

# Solution: https://algo.monster/liteproblems/1370
# Credit: AlgoMonster
def sort_string(s):
    # Count frequency of each character in the input string
    char_count = Counter(s)
    
    # Create a pattern: a-z followed by z-a for alternating ascending/descending order
    pattern = ascii_lowercase + ascii_lowercase[::-1]
    
    # Result list to build the output string
    result = []
    
    # Continue until we've used all characters from the original string
    while len(result) < len(s):
        # Iterate through the pattern (a-z, then z-a)
        for char in pattern:
            # If this character is still available
            if char_count[char] > 0:
                # Add it to the result
                result.append(char)
                # Decrease its count
                char_count[char] -= 1
    
    # Join the result list into a string and return
    return "".join(result)
    # Time: O(n)
    # Space: O(1)


def main():
    result = sort_string(s = "aaaabbbbcccc")
    print(result) # "abccbaabccba"

    result = sort_string(s = "rat")
    print(result) # "art"

if __name__ == "__main__":
    main()
