# -----------------------------------------
# 893. Groups of Special-Equivalent Strings
# -----------------------------------------

# Problem: https://leetcode.com/problems/groups-of-special-equivalent-strings
#
# You are given an array of strings of the same length words.
# 
# In one move, you can swap any two even indexed characters or any two odd indexed
# characters of a string words[i].
# 
# Two strings words[i] and words[j] are special-equivalent if after any number of
# moves, words[i] == words[j].
#         
#   * For example, words[i] = "zzxy" and words[j] = "xyzz" are special-
#     equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz".
# 
# A group of special-equivalent strings from words is a non-empty subset of words
# such that:
#         
#   * Every pair of strings in the group are special equivalent, and
#   * The group is the largest size possible (i.e., there is not a string
#     words[i] not in the group such that words[i] is special-equivalent to every
#     string in the group).
# 
# Return the number of groups of special-equivalent strings from words.
# 
# Example 1:
# 
# Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
# Output: 3
# 
# Explanation:
# One group is ["abcd", "cdab", "cbad"], since they are all pairwise special
# equivalent, and none of the other strings is all pairwise special equivalent to
# these.
# The other two groups are ["xyzz", "zzxy"] and ["zzyx"].
# Note that in particular, "zzxy" is not special equivalent to "zzyx".
# 
# Example 2:
# 
# Input: words = ["abc","acb","bac","bca","cab","cba"]
# Output: 3
# 
# 
# Constraints:
#         1 <= words.length <= 1000
#         1 <= words[i].length <= 20
#         words[i] consist of lowercase English letters.
#         All the strings are of the same length.


# Solution: https://algo.monster/liteproblems/893
# Credit: AlgoMonster
def num_special_equiv_groups(words):
    # Use a set to store unique special-equivalent group signatures
    unique_groups = {
        # For each word, create a signature by:
        # 1. Sorting characters at even indices (word[::2])
        # 2. Sorting characters at odd indices (word[1::2])
        # 3. Concatenating the two sorted strings
        # This signature will be identical for special-equivalent strings
        ''.join(sorted(word[::2]) + sorted(word[1::2])) 
        for word in words
    }
    
    # Return the count of unique special-equivalent groups
    return len(unique_groups)
    # Time: O(n * m * log(m))
    # Space: O(n * m)
    # n = the number of words
    # m = the average length of each word.


def main():
    result = num_special_equiv_groups(words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"])
    print(result) # 3

    result = num_special_equiv_groups(words = ["abc","acb","bac","bca","cab","cba"])
    print(result) # 3

if __name__ == "__main__":
    main()
