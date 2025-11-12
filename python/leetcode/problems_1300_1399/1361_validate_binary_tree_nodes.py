# --------------------------------
# 1361. Validate Binary Tree Nodes
# --------------------------------

# Problem: https://leetcode.com/problems/validate-binary-tree-nodes
#
# You have n binary tree nodes numbered from 0 to n - 1 where node i has two
# children leftChild[i] and rightChild[i], return true if and only if all the
# given nodes form exactly one valid binary tree.
# 
# If node i has no left child then leftChild[i] will equal -1, similarly for the
# right child.
# 
# Note that the nodes have no values and that we only use the node numbers in this
# problem.
# 
# Example 1:
# 
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true
# 
# Example 2:
# 
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: false
# 
# Example 3:
# 
# Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
# Output: false
# 
# 
# Constraints:
#         n == leftChild.length == rightChild.length
#         1 <= n <= 10^4
#         -1 <= leftChild[i], rightChild[i] <= n - 1


# Solution: https://youtu.be/Mw67DTgUEqk
# Credit: Navdeep Singh founder of NeetCode
def validate_binary_tree_nodes(n, leftChild, rightChild):
    hasParent = set(leftChild + rightChild)
    hasParent.discard(-1)
    if len(hasParent) == n:
        return False

    root = -1
    for i in range(n):
        if i not in hasParent:
            root = i
            break

    visit = set()
    def dfs(i):
        if i == -1:
            return True
        if i in visit:
            return False
        visit.add(i)
        return dfs(leftChild[i]) and dfs(rightChild[i])

    return dfs(root) and len(visit) == n
    # Time: O(n)
    # Space: O(n)


def main():
    result = validate_binary_tree_nodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1])
    print(result) # True

    result = validate_binary_tree_nodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1])
    print(result) # False

    result = validate_binary_tree_nodes(n = 2, leftChild = [1,0], rightChild = [-1,-1])
    print(result) # False

if __name__ == "__main__":
    main()
