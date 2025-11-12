# --------------------------------------------
# 424. Longest Repeating Character Replacement
# --------------------------------------------

# Problem: https://leetcode.com/problems/longest-repeating-character-replacement/
# 
# You are given a string s and an integer k. You can choose any character of the 
# string and change it to any other uppercase English character. You can perform 
# this operation at most k times.
# 
# Return the length of the longest substring containing the same letter you can 
# get after performing the above operations.
# 
#  
# Example 1:
# 
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# 
# 
# Example 2:
# 
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
# 
#  
# Constraints:
# 
# 	1 <= s.length <= 10^5
# 	s consists of only uppercase English letters.
# 	0 <= k <= s.length


# Solution: https://youtu.be/gqXU1UyA8pk
# Credit: Navdeep Singh founder of NeetCode
def character_replacement(s, k):
    count = {}
    res = l = maxf = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
    return res

# Solution: https://youtu.be/tkNWKvxI3mU
# Credit: Greg Hogg
# Same Solution
def character_replacement_alt(s, k):
    longest = 0
    l = 0
    counts = [0] * 26

    for r in range(len(s)):
        counts[ord(s[r]) - 65] += 1

        while (r - l + 1) - max(counts) > k:
            counts[ord(s[l]) - 65] -= 1
            l += 1

        longest = max(longest, (r - l + 1))

    return longest
    # Time: O(n)
    # Space: O(1)

def main():
    result = character_replacement(s = "ABAB", k = 2)
    print(result) # 4

    result = character_replacement(s = "AABABBA", k = 1)
    print(result) # 4

if __name__ == "__main__":
    main()
