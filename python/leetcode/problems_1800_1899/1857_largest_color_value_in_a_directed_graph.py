# ---------------------------------------------
# 1857. Largest Color Value in a Directed Graph
# ---------------------------------------------

# Problem: https://leetcode.com/problems/largest-color-value-in-a-directed-graph
#
# There is a directed graph of n colored nodes and m edges. The nodes are numbered
# from 0 to n - 1.
# 
# You are given a string colors where colors[i] is a lowercase English letter
# representing the color of the ith node in this graph (0-indexed). You are also
# given a 2D array edges where edges[j] = [aj, bj] indicates that there is a
# directed edge from node aj to node bj.
# 
# A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk
# such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The
# color value of the path is the number of nodes that are colored the most
# frequently occurring color along that path.
# 
# Return the largest color value of any valid path in the given graph, or -1 if
# the graph contains a cycle.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/04/21/leet1.png
# 
# Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# Output: 3
# 
# Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a"
# (red in the above image).
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/04/21/leet2.png
# 
# Input: colors = "a", edges = [[0,0]]
# Output: -1
# 
# Explanation: There is a cycle from 0 to 0.
# 
# 
# Constraints:
#         n == colors.length
#         m == edges.length
#         1 <= n <= 10^5
#         0 <= m <= 10^5
#         colors consists of lowercase English letters.
#         0 <= aj, bj < n

from collections import defaultdict

# Solution: https://youtu.be/xLoDjKczUSk
# Credit: Navdeep Singh founder of NeetCode
def largest_path_value(colors, edges):
    adj = defaultdict(list)
    for src, dst in edges:
        adj[src].append(dst)

    n = len(colors)
    res = 0
    visit, path = set(), set()
    count = [[0] * 26 for i in range(n)]

    def dfs(node):
        if node in path:
            return float("inf")
        if node in visit:
            return 0

        visit.add(node)
        path.add(node)
        
        colorIndex = ord(colors[node]) - ord('a')
        count[node][colorIndex] = 1
        
        for nei in adj[node]:
            if dfs(nei) == float("inf"):
                return float("inf")
            
            for c in range(26):
                count[node][c] = max(
                    count[node][c],
                    count[nei][c] + (1 if c == colorIndex else 0)
                )
        
        path.remove(node)
        return max(count[node])
        
    for i in range(n):
        res = max(res, dfs(i))
        
    return res if res != float("inf") else -1
    # Time: O(v + e)
    # Space: O(v + e)


def main():
    result = largest_path_value(colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]])
    print(result) # 3

    result = largest_path_value(colors = "a", edges = [[0,0]])
    print(result) # -1

if __name__ == "__main__":
    main()
