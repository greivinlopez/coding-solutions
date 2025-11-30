# -----------------------------------------------------
# 1697. Checking Existence of Edge Length Limited Paths
# -----------------------------------------------------

# Problem: https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths
#
# An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [uᵢ,
# vᵢ, disᵢ] denotes an edge between nodes uᵢ and vᵢ with distance disᵢ. Note that
# there may be multiple edges between two nodes.
# 
# Given an array queries, where queries[j] = [pⱼ, qⱼ, limitⱼ], your task is to
# determine for each queries[j] whether there is a path between pⱼ and qⱼ such
# that each edge on the path has a distance strictly less than limitⱼ.
# 
# Return a boolean array answer, where answer.length == queries.length and the jᵗʰ
# value of answer is true if there is a path for queries[j] is true, and false
# otherwise.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/12/08/h.png
# 
# Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries =
# [[0,1,2],[0,2,5]]
# Output: [false,true]
# 
# Explanation: The above figure shows the given graph. Note that there are two
# overlapping edges between 0 and 1 with distances 2 and 16.
# For the first query, between 0 and 1 there is no path where each distance is
# less than 2, thus we return false for this query.
# For the second query, there is a path (0 -> 1 -> 2) of two edges with distances
# less than 5, thus we return true for this query.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/12/08/q.png
# 
# Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries =
# [[0,4,14],[1,4,13]]
# Output: [true,false]
# 
# Explanation: The above figure shows the given graph.
# 
# 
# Constraints:
#         2 <= n <= 10⁵
#         1 <= edgeList.length, queries.length <= 10⁵
#         edgeList[i].length == 3
#         queries[j].length == 3
#         0 <= uᵢ, vᵢ, pⱼ, qⱼ <= n - 1
#         uᵢ != vᵢ
#         pⱼ != qⱼ
#         1 <= disᵢ, limitⱼ <= 10⁹
#         There may be multiple edges between two nodes.


# Solution: https://algo.monster/liteproblems/1697
# Credit: AlgoMonster
def distance_limited_paths_exist(n, edgeList, queries):

    def find(node):
        if parent[node] != node:
            # Path compression: make node point directly to root
            parent[node] = find(parent[node])
        return parent[node]
    
    # Initialize Union-Find parent array where each node is its own parent
    parent = list(range(n))
    
    # Sort edges by weight in ascending order
    edgeList.sort(key=lambda edge: edge[2])
    
    # Initialize result array
    result = [False] * len(queries)
    
    # Process queries in ascending order of limit while preserving original indices
    # enumerate(queries) gives (index, query), then sort by query's limit (index 2)
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][2])
    
    edge_index = 0
    
    for query_index, (node_a, node_b, distance_limit) in sorted_queries:
        # Add all edges with weight less than current query's limit to Union-Find
        while edge_index < len(edgeList) and edgeList[edge_index][2] < distance_limit:
            u, v, _ = edgeList[edge_index]
            # Union operation: connect the two components
            parent[find(u)] = find(v)
            edge_index += 1
        
        # Check if node_a and node_b are in the same connected component
        result[query_index] = find(node_a) == find(node_b)
    
    return result
    # Time: O(m × log m + q × log q)
    # Space: O(n + m + q)
    # m = the number of edges
    # q = the number of queries


def main():
    result = distance_limited_paths_exist(n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]])
    print(result) # [False, True]

    result = distance_limited_paths_exist(n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]])
    print(result) # [True, False]

if __name__ == "__main__":
    main()
