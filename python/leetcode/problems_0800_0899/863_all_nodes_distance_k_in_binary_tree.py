# ----------------------------------------
# 863. All Nodes Distance K in Binary Tree
# ----------------------------------------

# Problem: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree
#
# Given the root of a binary tree, the value of a target node target, and an
# integer k, return an array of the values of all nodes that have a distance k
# from the target node.
# 
# You can return the answer in any order.
# 
# Example 1:
# 
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# 
# Explanation: The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
# 
# Example 2:
# 
# Input: root = [1], target = 1, k = 3
# Output: []
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 500].
#         0 <= Node.val <= 500
#         All the values Node.val are unique.
#         target is the value of one of the nodes in the tree.
#         0 <= k <= 1000


# Solution: https://algo.monster/liteproblems/863
# Credit: AlgoMonster
def distanceK(root, target, k):

    def build_parent_map(node, parent) -> None:
        if node is None:
            return
        
        # Map current node to its parent
        parent_map[node] = parent
        
        # Recursively process left and right subtrees
        build_parent_map(node.left, node)
        build_parent_map(node.right, node)
    
    def find_nodes_at_distance_k(node, previous, remaining_distance):
        if node is None:
            return
        
        # If we've reached the required distance, add node value to result
        if remaining_distance == 0:
            result.append(node.val)
            return
        
        # Explore all three possible directions: left child, right child, and parent
        for next_node in (node.left, node.right, parent_map[node]):
            # Avoid going back to the node we came from
            if next_node != previous:
                find_nodes_at_distance_k(next_node, node, remaining_distance - 1)
    
    # Initialize parent mapping dictionary
    parent_map = {}
    
    # Build the parent map for all nodes in the tree
    build_parent_map(root, None)
    
    # Initialize result list to store node values at distance k
    result = []
    
    # Find all nodes at distance k from the target
    find_nodes_at_distance_k(target, None, k)
    
    return result
    # Time: O(n)
    # Space: O(n)


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
