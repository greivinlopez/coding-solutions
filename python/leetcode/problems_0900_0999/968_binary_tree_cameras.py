# ---------------------------
# 968. Binary Tree Cameras 📷
# ---------------------------

# Problem: https://leetcode.com/problems/binary-tree-cameras
#
# You are given the root of a binary tree. We install cameras on the tree nodes
# where each camera at a node can monitor its parent, itself, and its immediate
# children.
# 
# Return the minimum number of cameras needed to monitor all nodes of the tree.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png
# 
# Input: root = [0,0,null,0,0]
# Output: 1
# 
# Explanation: One camera is enough to monitor all nodes if placed as shown.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png
# 
# Input: root = [0,0,null,0,null,0,null,null,0]
# Output: 2
# 
# Explanation: At least two cameras are needed to monitor all nodes of the tree.
# The above image shows one of the valid configurations of camera placement.
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 1000].
#         Node.val == 0

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/968
# Credit: AlgoMonster
def min_camera_cover(root):
    from math import inf

    def dfs(node):       
        # Base case: null node
        if node is None:
            return inf, 0, 0
        
        # Recursively solve for left and right subtrees
        left_camera, left_covered, left_not_covered = dfs(node.left)
        right_camera, right_covered, right_not_covered = dfs(node.right)
        
        # Case 1: Place camera at current node
        # Camera covers current node and both children
        # Children can be in any state since they're covered by this camera
        camera_here = min(left_camera, left_covered, left_not_covered) + \
                        min(right_camera, right_covered, right_not_covered) + 1
        
        # Case 2: Current node is covered but has no camera
        # At least one child must have a camera to cover current node
        covered_no_camera = min(
            left_camera + right_covered,  # left child has camera
            left_covered + right_camera,  # right child has camera
            left_camera + right_camera    # both children have cameras
        )
        
        # Case 3: Current node is not covered
        # Both children must be covered (but don't have cameras)
        # This forces parent to have a camera
        not_covered = left_covered + right_covered
        
        return camera_here, covered_no_camera, not_covered
    
    # Get results for root node
    camera_at_root, root_covered, _ = dfs(root)
    
    # Root must be covered, so return minimum of:
    # - placing camera at root
    # - root being covered by its children
    return min(camera_at_root, root_covered)
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[0,0,null,0,0]")
    result = min_camera_cover(root)
    print(result) # 1

    root = get_tree("[0,0,null,0,null,0,null,null,0]")
    result = min_camera_cover(root)
    print(result) # 2

if __name__ == "__main__":
    main()
