# ------------------------------------
# 797. All Paths From Source to Target
# ------------------------------------

# Problem: https://leetcode.com/problems/all-paths-from-source-to-target
#
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find
# all possible paths from node 0 to node n - 1 and return them in any order.
# 
# The graph is given as follows: graph[i] is a list of all nodes you can visit
# from node i (i.e., there is a directed edge from node i to node graph[i][j]).
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg
# 
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# 
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/09/28/all_2.jpg
# 
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
# 
# 
# Constraints:
#         n == graph.length
#         2 <= n <= 15
#         0 <= graph[i][j] < n
#         graph[i][j] != i (i.e., there will be no self-loops).
#         All the elements of graph[i] are unique.
#         The input graph is guaranteed to be a DAG.

from collections import deque

# Solution: https://algo.monster/liteproblems/797
# Credit: AlgoMonster
def all_paths_source_target(graph):
    # Get the number of nodes in the graph
    n = len(graph)
    
    # Initialize queue with the starting path containing only node 0
    queue = deque([[0]])
    
    # Store all valid paths from source to target
    result = []
    
    # BFS traversal to explore all paths
    while queue:
        # Get the current path from the queue
        current_path = queue.popleft()
        
        # Get the last node in the current path
        last_node = current_path[-1]
        
        # Check if we've reached the target node (n-1)
        if last_node == n - 1:
            # Add the complete path to results
            result.append(current_path)
            continue
        
        # Explore all neighbors of the current node
        for neighbor in graph[last_node]:
            # Create a new path by extending the current path with the neighbor
            new_path = current_path + [neighbor]
            queue.append(new_path)
    
    return result
    # Time: O(2ⁿ * n)
    # Space: O(2ⁿ * n)


def main():
    result = all_paths_source_target(graph = [[1,2],[3],[3],[]])
    print(result) # [[0, 1, 3], [0, 2, 3]]

    result = all_paths_source_target(graph = [[4,3,1],[3,2,4],[3],[4],[]])
    print(result) # [[0, 4], [0, 3, 4], [0, 1, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4]]

if __name__ == "__main__":
    main()
