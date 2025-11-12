# --------------------------------
# 1202. Smallest String With Swaps
# --------------------------------

# Problem: https://leetcode.com/problems/smallest-string-with-swaps
#
# You are given a string s, and an array of pairs of indices in the
# string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the
# string.
# 
# You can swap the characters at any pair of indices in the given pairs any number
# of times.
# 
# Return the lexicographically smallest string that s can be changed to after
# using the swaps.
# 
# Example 1:
# 
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# 
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# 
# Example 2:
# 
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# 
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# 
# Example 3:
# 
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# 
# Explaination:
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
# 
# 
# Constraints:
#         1 <= s.length <= 10^5
#         0 <= pairs.length <= 10^5
#         0 <= pairs[i][0], pairs[i][1] < s.length
#         s only contains lower case English letters.

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/1202
# Credit: AlgoMonster
def smallest_string_with_swaps(s, pairs):
    # Find the root parent of a node using path compression
    def find_root(node: int) -> int:
        if parent[node] != node:
            # Path compression: directly connect node to its root
            parent[node] = find_root(parent[node])
        return parent[node]
    
    n = len(s)
    # Initialize parent array where each node is its own parent
    parent = list(range(n))
    
    # Union operation: connect all indices that can be swapped
    for index_a, index_b in pairs:
        # Union by connecting roots of both indices
        parent[find_root(index_a)] = find_root(index_b)
    
    # Group characters by their connected component (root parent)
    component_chars = defaultdict(list)
    for index, char in enumerate(s):
        root = find_root(index)
        component_chars[root].append(char)
    
    # Sort characters in each component in descending order
    # This allows us to pop from the end (smallest character) efficiently
    for root in component_chars.keys():
        component_chars[root].sort(reverse=True)
    
    # Build result by taking smallest available character from each component
    result = []
    for index in range(n):
        root = find_root(index)
        # Pop the smallest character (last element after reverse sort)
        result.append(component_chars[root].pop())
    
    return "".join(result)
    # Time: O(n * log n + m * α(m))
    # Space: O(n)
    # where α is the inverse Ackermann function


def main():
    result = smallest_string_with_swaps(s = "dcab", pairs = [[0,3],[1,2]])
    print(result) # "bacd"

    result = smallest_string_with_swaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]])
    print(result) # "abcd"

    result = smallest_string_with_swaps(s = "cba", pairs = [[0,1],[1,2]])
    print(result) # "abc"

if __name__ == "__main__":
    main()
