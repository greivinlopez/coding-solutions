# -------------------------------------------------------
# 1897. Redistribute Characters to Make All Strings Equal
# -------------------------------------------------------

# Problem: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal
#
# You are given an array of strings words (0-indexed).
# 
# In one operation, pick two distinct indices i and j, where words[i] is a non-
# empty string, and move any character from words[i] to any position in words[j].
# 
# Return true if you can make every string in words equal using any number of
# operations, and false otherwise.
# 
# Example 1:
# 
# Input: words = ["abc","aabc","bc"]
# Output: true
# 
# Explanation: Move the first 'a' in words[1] to the front of words[2],
# to make words[1] = "abc" and words[2] = "abc".
# All the strings are now equal to "abc", so return true.
# 
# Example 2:
# 
# Input: words = ["ab","a"]
# Output: false
# 
# Explanation: It is impossible to make all the strings equal using the operation.
# 
# 
# Constraints:
#         1 <= words.length <= 100
#         1 <= words[i].length <= 100
#         words[i] consists of lowercase English letters.

from collections import defaultdict

# Solution: https://youtu.be/a3SmUiimBi8
# Credit: Navdeep Singh founder of NeetCode
def make_equal(words):
    char_cnt = defaultdict(int)

    for w in words:
        for c in w:
            char_cnt[c] += 1

    for c in char_cnt:
        if char_cnt[c] % len(words) != 0:
            return False

    return True
    # Time: O(n)
    # Space: O(1)


def main():
    result = make_equal(["abc","aabc","bc"])
    print(result) # True

    result = make_equal(["ab","a"])
    print(result) # False

if __name__ == "__main__":
    main()
