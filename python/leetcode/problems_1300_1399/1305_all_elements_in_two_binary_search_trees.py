# ------------------------------------------------
# 1305. All Elements in Two Binary Search Trees 🌲
# ------------------------------------------------

# Problem: https://leetcode.com/problems/all-elements-in-two-binary-search-trees
#
# Given two binary search trees root1 and root2, return a list containing all the
# integers from both trees sorted in ascending order.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/12/18/q2-e1.png
# 
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2019/12/18/q2-e5-.png
# 
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
# 
# 
# Constraints:
#         The number of nodes in each tree is in the range [0, 5000].
#         -10⁵ <= Node.val <= 10⁵

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/1305
# Credit: AlgoMonster
def get_all_elements(root1, root2):
  
    def inorder_traversal(root, elements):
        if root is None:
            return
        
        # Traverse left subtree
        inorder_traversal(root.left, elements)
        # Process current node
        elements.append(root.val)
        # Traverse right subtree
        inorder_traversal(root.right, elements)
    
    # Collect sorted elements from both trees
    first_tree_elements = []
    second_tree_elements = []
    inorder_traversal(root1, first_tree_elements)
    inorder_traversal(root2, second_tree_elements)
    
    # Get lengths of both lists
    len_first = len(first_tree_elements)
    len_second = len(second_tree_elements)
    
    # Initialize pointers for merging
    pointer_first = 0
    pointer_second = 0
    merged_result = []
    
    # Merge two sorted lists
    while pointer_first < len_first and pointer_second < len_second:
        if first_tree_elements[pointer_first] <= second_tree_elements[pointer_second]:
            merged_result.append(first_tree_elements[pointer_first])
            pointer_first += 1
        else:
            merged_result.append(second_tree_elements[pointer_second])
            pointer_second += 1
    
    # Add remaining elements from first list
    while pointer_first < len_first:
        merged_result.append(first_tree_elements[pointer_first])
        pointer_first += 1
    
    # Add remaining elements from second list
    while pointer_second < len_second:
        merged_result.append(second_tree_elements[pointer_second])
        pointer_second += 1
    
    return merged_result
    # Time: O(n + m)
    # Space: O(n + m)


def main():
    root1 = get_tree("[2,1,4]")
    root2 = get_tree("[1,0,3]")
    result = get_all_elements(root1, root2)
    print(result) # [0, 1, 1, 2, 3, 4]

    root1 = get_tree("[1,null,8]")
    root2 = get_tree("[8,1]")
    result = get_all_elements(root1, root2)
    print(result) # [1, 1, 8, 8]

if __name__ == "__main__":
    main()
