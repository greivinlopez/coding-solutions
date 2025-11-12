# ------------------------------------
# 522. Longest Uncommon Subsequence II
# ------------------------------------

# Problem: https://leetcode.com/problems/longest-uncommon-subsequence-ii
#
# Given an array of strings strs, return the length of the longest uncommon
# subsequence between them. If the longest uncommon subsequence does not exist,
# return -1.
# 
# An uncommon subsequence between an array of strings is a string that is a
# subsequence of one string but not the others.
# 
# A subsequence of a string s is a string that can be obtained after deleting any
# number of characters from s.
#         
#   * For example, "abc" is a subsequence of "aebdc" because you can delete
#     the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc"
#     include "aebdc", "aeb", and "" (empty string).
# 
# Example 1:
# 
# Input: strs = ["aba","cdc","eae"]
# Output: 3
# 
# Example 2:
# 
# Input: strs = ["aaa","aaa","aa"]
# Output: -1
# 
# 
# Constraints:
#         2 <= strs.length <= 50
#         1 <= strs[i].length <= 10
#         strs[i] consists of lowercase English letters.


# Solution: https://algo.monster/liteproblems/522
# Credit: AlgoMonster
def find_l_u_s_length(strs):
    # Helper function to check if string b is a subsequence of string a.
    def is_subsequence(a, b):
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                j += 1    # Move to the next character in b if there's a match.
            i += 1        # Move to the next character in a.
        return j == len(b)  # Check if all characters in b are matched.

    num_strings = len(strs)
    longest_unique_length = -1  # Initialize with -1 as we may not find any unique strings.

    # Iterate over each string in 'strs'.
    for i in range(num_strings):
        j = 0
        # Compare the selected string with all other strings.
        while j < num_strings:
            # Skip if comparing the string with itself or if 'strs[j]' is not a subsequence of 'strs[i]'.
            if i == j or not is_subsequence(strs[j], strs[i]):
                j += 1  # Move to the next string for comparison.
            else:
                break  # 'strs[i]' is a subsequence of 'strs[j]', hence not unique.
        # If we reached the end after comparisons, 'strs[i]' is unique.
        if j == num_strings:
            # Update the maximum length with the length of this unique string.
            longest_unique_length = max(longest_unique_length, len(strs[i]))
    
    # Return the length of the longest uncommon subsequence.
    return longest_unique_length
    # Time: O(n² * m)
    # Space: O(1)


def main():
    result = find_l_u_s_length(["aba","cdc","eae"])
    print(result) # 3

    result = find_l_u_s_length(["aaa","aaa","aa"])
    print(result) # -1

if __name__ == "__main__":
    main()
