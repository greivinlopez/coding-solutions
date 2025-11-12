# ---------------------------------------------------
# 331. Verify Preorder Serialization of a Binary Tree
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree
#
# One way to serialize a binary tree is to use preorder traversal. When we
# encounter a non-null node, we record the node's value. If it is a null node, we
# record using a sentinel value such as '#'.
# 
# https://assets.leetcode.com/uploads/2021/03/12/pre-tree.jpg
# 
# For example, the above binary tree can be serialized to the string
# "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.
# 
# Given a string of comma-separated values preorder, return true if it is a
# correct preorder traversal serialization of a binary tree.
# 
# It is guaranteed that each comma-separated value in the string must be either an
# integer or a character '#' representing null pointer.
# 
# You may assume that the input format is always valid.
#         
#   * For example, it could never contain two consecutive commas, such as "1,,3".
# 
# Note: You are not allowed to reconstruct the tree.
# 
# Example 1:
# 
# Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
# 
# Example 2:
# 
# Input: preorder = "1,#"
# Output: false
# 
# Example 3:
# 
# Input: preorder = "9,#,#,1"
# Output: false
# 
# 
# Constraints:
#   1 <= preorder.length <= 10⁴
#   preorder consist of integers in the range [0, 100] and '#' separated by commas ','.


# Solution: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/solutions/3244705/331-time-98-solution-with-step-by-step-explanation
def is_valid_serialization(preorder):
    degree = 1
    
    for node in preorder.split(','):
        degree -= 1      
        if degree < 0:
            return False    
        if node != '#':
            degree += 2

    return degree == 0
    # Time: O(n)
    # Space: O(n)


def main():
    result = is_valid_serialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
    print(result) # True

    result = is_valid_serialization("1,#")
    print(result) # False

    result = is_valid_serialization("9,#,#,1")
    print(result) # False

if __name__ == "__main__":
    main()
