# --------------------------
# 2421. Number of Good Paths
# --------------------------

# Problem: https://leetcode.com/problems/number-of-good-paths
#
# There is a tree (i.e. a connected, undirected graph with no cycles) consisting
# of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.
# 
# You are given a 0-indexed integer array vals of length n where vals[i] denotes
# the value of the ith node. You are also given a 2D integer array edges where
# edges[i] = [aᵢ, bᵢ] denotes that there exists an undirected edge connecting
# nodes aᵢ and bᵢ.
# 
# A good path is a simple path that satisfies the following conditions:
#         
#   * The starting node and the ending node have the same value.
#   * All nodes between the starting node and the ending node have values less
#     than or equal to the starting node (i.e. the starting node's value should be the
#     maximum value along the path).
# 
# Return the number of distinct good paths.
# 
# Note that a path and its reverse are counted as the same path. For example, 0 ->
# 1 is considered to be the same as 1 -> 0. A single node is also considered as a
# valid path.
# 
# Example 1:
# 
# Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
# Output: 6
# 
# Explanation: There are 5 good paths consisting of a single node.
# There is 1 additional good path: 1 -> 0 -> 2 -> 4.
# (The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
# Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].
# 
# Example 2:
# 
# Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
# Output: 7
# 
# Explanation: There are 5 good paths consisting of a single node.
# There are 2 additional good paths: 0 -> 1 and 2 -> 3.
# 
# Example 3:
# 
# Input: vals = [1], edges = []
# Output: 1
# 
# Explanation: The tree consists of only one node, so there is one good path.
# 
# 
# Constraints:
#         n == vals.length
#         1 <= n <= 3 * 104
#         0 <= vals[i] <= 105
#         edges.length == n - 1
#         edges[i].length == 2
#         0 <= ai, bi < n
#         ai != bi
#         edges represents a valid tree.

from collections import defaultdict

# Solution: https://youtu.be/rv2GBYQm7xM
# Credit: Navdeep Singh founder of NeetCode
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        while i != self.par[i]:
            self.par[i] = self.par[self.par[i]]
            i = self.par[i]
        return i

    def union(self, a, b):
        aRoot = self.find(a)
        bRoot = self.find(b)

        if aRoot == bRoot:
            return False

        if self.rank[aRoot] < self.rank[bRoot]:
            self.par[aRoot] = bRoot
            self.rank[bRoot] += self.rank[aRoot]
        else:
            self.par[bRoot] = aRoot
            self.rank[aRoot] += self.rank[bRoot]

        return True

def number_of_good_paths(vals, edges):
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    val_to_index = defaultdict(list)
    for i, val in enumerate(vals):
        val_to_index[val].append(i)

    res = 0
    uf = UnionFind(len(vals))
    for val in sorted(val_to_index.keys()):
        for i in val_to_index[val]:
            for nei in adj[i]:
                if vals[nei] <= vals[i]:
                    uf.union(nei, i)
        
        # For each disjoint set, how many val's does it contain?
        count = defaultdict(int)
        for i in val_to_index[val]:
            count[uf.find(i)] += 1
            res += count[uf.find(i)]
    
    return res
    # Time: O(e * log(v) + v)
    # Space: O(e + v)
    # e = number of edges
    # v = number of vertices (nodes)


def main():
    result = number_of_good_paths(vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]])
    print(result) # 6

    result = number_of_good_paths(vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]])
    print(result) # 7

    result = number_of_good_paths(vals = [1], edges = [])
    print(result) # 1

if __name__ == "__main__":
    main()
