# ------------------
# 859. Buddy Strings
# ------------------

# Problem: https://leetcode.com/problems/buddy-strings
#
# Given two strings s and goal, return true if you can swap two letters in s so
# the result is equal to goal, otherwise, return false.
# 
# Swapping letters is defined as taking two indices i and j (0-indexed) such that
# i != j and swapping the characters at s[i] and s[j].
#         
#   * For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
# 
# Example 1:
# 
# Input: s = "ab", goal = "ba"
# Output: true
# 
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal
# to goal.
# 
# Example 2:
# 
# Input: s = "ab", goal = "ab"
# Output: false
# 
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which
# results in "ba" != goal.
# 
# Example 3:
# 
# Input: s = "aa", goal = "aa"
# Output: true
# 
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal
# to goal.
# 
# 
# Constraints:
#         1 <= s.length, goal.length <= 2 * 10⁴
#         s and goal consist of lowercase letters.

from collections import Counter

# Solution: https://algo.monster/liteproblems/859
# Credit: AlgoMonster
def buddy_strings(s, goal):
    # Check if strings have the same length
    string_length = len(s)
    goal_length = len(goal)
    
    if string_length != goal_length:
        return False
    
    # Count character frequencies in both strings
    s_char_count = Counter(s)
    goal_char_count = Counter(goal)
    
    # If character frequencies don't match, strings can't be made equal
    if s_char_count != goal_char_count:
        return False
    
    # Count the number of positions where characters differ
    difference_count = sum(s[i] != goal[i] for i in range(string_length))
    
    # Two valid cases:
    # 1. Exactly 2 differences (swap those two positions)
    # 2. No differences but at least one duplicate character (swap two identical chars)
    return (difference_count == 2 or 
            (difference_count == 0 and any(count > 1 for count in s_char_count.values())))
    # Time: O(n)
    # Space: O(1), O(k) where k = 26.


def main():
    result = buddy_strings(s = "ab", goal = "ba")
    print(result) # True

    result = buddy_strings(s = "ab", goal = "ab")
    print(result) # False

    result = buddy_strings(s = "aa", goal = "aa")
    print(result) # True

if __name__ == "__main__":
    main()
