# --------------------------
# 839. Similar String Groups
# --------------------------

# Problem: https://leetcode.com/problems/similar-string-groups
#
# Two strings, X and Y, are considered similar if either they are identical or we
# can make them equivalent by swapping at most two letters (in distinct positions)
# within the string X.
# 
# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and
# "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or
# "arts".
# 
# Together, these form two connected groups by similarity: {"tars", "rats",
# "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even
# though they are not similar.  Formally, each group is such that a word is in the
# group if and only if it is similar to at least one other word in the group.
# 
# We are given a list strs of strings where every string in strs is an anagram of
# every other string in strs. How many groups are there?
# 
# Example 1:
# 
# Input: strs = ["tars","rats","arts","star"]
# Output: 2
# 
# Example 2:
# 
# Input: strs = ["omv","ovm"]
# Output: 1
# 
# 
# Constraints:
#         1 <= strs.length <= 300
#         1 <= strs[i].length <= 300
#         strs[i] consists of lowercase letters only.
#         All words in strs have the same length and are anagrams of each other.


# Solution: https://leetcode.com/problems/similar-string-groups/solutions/3462133/image-explanation-easy-to-understand-concise-c-java-python
# Credit: Aryan Mittal -> https://leetcode.com/u/lc00701/
def num_similar_groups(strs):
    def is_similar(a, b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]: count += 1
        return count == 2 or count == 0

    def dfs(i, strs, vis):
        vis[i] = True
        for j in range(len(strs)):
            if vis[j]: continue
            if is_similar(strs[i], strs[j]):
                dfs(j, strs, vis)

    groups = 0
    n = len(strs)
    vis = [False] * n
    for i in range(n):
        if vis[i]: continue
        groups += 1
        dfs(i, strs, vis)
    return groups
    # Time: O(n² * m)
    # Space: O(n * m)
    # n = the number of strings in strs
    # m = the length of each string. Since all strings in a similarity group problem typically have the same length, we assume this holds.

# Alternative Solution: Using Union-Find (Disjoint Set Union) data structure.
# Solution: https://algo.monster/liteproblems/839
# Credit: AlgoMonster


def main():
    result = num_similar_groups(strs = ["tars","rats","arts","star"])
    print(result) # 2

    result = num_similar_groups(strs = ["omv","ovm"])
    print(result) # 1

if __name__ == "__main__":
    main()
