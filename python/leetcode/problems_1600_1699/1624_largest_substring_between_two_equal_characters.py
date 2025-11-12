# ----------------------------------------------------
# 1624. Largest Substring Between Two Equal Characters
# ----------------------------------------------------

# Problem: https://leetcode.com/problems/largest-substring-between-two-equal-characters
#
# Given a string s, return the length of the longest substring between two equal
# characters, excluding the two characters. If there is no such substring return
# -1.
# 
# A substring is a contiguous sequence of characters within a string.
# 
# Example 1:
# 
# Input: s = "aa"
# Output: 0
# 
# Explanation: The optimal substring here is an empty substring between the two
# 'a's.
# 
# Example 2:
# 
# Input: s = "abca"
# Output: 2
# 
# Explanation: The optimal substring here is "bc".
# 
# Example 3:
# 
# Input: s = "cbzxy"
# Output: -1
# 
# Explanation: There are no characters that appear twice in s.
# 
# 
# Constraints:
#         1 <= s.length <= 300
#         s contains only lowercase English letters.


# Solution: https://youtu.be/66b2V_rCuJw
# Credit: Navdeep Singh founder of NeetCode
def max_length_between_equal_characters(s):
    char_index = {}
    res = -1

    for i, c in enumerate(s):
        if c in char_index:
            res = max(res, i - char_index[c] - 1)
        else:
            char_index[c] = i
    
    return res
    # Time: O(n)
    # Space: O(k)


def main():
    result = max_length_between_equal_characters("aa")
    print(result) # 0

    result = max_length_between_equal_characters("abca")
    print(result) # 2

    result = max_length_between_equal_characters("cbzxy")
    print(result) # -1

if __name__ == "__main__":
    main()
