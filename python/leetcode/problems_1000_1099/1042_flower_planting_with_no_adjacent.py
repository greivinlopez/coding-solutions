# -------------------------------------
# 1042. Flower Planting With No Adjacent
# -------------------------------------

# Problem: https://leetcode.com/problems/flower-planting-with-no-adjacent
#
# You have n gardens, labeled from 1 to n, and an array paths where paths[i] =
# [xᵢ, yᵢ] describes a bidirectional path between garden xᵢ to garden yᵢ. In each
# garden, you want to plant one of 4 types of flowers.
# 
# All gardens have at most 3 paths coming into or leaving it.
# 
# Your task is to choose a flower type for each garden such that, for any two
# gardens connected by a path, they have different types of flowers.
# 
# Return any such a choice as an array answer, where answer[i] is the type of
# flower planted in the (i+1)ᵗʰ garden. The flower types are denoted 1, 2, 3, or
# 4. It is guaranteed an answer exists.
# 
# Example 1:
# 
# Input: n = 3, paths = [[1,2],[2,3],[3,1]]
# Output: [1,2,3]
# 
# Explanation:
# Gardens 1 and 2 have different types.
# Gardens 2 and 3 have different types.
# Gardens 3 and 1 have different types.
# Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2],
# and [3,2,1].
# 
# Example 2:
# 
# Input: n = 4, paths = [[1,2],[3,4]]
# Output: [1,2,1,2]
# 
# Example 3:
# 
# Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# Output: [1,2,3,4]
# 
# 
# Constraints:
#         1 <= n <= 10⁴
#         0 <= paths.length <= 2 * 10⁴
#         paths[i].length == 2
#         1 <= xᵢ, yᵢ <= n
#         xᵢ != yᵢ
#         Every garden has at most 3 paths coming into or leaving it.

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/1042
# Credit: AlgoMonster
def garden_no_adj(n, paths):
    # Build adjacency list for the graph
    # Key: garden index (0-based), Value: list of adjacent garden indices
    adjacency_graph = defaultdict(list)
    
    # Convert paths to 0-based indexing and build bidirectional edges
    for garden1, garden2 in paths:
        # Convert from 1-based to 0-based indexing
        garden1_idx = garden1 - 1
        garden2_idx = garden2 - 1
        
        # Add bidirectional edges
        adjacency_graph[garden1_idx].append(garden2_idx)
        adjacency_graph[garden2_idx].append(garden1_idx)
    
    # Initialize result array to store flower type for each garden
    # 0 means no flower type assigned yet
    flower_assignments = [0] * n
    
    # Process each garden one by one
    for current_garden in range(n):
        # Collect flower types already used by neighboring gardens
        used_flower_types = {flower_assignments[neighbor] 
                            for neighbor in adjacency_graph[current_garden]}
        
        # Try assigning flower types 1 through 4
        for flower_type in range(1, 5):
            # If this flower type is not used by any neighbor
            if flower_type not in used_flower_types:
                # Assign this flower type to current garden
                flower_assignments[current_garden] = flower_type
                break  # Move to next garden
    
    return flower_assignments
    # Time: O(n + m)
    # Space: O(n + m)


def main():
    result = garden_no_adj(n = 3, paths = [[1,2],[2,3],[3,1]])
    print(result) # [1, 2, 3]

    result = garden_no_adj(n = 4, paths = [[1,2],[3,4]])
    print(result) # [1, 2, 1, 2]

    result = garden_no_adj(n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]])
    print(result) # [1, 2, 3, 4]

if __name__ == "__main__":
    main()
