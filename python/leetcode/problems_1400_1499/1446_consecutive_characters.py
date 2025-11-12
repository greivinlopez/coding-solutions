# ----------------------------
# 1446. Consecutive Characters
# ----------------------------

# Problem: https://leetcode.com/problems/consecutive-characters
#
# The power of the string is the maximum length of a non-empty substring that
# contains only one unique character.
# 
# Given a string s, return the power of s.
# 
# Example 1:
# 
# Input: s = "leetcode"
# Output: 2
# 
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# 
# Example 2:
# 
# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# 
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
# 
# 
# Constraints:
#         1 <= s.length <= 500
#         s consists of only lowercase English letters.


# Solution: https://algo.monster/liteproblems/1446
# Credit: AlgoMonster
def max_power(s):
    # Initialize the maximum length and current streak counter
    max_length = 1
    current_streak = 1
    
    # Iterate through consecutive character pairs in the string
    for i in range(len(s) - 1):
        # Check if current character equals the next character
        if s[i] == s[i + 1]:
            # Increment the current streak counter
            current_streak += 1
            # Update maximum length if current streak is longer
            max_length = max(max_length, current_streak)
        else:
            # Reset streak counter when characters differ
            current_streak = 1
    
    return max_length
    # Time: O(n)
    # Space: O(1)


def main():
    result = max_power(s = "leetcode")
    print(result) # 2

    result = max_power(s = "abbcccddddeeeeedcba")
    print(result) # 5

if __name__ == "__main__":
    main()
