# -----------------------------------------------------
# 1617. Count Subtrees With Max Distance Between Cities
# -----------------------------------------------------

# Problem: https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities
#
# There are n cities numbered from 1 to n. You are given an array edges of size
# n-1, where edges[i] = [uᵢ, vᵢ] represents a bidirectional edge between cities uᵢ
# and vᵢ. There exists a unique path between each pair of cities. In other words,
# the cities form a tree.
# 
# A subtree is a subset of cities where every city is reachable from every other
# city in the subset, where the path between each pair passes through only the
# cities from the subset. Two subtrees are different if there is a city in one
# subtree that is not present in the other.
# 
# For each d from 1 to n-1, find the number of subtrees in which the maximum
# distance between any two cities in the subtree is equal to d.
# 
# Return an array of size n-1 where the dᵗʰ element (1-indexed) is the number of
# subtrees in which the maximum distance between any two cities is equal to d.
# 
# Notice that the distance between the two cities is the number of edges in the
# path between them.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/21/p1.png
# 
# Input: n = 4, edges = [[1,2],[2,3],[2,4]]
# Output: [3,4,0]
# 
# Explanation:
# The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
# The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max
# distance of 2.
# No subtree has two nodes where the max distance between them is 3.
# 
# Example 2:
# 
# Input: n = 2, edges = [[1,2]]
# Output: [1]
# 
# Example 3:
# 
# Input: n = 3, edges = [[1,2],[2,3]]
# Output: [2,1]
# 
# 
# Constraints:
#         2 <= n <= 15
#         edges.length == n-1
#         edges[i].length == 2
#         1 <= uᵢ, vᵢ <= n
#         All pairs (uᵢ, vᵢ) are distinct.


# Solution: https://algo.monster/liteproblems/1617
# Credit: AlgoMonster
def count_subgraphs_for_each_diameter(n, edges):
    from collections import defaultdict
    
    def dfs(node, distance = 0):
        nonlocal max_distance, farthest_node, visited_mask
        
        # Update the farthest node if we found a longer path
        if max_distance < distance:
            max_distance = distance
            farthest_node = node
        
        # Mark current node as visited by flipping its bit
        visited_mask ^= (1 << node)
        
        # Explore all neighbors that are in the current subset
        for neighbor in adjacency_list[node]:
            if visited_mask >> neighbor & 1:  # Check if neighbor is in subset and not visited
                dfs(neighbor, distance + 1)
    
    # Build adjacency list for the tree (converting to 0-indexed)
    adjacency_list = defaultdict(list)
    for u, v in edges:
        u, v = u - 1, v - 1
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    
    # Initialize result array for diameters from 1 to n-1
    result = [0] * (n - 1)
    
    # Variables to track during DFS
    farthest_node = 0
    max_distance = 0
    
    # Iterate through all possible non-empty subsets of nodes
    for subset_mask in range(1, 1 << n):
        # Skip subsets with only one node (no edges, no diameter)
        if subset_mask & (subset_mask - 1) == 0:
            continue
        
        # Initialize for first DFS
        visited_mask = subset_mask
        max_distance = 0
        
        # Start DFS from the highest bit set (rightmost node in subset)
        start_node = visited_mask.bit_length() - 1
        dfs(start_node)
        
        # Check if all nodes in subset were visited (connected subgraph)
        if visited_mask == 0:
            # Run second DFS from farthest node to find actual diameter
            visited_mask = subset_mask
            max_distance = 0
            dfs(farthest_node)
            
            # Record this diameter count
            result[max_distance - 1] += 1
    
    return result
    # Time: O(2ⁿ * n)
    # Space: O(n)


def main():
    result = count_subgraphs_for_each_diameter(n = 4, edges = [[1,2],[2,3],[2,4]])
    print(result) # [3, 4, 0]

    result = count_subgraphs_for_each_diameter(n = 2, edges = [[1,2]])
    print(result) # [1]

    result = count_subgraphs_for_each_diameter(n = 3, edges = [[1,2],[2,3]])
    print(result) # [2, 1]

if __name__ == "__main__":
    main()
