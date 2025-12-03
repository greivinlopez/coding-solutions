# ---------------------------------------------------
# 1761. Minimum Degree of a Connected Trio in a Graph
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph
#
# You are given an undirected graph. You are given an integer n which is the
# number of nodes in the graph and an array edges, where each edges[i] = [uᵢ, vᵢ]
# indicates that there is an undirected edge between uᵢ and vᵢ.
# 
# A connected trio is a set of three nodes where there is an edge between every
# pair of them.
# 
# The degree of a connected trio is the number of edges where one endpoint is in
# the trio, and the other is not.
# 
# Return the minimum degree of a connected trio in the graph, or -1 if the graph
# has no connected trios.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/01/26/trios1.png
# 
# Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
# Output: 3
# 
# Explanation: There is exactly one trio, which is [1,2,3]. The edges that form
# its degree are bolded in the figure above.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/01/26/trios2.png
# 
# Input: n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
# Output: 0
# 
# Explanation: There are exactly three trios:
# 1) [1,4,3] with degree 0.
# 2) [2,5,6] with degree 2.
# 3) [5,6,7] with degree 2.
# 
# 
# Constraints:
#         2 <= n <= 400
#         edges[i].length == 2
#         1 <= edges.length <= n * (n-1) / 2
#         1 <= uᵢ, vᵢ <= n
#         uᵢ != vᵢ
#         There are no repeated edges.


# Solution: https://algo.monster/liteproblems/1761
# Credit: AlgoMonster
def min_trio_degree(n, edges):
    from math import inf

    # Create adjacency matrix to track connections between nodes
    # graph[i][j] = True if there's an edge between node i and j
    graph = [[False] * n for _ in range(n)]
    
    # Track the degree (number of connections) for each node
    degree = [0] * n
    
    # Build the graph from edges (convert to 0-indexed)
    for u, v in edges:
        u, v = u - 1, v - 1  # Convert from 1-indexed to 0-indexed
        graph[u][v] = graph[v][u] = True  # Undirected graph
        degree[u] += 1
        degree[v] += 1
    
    # Initialize minimum trio degree to infinity
    min_degree = inf
    
    # Check all possible trios (i, j, k) where i < j < k
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j]:  # If i and j are connected
                for k in range(j + 1, n):
                    # Check if k forms a trio with i and j
                    if graph[i][k] and graph[j][k]:
                        # Calculate trio degree: sum of degrees minus internal edges
                        # Each trio has 3 internal edges, counted twice in degree sum
                        trio_degree = degree[i] + degree[j] + degree[k] - 6
                        min_degree = min(min_degree, trio_degree)
    
    # Return -1 if no trio found, otherwise return minimum trio degree
    return -1 if min_degree == inf else min_degree
    # Time: O(n³)
    # Space: O(n²)


def main():
    result = min_trio_degree(n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]])
    print(result) # 3

    result = min_trio_degree(n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]])
    print(result) # 0

if __name__ == "__main__":
    main()
