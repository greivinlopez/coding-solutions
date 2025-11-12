# -------------------------
# 1417. Reformat The String
# -------------------------

# Problem: https://leetcode.com/problems/reformat-the-string
#
# You are given an alphanumeric string s. (Alphanumeric string is a string
# consisting of lowercase English letters and digits).
# 
# You have to find a permutation of the string where no letter is followed by
# another letter and no digit is followed by another digit. That is, no two
# adjacent characters have the same type.
# 
# Return the reformatted string or return an empty string if it is impossible to
# reformat the string.
# 
# Example 1:
# 
# Input: s = "a0b1c2"
# Output: "0a1b2c"
# 
# Explanation: No two adjacent characters have the same type in "0a1b2c".
# "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
# 
# Example 2:
# 
# Input: s = "leetcode"
# Output: ""
# 
# Explanation: "leetcode" has only characters so we cannot separate them by
# digits.
# 
# Example 3:
# 
# Input: s = "1229857369"
# Output: ""
# 
# Explanation: "1229857369" has only digits so we cannot separate them by
# characters.
# 
# 
# Constraints:
#         1 <= s.length <= 500
#         s consists of only lowercase English letters and/or digits.


# Solution: https://algo.monster/liteproblems/1417
# Credit: AlgoMonster
def reformat(s):
    # Separate letters and digits into two lists
    letters = [char for char in s if char.isalpha()]
    digits = [char for char in s if char.isdigit()]
    
    # Check if valid alternating pattern is possible
    # The difference in lengths cannot exceed 1
    if abs(len(letters) - len(digits)) > 1:
        return ''
    
    # Ensure the longer list is first for proper alternation
    # This simplifies the alternating logic
    if len(letters) < len(digits):
        letters, digits = digits, letters
    
    # Build the result by alternating between the two lists
    result = []
    for first_char, second_char in zip(letters, digits):
        result.append(first_char + second_char)
    
    # If one list is longer, append the remaining character
    if len(letters) > len(digits):
        result.append(letters[-1])
    
    # Join all parts into the final string
    return ''.join(result)
    # Time: O(n)
    # Space: O(n)


def main():
    result = reformat(s = "a0b1c2")
    print(result) # "0a1b2c"

    result = reformat(s = "leetcode")
    print(result) # ""

    result = reformat(s = "1229857369")
    print(result) # ""

if __name__ == "__main__":
    main()
