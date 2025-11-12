# --------------------------------------
# 1377. Frog Position After T Seconds 🐸
# --------------------------------------

# Problem: https://leetcode.com/problems/frog-position-after-t-seconds
#
# Given an undirected tree consisting of n vertices numbered from 1 to n. A frog
# starts jumping from vertex 1. In one second, the frog jumps from its current
# vertex to another unvisited vertex if they are directly connected. The frog can
# not jump back to a visited vertex. In case the frog can jump to several
# vertices, it jumps randomly to one of them with the same probability. Otherwise,
# when the frog can not jump to any unvisited vertex, it jumps forever on the same
# vertex.
# 
# The edges of the undirected tree are given in the array edges, where edges[i] =
# [aᵢ, bᵢ] means that exists an edge connecting the vertices aᵢ and bᵢ.
# 
# Return the probability that after t seconds the frog is on the vertex target.
# Answers within 10⁻⁵ of the actual answer will be accepted.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/12/21/frog1.jpg
# 
# Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
# Output: 0.16666666666666666
# 
# Explanation: The figure above shows the given graph. The frog starts at vertex
# 1, jumping with 1/3 probability to the vertex 2 after second 1 and then jumping
# with 1/2 probability to vertex 4 after second 2. Thus the probability for the
# frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 =
# 0.16666666666666666.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/12/21/frog2.jpg
# 
# Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
# Output: 0.3333333333333333
# 
# Explanation: The figure above shows the given graph. The frog starts at vertex
# 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after
# second 1.
# 
# 
# Constraints:
#         1 <= n <= 100
#         edges.length == n - 1
#         edges[i].length == 2
#         1 <= aᵢ, bᵢ <= n
#         1 <= t <= 50
#         1 <= target <= n

from collections import defaultdict, deque

# Solution: https://algo.monster/liteproblems/1377
# Credit: AlgoMonster
def frog_position(n, edges, t, target):
    # Build adjacency list representation of the tree
    graph = defaultdict(list)
    for node_u, node_v in edges:
        graph[node_u].append(node_v)
        graph[node_v].append(node_u)
    
    # Initialize BFS queue with starting position (node 1) and probability 1.0
    queue = deque([(1, 1.0)])
    
    # Track visited nodes to avoid revisiting
    visited = [False] * (n + 1)
    visited[1] = True
    
    # Perform BFS for exactly t seconds
    while queue and t >= 0:
        # Process all nodes at current time step
        level_size = len(queue)
        for _ in range(level_size):
            current_node, probability = queue.popleft()
            
            # Calculate number of unvisited children
            # For root node (1), all neighbors are children
            # For other nodes, subtract 1 to exclude the parent
            unvisited_children_count = len(graph[current_node]) - int(current_node != 1)
            
            # Check if we've reached the target node
            if current_node == target:
                # Frog stays at target if no unvisited children or no time left
                # Otherwise, frog must jump away, so probability becomes 0
                return probability if unvisited_children_count * t == 0 else 0
            
            # Add unvisited neighbors to queue for next time step
            for neighbor in graph[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    # Probability is divided equally among unvisited children
                    queue.append((neighbor, probability / unvisited_children_count))
        
        # Decrement time after processing current level
        t -= 1
    
    # Target not reached within time limit
    return 0
    # Time: O(n)
    # Space: O(n)


def main():
    result = frog_position(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4)
    print(result) # 0.16666666666666666

    result = frog_position(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7)
    print(result) # 0.3333333333333333

if __name__ == "__main__":
    main()
