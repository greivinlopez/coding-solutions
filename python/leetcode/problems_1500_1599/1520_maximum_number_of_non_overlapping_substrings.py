# --------------------------------------------------
# 1520. Maximum Number of Non-Overlapping Substrings
# --------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings
#
# Given a string s of lowercase letters, you need to find the maximum number of
# non-empty substrings of s that meet the following conditions:
#         
#   1. The substrings do not overlap, that is for any two substrings s[i..j]
#      and s[x..y], either j < x or i > y is true.
#   2. A substring that contains a certain character c must also contain all
#      occurrences of c.
# 
# Find the maximum number of substrings that meet the above conditions. If there
# are multiple solutions with the same number of substrings, return the one with
# minimum total length. It can be shown that there exists a unique solution of
# minimum total length.
# 
# Notice that you can return the substrings in any order.
# 
# Example 1:
# 
# Input: s = "adefaddaccc"
# Output: ["e","f","ccc"]
# Explanation: The following are all the possible substrings that meet the
# conditions:
# [
#   "adefaddaccc"
#   "adefadda",
#   "ef",
#   "e",
#   "f",
#   "ccc",
# ]
# If we choose the first string, we cannot choose anything else and we'd get only
# 1. If we choose "adefadda", we are left with "ccc" which is the only one that
# doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal
# to choose "ef" since it can be split into two. Therefore, the optimal way is to
# choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the
# same number of substrings exist.
# 
# Example 2:
# 
# Input: s = "abbaccd"
# Output: ["d","bb","cc"]
# 
# Explanation: Notice that while the set of substrings ["d","abba","cc"] also has
# length 3, it's considered incorrect since it has larger total length.
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s contains only lowercase English letters.


# Solution: https://algo.monster/liteproblems/1520
# Credit: AlgoMonster
def max_num_of_substrings(s):
    n = len(s)
    left = [n] * 26
    right = [0] * 26

    # Record the leftmost and rightmost index for each character.
    for i in range(n):
        index = ord(s[i]) - ord('a')
        left[index] = min(left[index], i)
        right[index] = i

    res = []
    r = -1

    # For each character (if it's the leftmost occurrence),
    # check if it forms a valid solution.
    for i in range(n):
        if i != left[ord(s[i]) - ord('a')]:
            continue
        new_r = right[ord(s[i]) - ord('a')]
        j = i + 1
        while (j < new_r + 1) :
            if left[ord(s[j]) - ord('a')] < i:
                print
                new_r = n
                break
            new_r = max(new_r, right[ord(s[j]) - ord('a')])
            j = j + 1
        if new_r < n and (i > r or new_r < right[ord(s[r]) - ord('a')]):
            if i > r:
                res.append(s[i:new_r + 1])
            else:
                res[-1] = s[i:new_r + 1]
            r = new_r

    return res
    # Time: O(n²)
    # Space: O(n)


def main():
    result = max_num_of_substrings(s = "adefaddaccc")
    print(result) # ['e', 'f', 'ccc']

    result = max_num_of_substrings(s = "abbaccd")
    print(result) # ['bb', 'cc', 'd']

if __name__ == "__main__":
    main()
