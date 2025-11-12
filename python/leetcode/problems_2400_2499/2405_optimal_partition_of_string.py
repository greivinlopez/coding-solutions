# --------------------------------
# 2405. Optimal Partition Of String
# --------------------------------

# Problem: https://leetcode.com/problems/optimal-partition-of-string
#
# Given a string s, partition the string into one or more substrings such that the
# characters in each substring are unique. That is, no letter appears in a single
# substring more than once.
# 
# Return the minimum number of substrings in such a partition.
# 
# Note that each character should belong to exactly one substring in a partition.
# 
# Example 1:
# 
# Input: s = "abacaba"
# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.
# 
# Example 2:
# 
# Input: s = "ssssss"
# Output: 6
# Explanation:
# The only valid partition is ("s","s","s","s","s","s").
# 
# 
# Constraints:
#         1 <= s.length <= 10^5
#         s consists of only English lowercase letters.


# Solution: https://youtu.be/CKZPdiXiQf0
# Credit: Navdeep Singh founder of NeetCode
def partition_string(s):
    c = 0
    res=set()
    for i in s:
        if i in res:
            c = c + 1
            res=set()
        res.add(i)
    return c + 1


def main():
    result = partition_string("abacaba")
    print(result) # 4

    result = partition_string("ssssss")
    print(result) # 6

if __name__ == "__main__":
    main()
