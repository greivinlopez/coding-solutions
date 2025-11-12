# --------------------------------------------------
# 2516. Take K of Each Character From Left and Right
# --------------------------------------------------

# Problem: https://leetcode.com/problems/take-k-of-each-character-from-left-and-right
#
# You are given a string s consisting of the characters 'a', 'b', and 'c' and a
# non-negative integer k. Each minute, you may take either the leftmost character
# of s, or the rightmost character of s.
# 
# Return the minimum number of minutes needed for you to take at least k of each
# character, or return -1 if it is not possible to take k of each character.
# 
# Example 1:
# 
# Input: s = "aabaaaacaabc", k = 2
# Output: 8
# 
# Explanation:
# Take three characters from the left of s. You now have two 'a' characters, and
# one 'b' character.
# Take five characters from the right of s. You now have four 'a' characters, two
# 'b' characters, and two 'c' characters.
# A total of 3 + 5 = 8 minutes is needed.
# It can be proven that 8 is the minimum number of minutes needed.
# 
# Example 2:
# 
# Input: s = "a", k = 1
# Output: -1
# 
# Explanation: It is not possible to take one 'b' or 'c' so return -1.
# 
# 
# Constraints:
#         1 <= s.length <= 10^5
#         s consists of only the letters 'a', 'b', and 'c'.
#         0 <= k <= s.length


# Solution: https://youtu.be/QzcxeJZByNM
# Credit: Navdeep Singh founder of NeetCode
def take_characters(s, k):
    # Total counts
    count = [0, 0, 0]
    for c in s:
        count[ord(c) - ord("a")] += 1
    
    if min(count) < k:
        return -1
    
    # Sliding Window
    res = float("inf")
    l = 0
    for r in range(len(s)):
        count[ord(s[r]) - ord("a")] -= 1
        
        while min(count) < k:
            count[ord(s[l]) - ord("a")] += 1
            l += 1
        
        res = min(res, len(s) - (r - l + 1))
    return res
    # Time: O(n)
    # Space: O(1)


def main():
    result = take_characters(s = "aabaaaacaabc", k = 2)
    print(result) # 8

    result = take_characters(s = "a", k = 1)
    print(result) # -1

if __name__ == "__main__":
    main()
