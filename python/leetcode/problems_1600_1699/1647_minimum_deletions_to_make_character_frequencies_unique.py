# ------------------------------------------------------------
# 1647. Minimum Deletions to Make Character Frequencies Unique
# ------------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique
#
# A string s is called good if there are no two different characters in s that
# have the same frequency.
# 
# Given a string s, return the minimum number of characters you need to delete to
# make s good.
# 
# The frequency of a character in a string is the number of times it appears in
# the string. For example, in the string "aab", the frequency of 'a' is 2, while
# the frequency of 'b' is 1.
# 
# Example 1:
# 
# Input: s = "aab"
# Output: 0
# 
# Explanation: s is already good.
# 
# Example 2:
# 
# Input: s = "aaabbbcc"
# Output: 2
# 
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string
# "aaabbc".
# 
# Example 3:
# 
# Input: s = "ceabaacb"
# Output: 2
# 
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end
# (i.e. frequency of 0 is ignored).
# 
# 
# Constraints:
#         1 <= s.length <= 10^5
#         s contains only lowercase English letters.

from collections import Counter

# Solution: https://youtu.be/h8AZEN49gTc
# Credit: Navdeep Singh founder of NeetCode
def min_deletions(s):
    count = Counter(s)
    used_freq = set()
    res = 0

    for c, freq in count.items():
        while freq > 0 and freq in used_freq:
            freq -= 1
            res += 1
        used_freq.add(freq)
    
    return res
    # Time: O(n) 
    # Space: O(n)


def main():
    result = min_deletions("aab")
    print(result) # 0

    result = min_deletions("aaabbbcc")
    print(result) # 2

    result = min_deletions("ceabaacb")
    print(result) # 2

if __name__ == "__main__":
    main()
