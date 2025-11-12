# ----------------------------
# 685. Redundant Connection II
# ----------------------------

# Problem: https://leetcode.com/problems/redundant-connection-ii
#
# In this problem, a rooted tree is a directed graph such that, there is exactly
# one node (the root) for which all other nodes are descendants of this node, plus
# every node has exactly one parent, except for the root node which has no
# parents.
# 
# The given input is a directed graph that started as a rooted tree with n nodes
# (with distinct values from 1 to n), with one additional directed edge added. The
# added edge has two different vertices chosen from 1 to n, and was not an edge
# that already existed.
# 
# The resulting graph is given as a 2D-array of edges. Each element of edges is a
# pair [uᵢ, vᵢ] that represents a directed edge connecting nodes uᵢ and vᵢ, where
# uᵢ is a parent of child vᵢ.
# 
# Return an edge that can be removed so that the resulting graph is a rooted tree
# of n nodes. If there are multiple answers, return the answer that occurs last in
# the given 2D-array.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/12/20/graph1.jpg
# 
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/12/20/graph2.jpg
# 
# Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
# Output: [4,1]
# 
# 
# Constraints:
#         n == edges.length
#         3 <= n <= 1000
#         edges[i].length == 2
#         1 <= uᵢ, vᵢ <= n
#         uᵢ != vᵢ


# Solution: https://algo.monster/liteproblems/685
# Credit: AlgoMonster
def find_redundant_directed_connection(edges):

    def find_root(node: int) -> int:
        """Find the root of the node using path compression."""
        if parent[node] != node:
            parent[node] = find_root(parent[node])  # Path compression
        return parent[node]
    
    n = len(edges)
    
    # Count in-degrees for each node (to find nodes with 2 parents)
    in_degree = [0] * n
    for parent_node, child_node in edges:
        in_degree[child_node - 1] += 1
    
    # Find edges where the child has 2 parents (in-degree = 2)
    duplicate_parent_edges = [
        i for i, (parent_node, child_node) in enumerate(edges) 
        if in_degree[child_node - 1] == 2
    ]
    
    # Initialize Union-Find parent array
    parent = list(range(n))
    
    if duplicate_parent_edges:
        # Case 1: A node has two parents
        # Try removing the second edge first
        for i, (u, v) in enumerate(edges):
            if i == duplicate_parent_edges[1]:
                continue  # Skip the second duplicate edge
            
            root_u, root_v = find_root(u - 1), find_root(v - 1)
            
            if root_u == root_v:
                # Found a cycle without the second edge
                # So the first duplicate edge must be removed
                return edges[duplicate_parent_edges[0]]
            
            # Union the components
            parent[root_u] = root_v
        
        # No cycle found after removing second edge
        # So the second edge should be removed
        return edges[duplicate_parent_edges[1]]
    
    # Case 2: No node has two parents, just find the cycle
    for i, (u, v) in enumerate(edges):
        root_u, root_v = find_root(u - 1), find_root(v - 1)
        
        if root_u == root_v:
            # Found the edge that creates a cycle
            return edges[i]
        
        # Union the components
        parent[root_u] = root_v
    
    # This line should never be reached given valid input
    return []
    # Time: O(n * α(n))
    # Space: O(n)
    # α(n) is the inverse Ackermann function


def main():
    result = find_redundant_directed_connection(edges = [[1,2],[1,3],[2,3]])
    print(result) # [2, 3]

    result = find_redundant_directed_connection(edges = [[1,2],[2,3],[3,4],[4,1],[1,5]])
    print(result) # [4, 1]

if __name__ == "__main__":
    main()
