# -----------------------------------------------
# 1234. Replace the Substring for Balanced String
# -----------------------------------------------

# Problem: https://leetcode.com/problems/replace-the-substring-for-balanced-string
#
# You are given a string s of length n containing only four kinds of characters:
# 'Q', 'W', 'E', and 'R'.
# 
# A string is said to be balanced if each of its characters appears n / 4 times
# where n is the length of the string.
# 
# Return the minimum length of the substring that can be replaced with any other
# string of the same length to make s balanced. If s is already balanced, return
# 0.
# 
# Example 1:
# 
# Input: s = "QWER"
# Output: 0
# 
# Explanation: s is already balanced.
# 
# Example 2:
# 
# Input: s = "QQWE"
# Output: 1
# 
# Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is
# balanced.
# 
# Example 3:
# 
# Input: s = "QQQW"
# Output: 2
# 
# Explanation: We can replace the first "QQ" to "ER".
# 
# 
# Constraints:
#         n == s.length
#         4 <= n <= 10⁵
#         n is a multiple of 4.
#         s contains only 'Q', 'W', 'E', and 'R'.

from collections import Counter

# Solution: https://algo.monster/liteproblems/1234
# Credit: AlgoMonster
def balanced_string(s):
    # Count frequency of each character in the string
    char_count = Counter(s)
    n = len(s)
    target_count = n // 4  # Each character should appear exactly n/4 times in a balanced string
    
    # If string is already balanced, no replacement needed
    if all(count <= target_count for count in char_count.values()):
        return 0
    
    min_window_size = n  # Initialize minimum window size to string length
    left = 0  # Left pointer of sliding window
    
    # Iterate through string with right pointer
    for right, char in enumerate(s):
        # Remove current character from count (considering it part of window to replace)
        char_count[char] -= 1
        
        # Try to shrink window from left while maintaining valid state
        # Valid state: remaining characters outside window don't exceed target_count
        while left <= right and all(count <= target_count for count in char_count.values()):
            # Update minimum window size
            min_window_size = min(min_window_size, right - left + 1)
            # Add back the leftmost character (removing it from replacement window)
            char_count[s[left]] += 1
            left += 1
    
    return min_window_size
    # Time: O(n)
    # Space: O(1)


def main():
    result = balanced_string(s = "QWER")
    print(result) # 0

    result = balanced_string(s = "QQWE")
    print(result) # 1

    result = balanced_string(s = "QQQW")
    print(result) # 2

if __name__ == "__main__":
    main()
