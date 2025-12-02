# ------------------------------------------
# 1719. Number Of Ways To Reconstruct A Tree
# ------------------------------------------

# Problem: https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree
#
# You are given an array pairs, where pairs[i] = [xᵢ, yᵢ], and:
#         
#   * There are no duplicates.
#   * xᵢ < yᵢ
# 
# Let ways be the number of rooted trees that satisfy the following conditions:
#         
#   * The tree consists of nodes whose values appeared in pairs.
#   * A pair [xᵢ, yᵢ] exists in pairs if and only if xᵢ is an ancestor of yᵢ or yᵢ
#     is an ancestor of xᵢ.
#   * Note: the tree does not have to be a binary tree.
# 
# Two ways are considered to be different if there is at least one node that has
# different parents in both ways.
# 
# Return:
#         0 if ways == 0
#         1 if ways == 1
#         2 if ways > 1
# 
# A rooted tree is a tree that has a single root node, and all edges are oriented
# to be outgoing from the root.
# 
# An ancestor of a node is any node on the path from the root to that node
# (excluding the node itself). The root has no ancestors.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/12/03/trees2.png
# 
# Input: pairs = [[1,2],[2,3]]
# Output: 1
# 
# Explanation: There is exactly one valid rooted tree, which is shown in the above
# figure.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/12/03/tree.png
# 
# Input: pairs = [[1,2],[2,3],[1,3]]
# Output: 2
# 
# Explanation: There are multiple valid rooted trees. Three of them are shown in
# the above figures.
# 
# Example 3:
# 
# Input: pairs = [[1,2],[2,3],[2,4],[1,5]]
# Output: 0
# 
# Explanation: There are no valid rooted trees.
# 
# 
# Constraints:
#         1 <= pairs.length <= 10⁵
#         1 <= xᵢ < yᵢ <= 500
#         The elements in pairs are unique.


# Solution: https://algo.monster/liteproblems/1719
# Credit: AlgoMonster
def check_ways(pairs):
    from collections import defaultdict

    # Create adjacency matrix to track connections between nodes
    adjacency_matrix = [[False] * 510 for _ in range(510)]
    
    # Create adjacency list to store neighbors for each node
    adjacency_list = defaultdict(list)
    
    # Build the graph from the given pairs
    for node1, node2 in pairs:
        adjacency_matrix[node1][node2] = adjacency_matrix[node2][node1] = True
        adjacency_list[node1].append(node2)
        adjacency_list[node2].append(node1)
    
    # Collect all nodes that appear in the pairs
    active_nodes = []
    for node_id in range(510):
        if adjacency_list[node_id]:
            active_nodes.append(node_id)
            # Mark self-connection as true for active nodes
            adjacency_matrix[node_id][node_id] = True
    
    # Sort nodes by their degree (number of connections) in ascending order
    active_nodes.sort(key=lambda node: len(adjacency_list[node]))
    
    # Track if there are multiple valid trees possible
    multiple_solutions_exist = False
    
    # Count potential root nodes
    root_count = 0
    
    # Check each node to find its potential parent in the tree
    for current_index, current_node in enumerate(active_nodes):
        # Look for the first node with higher or equal degree that is connected
        parent_index = current_index + 1
        while parent_index < len(active_nodes) and not adjacency_matrix[current_node][active_nodes[parent_index]]:
            parent_index += 1
        
        if parent_index < len(active_nodes):
            # Found a potential parent node
            parent_node = active_nodes[parent_index]
            
            # Check if degrees are equal (multiple valid parent choices)
            if len(adjacency_list[current_node]) == len(adjacency_list[parent_node]):
                multiple_solutions_exist = True
            
            # Verify that all neighbors of current node are also connected to parent
            # This is necessary for a valid tree structure
            for neighbor in adjacency_list[current_node]:
                if not adjacency_matrix[parent_node][neighbor]:
                    return 0  # Invalid tree structure
        else:
            # No parent found, this node could be a root
            root_count += 1
    
    # A valid tree must have exactly one root
    if root_count > 1:
        return 0  # Invalid: multiple disconnected components
    
    # Return 2 if multiple valid trees exist, 1 if unique tree exists
    return 2 if multiple_solutions_exist else 1
    # Time: O(n² + m * n)
    # Space: O(1)


def main():
    result = check_ways(pairs = [[1,2],[2,3]])
    print(result) # 1

    result = check_ways(pairs = [[1,2],[2,3],[1,3]])
    print(result) # 2

    result = check_ways(pairs = [[1,2],[2,3],[2,4],[1,5]])
    print(result) # 0

if __name__ == "__main__":
    main()
