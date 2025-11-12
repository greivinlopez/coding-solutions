# --------------------------------------------------------------------
# 1239. Maximum Length Of A Concatenated String With Unique Characters
# --------------------------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters
#
# You are given an array of strings arr. A string s is formed by the concatenation
# of a subsequence of arr that has unique characters.
# 
# Return the maximum possible length of s.
# 
# A subsequence is an array that can be derived from another array by deleting
# some or no elements without changing the order of the remaining elements.
# 
# Example 1:
# 
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.
# 
# Example 2:
# 
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers")
# and "acters" ("act" + "ers").
# 
# Example 3:
# 
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.
# 
# 
# Constraints:
#         1 <= arr.length <= 16
#         1 <= arr[i].length <= 26
#         arr[i] contains only lowercase English letters.

from collections import Counter

# Solution: https://youtu.be/d4SPuvkaeoo
# Credit: Navdeep Singh founder of NeetCode
def max_length(arr):
    charSet = set()

    def overlap(charSet, s):
        c = Counter(charSet) + Counter(s)
        return max(c.values()) > 1
        # prev = set()
        # for c in s:
        #     if c in charSet or c in prev:
        #         return True
        #     prev.add(c)
        # return False

    def backtrack(i):
        if i == len(arr):
            return len(charSet)
        res = 0
        if not overlap(charSet, arr[i]):
            for c in arr[i]:
                charSet.add(c)
            res = backtrack(i + 1)
            for c in arr[i]:
                charSet.remove(c)
        return max(res, backtrack(i + 1))  # dont concatenate arr[i]

    return backtrack(0)


def main():
    result = max_length(["un","iq","ue"])
    print(result) # 4

    result = max_length(["cha","r","act","ers"])
    print(result) # 6

    result = max_length(["abcdefghijklmnopqrstuvwxyz"])
    print(result) # 26

if __name__ == "__main__":
    main()
