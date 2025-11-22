# ---------------------------------------------------------------------
# 1585. Check If String Is Transformable With Substring Sort Operations
# ---------------------------------------------------------------------

# Problem: https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations
#
# Given two strings s and t, transform string s into string t using the following
# operation any number of times:
#         
#   * Choose a non-empty substring in s and sort it in place so the characters
#     are in ascending order.
#       * For example, applying the operation on the underlined substring
#         in "14234" results in "12344".
# 
# Return true if it is possible to transform s into t. Otherwise, return false.
# 
# A substring is a contiguous sequence of characters within a string.
# 
# Example 1:
# 
# Input: s = "84532", t = "34852"
# Output: true
# 
# Explanation: You can transform s into t using the following sort operations:
# "84532" (from index 2 to 3) -> "84352"
# "84352" (from index 0 to 2) -> "34852"
# 
# Example 2:
# 
# Input: s = "34521", t = "23415"
# Output: true
# 
# Explanation: You can transform s into t using the following sort operations:
# "34521" -> "23451"
# "23451" -> "23415"
# 
# Example 3:
# 
# Input: s = "12345", t = "12435"
# Output: false
# 
# 
# Constraints:
#         s.length == t.length
#         1 <= s.length <= 10⁵
#         s and t consist of only digits.

from collections import defaultdict, deque

# Solution: https://algo.monster/liteproblems/1585
# Credit: AlgoMonster
def is_transformable(s, t):
    # Create a dictionary to store positions of each digit in string s
    # Key: digit (0-9), Value: deque of positions where this digit appears
    digit_positions = defaultdict(deque)
    
    # Populate the position queues for each digit in string s
    for index, char in enumerate(s):
        digit = int(char)
        digit_positions[digit].append(index)
    
    # Process each character in target string t
    for char in t:
        target_digit = int(char)
        
        # Check if target digit exists in remaining positions
        if not digit_positions[target_digit]:
            return False
        
        # Get the leftmost position of the target digit
        target_position = digit_positions[target_digit][0]
        
        # Check if any smaller digit appears before the target digit's position
        # This would block the transformation (smaller digits can't move right past larger ones)
        for smaller_digit in range(target_digit):
            if digit_positions[smaller_digit] and digit_positions[smaller_digit][0] < target_position:
                return False
        
        # Remove the used position of the target digit
        digit_positions[target_digit].popleft()
    
    # All characters successfully matched
    return True
    # Time: O(n)
    # Space: O(n)


def main():
    result = is_transformable(s = "84532", t = "34852")
    print(result) # True

    result = is_transformable(s = "34521", t = "23415")
    print(result) # True

    result = is_transformable(s = "12345", t = "12435")
    print(result) # False

if __name__ == "__main__":
    main()
