# -----------------------------------------
# 1104. Path In Zigzag Labelled Binary Tree
# -----------------------------------------

# Problem: https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree
#
# In an infinite binary tree where every node has two children, the nodes are
# labelled in row order.
# 
# In the odd numbered rows (ie., the first, third, fifth,...), the labelling is
# left to right, while in the even numbered rows (second, fourth, sixth,...), the
# labelling is right to left.
# 
# https://assets.leetcode.com/uploads/2019/06/24/tree.png
# 
# Given the label of a node in this tree, return the labels in the path from the
# root of the tree to the node with that label.
# 
# Example 1:
# 
# Input: label = 14
# Output: [1,3,4,14]
# 
# Example 2:
# 
# Input: label = 26
# Output: [1,2,6,10,26]
# 
# 
# Constraints:
#         1 <= label <= 10⁶


# Solution: https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/solutions/634695/python-easy-to-understand-faster-than-91-93-memory-usage-less-than-100
# Credit: user8083w -> https://leetcode.com/u/user8083w/
def path_in_zig_zag_tree(label):
    #Base case
    if label == 1:
        return [1]
    
    # Calculate the level that the label is present in 
    level = 1
    while True:
        if (2**level - 1 >= label):
            break
        level += 1
            
    pathArray = [label]
    # reduce level by 1 since we have already added label to the path array
    level -= 1
    
    # Base case
    while level != 0:
        
        # calculating parent 
        label = 2**(level-1) + ((2**(level+1) - 1 - label)//2)
        # insert parent to the top
        pathArray.insert(0, label)
        level -= 1
        
    return pathArray
    # Time: O(log(n))
    # Space: O(1)


def main():
    result = path_in_zig_zag_tree(label = 14)
    print(result) # [1, 3, 4, 14]

    result = path_in_zig_zag_tree(label = 26)
    print(result) # [1, 2, 6, 10, 26]

if __name__ == "__main__":
    main()
