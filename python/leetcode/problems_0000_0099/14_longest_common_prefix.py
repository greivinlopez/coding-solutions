# -------------------------
# 14. Longest Common Prefix
# -------------------------

# Problem: https://leetcode.com/problems/longest-common-prefix
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# Example 2:
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# 
# Explanation: There is no common prefix among the input strings.
# 
# 
# Constraints:
#         1 <= strs.length <= 200
#         0 <= strs[i].length <= 200
#         strs[i] consists of only lowercase English letters if it is non-empty.

# Solution: https://youtu.be/8C6F8_nM0qs
# Credit: Navdeep Singh founder of NeetCode 
def longest_common_prefix(strs):
    min_length = float('inf')

    for s in strs:
        if len(s) < min_length:
            min_length = len(s)
    
    i = 0
    while i < min_length:
        for s in strs:
            if s[i] != strs[0][i]:
                return s[:i]
        i += 1
    
    return strs[0][:i]
    # Time: O(m * n)
    # Space: O(1)
    # m = length of the shortest string
    # n = number of strings

# Solution: https://youtu.be/0sWShKIJoo4
# Credit: Greg Hogg
def longest_common_prefix_alt(strs):
    for i in range(len(strs[0])):
        for s in strs:
            if i >= len(s) or s[i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]
    # Time: O(s)
    # Space: O(m)
    # s = total number of characters in all strings
    # m = length of the first string

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def longest_common_prefix_alt_2(strs):
    if len(strs) == 0 or strs == None:
        return ""
    prefix = strs[0]
    for s in strs:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix
    # Time: O(s)
    # Space: O(1)
    # s = total number of characters in all strings

def main():
    result = longest_common_prefix_alt(["flower","flow","flight"]) # "fl"
    print(result)
    result = longest_common_prefix_alt(["dog","racecar","car"]) # ""
    print(result)

if __name__ == "__main__":
    main()