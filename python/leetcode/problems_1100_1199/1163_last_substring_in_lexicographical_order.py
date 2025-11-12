# ---------------------------------------------
# 1163. Last Substring in Lexicographical Order
# ---------------------------------------------

# Problem: https://leetcode.com/problems/last-substring-in-lexicographical-order
#
# Given a string s, return the last substring of s in lexicographical order.
# 
# Example 1:
# 
# Input: s = "abab"
# Output: "bab"
# 
# Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"].
# The lexicographically maximum substring is "bab".
# 
# Example 2:
# 
# Input: s = "leetcode"
# Output: "tcode"
# 
# 
# Constraints:
#         1 <= s.length <= 4 * 10⁵
#         s contains only lowercase English letters.


# Solution: https://algo.monster/liteproblems/1163
# Credit: AlgoMonster
def last_substring(s):
    # Initialize two pointers for comparing potential starting positions
    left_start = 0   # First candidate starting position
    right_start = 1  # Second candidate starting position
    offset = 0       # Current comparison offset from both starting positions
    
    # Continue until we've examined all necessary characters
    while right_start + offset < len(s):
        # Case 1: Characters at current offset are equal
        if s[left_start + offset] == s[right_start + offset]:
            # Move to next character for comparison
            offset += 1
            
        # Case 2: Left substring is smaller at current offset
        elif s[left_start + offset] < s[right_start + offset]:
            # Skip the entire left substring and its compared portion
            # The new left_start jumps past all compared characters
            left_start = left_start + offset + 1
            offset = 0  # Reset comparison offset
            
            # Ensure right_start is always ahead of left_start
            if left_start >= right_start:
                right_start = left_start + 1
                
        # Case 3: Right substring is smaller at current offset
        else:
            # Skip the entire right substring and its compared portion
            right_start = right_start + offset + 1
            offset = 0  # Reset comparison offset
    
    # Return the suffix starting from the optimal position
    return s[left_start:]
    # Time: O(n)
    # Space: O(1)


def main():
    result = last_substring(s = "abab")
    print(result) # "bab"

    result = last_substring(s = "leetcode")
    print(result) # "tcode"

if __name__ == "__main__":
    main()
