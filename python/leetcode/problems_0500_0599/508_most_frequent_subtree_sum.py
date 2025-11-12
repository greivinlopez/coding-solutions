# ------------------------------
# 508. Most Frequent Subtree Sum
# ------------------------------

# Problem: https://leetcode.com/problems/most-frequent-subtree-sum
#
# Given the root of a binary tree, return the most frequent subtree sum. If there
# is a tie, return all the values with the highest frequency in any order.
# 
# The subtree sum of a node is defined as the sum of all the node values formed by
# the subtree rooted at that node (including the node itself).
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/04/24/freq1-tree.jpg
# 
# Input: root = [5,2,-3]
# Output: [2,-3,4]
# 
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/04/24/freq2-tree.jpg
# 
# Input: root = [5,2,-5]
# Output: [2]
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10⁴].
#         -10⁵ <= Node.val <= 10⁵

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree
from collections import Counter

# Solution: https://algo.monster/liteproblems/508
# Credit: AlgoMonster
def find_frequent_tree_sum(root):
   
    def calculate_subtree_sum(node):
        # Base case: empty subtree has sum of 0
        if node is None:
            return 0
        
        # Recursively calculate left and right subtree sums
        left_sum = calculate_subtree_sum(node.left)
        right_sum = calculate_subtree_sum(node.right)
        
        # Calculate current subtree sum
        current_subtree_sum = left_sum + right_sum + node.val
        
        # Update frequency counter for this sum
        sum_frequency[current_subtree_sum] += 1
        
        return current_subtree_sum
    
    # Initialize frequency counter for subtree sums
    sum_frequency = Counter()
    
    # Perform DFS to calculate all subtree sums
    calculate_subtree_sum(root)
    
    # Find the maximum frequency
    max_frequency = max(sum_frequency.values())
    
    # Return all sums that have the maximum frequency
    return [sum_value for sum_value, frequency in sum_frequency.items() 
            if frequency == max_frequency]
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[5,2,-3]")
    result = find_frequent_tree_sum(root)
    print(result) # [2,-3,4]

    root = get_tree("[5,2,-5]")
    result = find_frequent_tree_sum(root)
    print(result) # [2]

if __name__ == "__main__":
    main()
