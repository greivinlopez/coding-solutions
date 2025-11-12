# -------------------------------------
# 847. Shortest Path Visiting All Nodes
# -------------------------------------

# Problem: https://leetcode.com/problems/shortest-path-visiting-all-nodes
#
# You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You
# are given an array graph where graph[i] is a list of all the nodes connected
# with node i by an edge.
# 
# Return the length of the shortest path that visits every node. You may start and
# stop at any node, you may revisit nodes multiple times, and you may reuse edges.
# 
# Example 1:
# 
# Input: graph = [[1,2,3],[0],[0],[0]]
# Output: 4
# 
# Explanation: One possible path is [1,0,2,0,3]
# 
# Example 2:
# 
# Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# 
# Explanation: One possible path is [0,1,4,2,3]
# 
# 
# Constraints:
#         n == graph.length
#         1 <= n <= 12
#         0 <= graph[i].length < n
#         graph[i] does not contain i.
#         If graph[a] contains b, then graph[b] contains a.
#         The input graph is always connected.

from collections import deque

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def shortest_path_length(graph):
    n = len(graph)
    queue = deque([(1 << i, i, 0) for i in range(n)])
    visited = set((1 << i, i) for i in range(n))
    
    while queue:
        mask, node, dist = queue.popleft()
        
        if mask == (1 << n) -1:
            return dist
        
        for neighbor in graph[node]:
            new_mask = mask | (1 << neighbor)
            if ( new_mask, neighbor) not in visited:
                visited.add((new_mask, neighbor))
                queue.append((new_mask, neighbor, dist + 1))
    # Time: O(n² * 2ⁿ)
    # Space: O(n * 2ⁿ)


def main():
    result = shortest_path_length(graph = [[1,2,3],[0],[0],[0]])
    print(result) # 4

    result = shortest_path_length(graph = [[1],[0,2,4],[1,3,4],[2],[1,2]])
    print(result) # 4

if __name__ == "__main__":
    main()
