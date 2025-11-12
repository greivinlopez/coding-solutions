# ----------------------------------------
# 882. Reachable Nodes In Subdivided Graph
# ----------------------------------------

# Problem: https://leetcode.com/problems/reachable-nodes-in-subdivided-graph
#
# You are given an undirected graph (the "original graph") with n nodes labeled
# from 0 to n - 1. You decide to subdivide each edge in the graph into a chain of
# nodes, with the number of new nodes varying between each edge.
# 
# The graph is given as a 2D array of edges where edges[i] = [uᵢ, vᵢ, cntᵢ]
# indicates that there is an edge between nodes uᵢ and vᵢ in the original graph,
# and cntᵢ is the total number of new nodes that you will subdivide the edge into.
# Note that cntᵢ == 0 means you will not subdivide the edge.
# 
# To subdivide the edge [uᵢ, vᵢ], replace it with (cntᵢ + 1) new edges and cntᵢ
# new nodes. The new nodes are x₁, x₂, ..., x꜀ₙₜᵢ, and the new edges are [uᵢ, x₁],
# [x₁, x₂], [x₂, x3], ..., [x꜀ₙₜᵢ₋₁, x꜀ₙₜᵢ], [x꜀ₙₜᵢ, vi].
# 
# In this new graph, you want to know how many nodes are reachable from the node
# 0, where a node is reachable if the distance is maxMoves or less.
# 
# Given the original graph and maxMoves, return the number of nodes that are
# reachable from node 0 in the new graph.
# 
# Example 1:
# 
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/01/origfinal.png
# 
# Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
# Output: 13
# 
# Explanation: The edge subdivisions are shown in the image above.
# The nodes that are reachable are highlighted in yellow.
# 
# Example 2:
# 
# Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
# Output: 23
# 
# Example 3:
# 
# Input: edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
# Output: 1
# 
# Explanation: Node 0 is disconnected from the rest of the graph, so only node 0
# is reachable.
# 
# 
# Constraints:
#         0 <= edges.length <= min(n * (n - 1) / 2, 10⁴)
#         edges[i].length == 3
#         0 <= uᵢ < vᵢ < n
#         There are no multiple edges in the graph.
#         0 <= cntᵢ <= 10⁴
#         0 <= maxMoves <= 10⁹
#         1 <= n <= 3000

from collections import defaultdict
from heapq import heappop, heappush

# Solution: https://algo.monster/liteproblems/882
# Credit: AlgoMonster
def reachable_nodes(edges, maxMoves, n):
    # Build adjacency list representation of the graph
    # Each edge has 'cnt' intermediate nodes, so total distance is cnt + 1
    graph = defaultdict(list)
    for start_node, end_node, intermediate_count in edges:
        graph[start_node].append((end_node, intermediate_count + 1))
        graph[end_node].append((start_node, intermediate_count + 1))
    
    # Initialize priority queue for Dijkstra's algorithm
    # Format: (distance, node)
    priority_queue = [(0, 0)]
    
    # Initialize distances array (distance from node 0 to all other nodes)
    # dist[0] = 0 (starting node), all others initialized to infinity
    distances = [0] + [float('inf')] * n
    
    # Run Dijkstra's algorithm to find shortest distances from node 0
    while priority_queue:
        current_distance, current_node = heappop(priority_queue)
        
        # Explore neighbors of current node
        for neighbor, edge_weight in graph[current_node]:
            new_distance = current_distance + edge_weight
            
            # If we found a shorter path to the neighbor, update it
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(priority_queue, (new_distance, neighbor))
    
    # Count main nodes that are reachable within maxMoves
    reachable_count = sum(distance <= maxMoves for distance in distances)
    
    # Count intermediate nodes on edges that can be reached
    for start_node, end_node, intermediate_count in edges:
        # Calculate how many intermediate nodes can be reached from start_node
        reachable_from_start = min(intermediate_count, max(0, maxMoves - distances[start_node]))
        
        # Calculate how many intermediate nodes can be reached from end_node
        reachable_from_end = min(intermediate_count, max(0, maxMoves - distances[end_node]))
        
        # Total intermediate nodes reached on this edge (cannot exceed the actual count)
        reachable_count += min(intermediate_count, reachable_from_start + reachable_from_end)
    
    return reachable_count
    # Time: O((e + v) * log(v))
    # Space: O(e + v)
    # e = number of edges
    # v = number of vertices (n)


def main():
    result = reachable_nodes(edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3)
    print(result) # 13

    result = reachable_nodes(edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4)
    print(result) # 23

    result = reachable_nodes(edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5)
    print(result) # 1

if __name__ == "__main__":
    main()
