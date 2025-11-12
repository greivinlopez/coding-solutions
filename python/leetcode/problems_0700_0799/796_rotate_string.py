# ------------------
# 796. Rotate String
# ------------------

# Problem: https://leetcode.com/problems/rotate-string
#
# Given two strings s and goal, return true if and only if s can become goal after
# some number of shifts on s.
# 
# A shift on s consists of moving the leftmost character of s to the rightmost
# position.
#         
#   * For example, if s = "abcde", then it will be "bcdea" after one shift.
# 
# Example 1:
# 
# Input: s = "abcde", goal = "cdeab"
# Output: true
# 
# Example 2:
# 
# Input: s = "abcde", goal = "abced"
# Output: false
# 
# 
# Constraints:
#         1 <= s.length, goal.length <= 100
#         s and goal consist of lowercase English letters.


# Solution: https://algo.monster/liteproblems/796
# Credit: AlgoMonster
def rotate_string(s, goal):
    # First check if lengths are equal (necessary condition for rotation)
    # Then check if goal appears as a substring in the concatenated string s + s
    # Example: s = "abcde", s + s = "abcdeabcde"
    # All rotations like "cdeab", "deabc" etc. will be substrings of "abcdeabcde"
    return len(s) == len(goal) and goal in s + s


def main():
    result = rotate_string(s = "abcde", goal = "cdeab")
    print(result) # True

    result = rotate_string(s = "abcde", goal = "abced")
    print(result) # False

if __name__ == "__main__":
    main()
