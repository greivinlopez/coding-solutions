# ----------------------------------------------------------------------
# 1489. Find Critical And Pseudo Critical Edges In Minimum Spanning Tree
# ----------------------------------------------------------------------

# Problem: https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree
#
# Given a weighted undirected connected graph with n vertices numbered from 0 to n
# - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a
# bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree
# (MST) is a subset of the graph's edges that connects all vertices without
# cycles and with the minimum possible total edge weight.
# 
# Find all the critical and pseudo-critical edges in the given graph's minimum
# spanning tree (MST). An MST edge whose deletion from the graph would cause the
# MST weight to increase is called a critical edge. On the other hand, a pseudo-
# critical edge is that which can appear in some MSTs but not all.
# 
# Note that you can return the indices of the edges in any order.
# 
# Example 1:
# 
# Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# Output: [[0,1],[2,3,4,5]]
# Explanation: The figure above describes the graph.
# The following figure shows all the possible MSTs:
# Notice that the two edges 0 and 1 appear in all MSTs, therefore they are
# critical edges, so we return them in the first list of the output.
# The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are
# considered pseudo-critical edges. We add them to the second list of the output.
# 
# Example 2:
# 
# Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# Output: [[],[0,1,2,3]]
# Explanation: We can observe that since all 4 edges have equal weight, choosing
# any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are
# pseudo-critical.
# 
# 
# Constraints:
#         2 <= n <= 100
#         1 <= edges.length <= min(200, n * (n - 1) / 2)
#         edges[i].length == 3
#         0 <= ai < bi < n
#         1 <= weighti <= 1000
#         All pairs (ai, bi) are distinct.


# Solution: https://youtu.be/83JnUxrLKJU
# Credit: Navdeep Singh founder of NeetCode
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v1):
        while v1 != self.par[v1]:
            self.par[v1] = self.par[self.par[v1]]
            v1 = self.par[v1]
        return v1

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

def find_critical_and_pseudo_critical_edges(n, edges):
    for i, e in enumerate(edges):
        e.append(i) # [v1, v2, weight, original_index]

    edges.sort(key=lambda e: e[2])

    mst_weight = 0
    uf = UnionFind(n)
    for v1, v2, w, i in edges:
        if uf.union(v1, v2):
            mst_weight += w

    critical, pseudo = [], []
    for n1, n2, e_weight, i in edges:
        # Try without curr edge
        weight = 0
        uf = UnionFind(n)
        for v1, v2, w, j in edges:
            if i != j and uf.union(v1, v2):
                weight += w
        if max(uf.rank) != n or weight > mst_weight:
            critical.append(i)
            continue
        
        # Try with curr edge
        uf = UnionFind(n)
        uf.union(n1, n2)
        weight = e_weight
        for v1, v2, w, j in edges:
            if uf.union(v1, v2):
                weight += w
        if weight == mst_weight:
            pseudo.append(i)
    return [critical, pseudo]
    # Time: O(E^2) - UF operations are assumed to be approx O(1)

def main():
    edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
    result = find_critical_and_pseudo_critical_edges(5, edges)
    print(result) # [[0,1],[2,3,4,5]]

    edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
    result = find_critical_and_pseudo_critical_edges(4, edges)
    print(result) # [[],[0,1,2,3]]

if __name__ == "__main__":
    main()
