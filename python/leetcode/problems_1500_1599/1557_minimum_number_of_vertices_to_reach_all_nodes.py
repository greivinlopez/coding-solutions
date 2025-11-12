# ---------------------------------------------------
# 1557. Minimum Number of Vertices to Reach All Nodes
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes
#
# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an
# array edges where edges[i] = [fromi, toi] represents a directed edge from
# node fromi to node toi.
# 
# Find the smallest set of vertices from which all nodes in the graph are
# reachable. It's guaranteed that a unique solution exists.
# 
# Notice that you can return the vertices in any order.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/07/07/untitled22.png
# 
# Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
# Output: [0,3]
# 
# Explanation: It's not possible to reach all the nodes from a single vertex. From
# 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/07/07/untitled.png
# 
# Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
# Output: [0,2,3]
# 
# Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other
# node, so we must include them. Also any of these vertices can reach nodes 1 and
# 4.
# 
# 
# Constraints:
#         2 <= n <= 10^5
#         1 <= edges.length <= min(10^5, n * (n - 1) / 2)
#         edges[i].length == 2
#         0 <= fromᵢ, toᵢ < n
#         All pairs (fromᵢ, toᵢ) are distinct.

from collections import defaultdict

# Solution: https://youtu.be/TLzcum7vrTc
# Credit: Navdeep Singh founder of NeetCode
def find_smallest_set_of_vertices(n, edges):
    incoming = defaultdict(list)
    for src, dst in edges:
        incoming[dst].append(src)

    res = []
    for i in range(n):
        if not incoming[i]:
            res.append(i)
    
    return res
    # Time: O(v + e)    v = vertices, e = edges
    # Space: O(v + e)


def main():
    edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
    result = find_smallest_set_of_vertices(6, edges)
    print(result) # [0,3]

    edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
    result = find_smallest_set_of_vertices(5, edges)
    print(result) # [0,2,3]

if __name__ == "__main__":
    main()
