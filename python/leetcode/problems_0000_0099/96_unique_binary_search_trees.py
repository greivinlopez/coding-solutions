# ------------------------------
# 96. Unique Binary Search Trees
# ------------------------------

# Problem: https://leetcode.com/problems/unique-binary-search-trees
#
# Given an integer n, return the number of structurally unique BST's (binary
# search trees) which has exactly n nodes of unique values from 1 to n.
# 
# Example 1:
# 
# Input: n = 3
# Output: 5
# 
# Example 2:
# 
# Input: n = 1
# Output: 1
# 
# 
# Constraints:
# 
#         1 <= n <= 19


# Solution: https://youtu.be/Ox0TenN3Zpg
# Credit: Navdeep Singh founder of NeetCode
def num_trees(n):
    num_tree = [1] * (n + 1)
    
    # 0 nodes = 1 tree
    # 1 nodes = 1 tree
    for nodes in range(2, n + 1):
        total = 0
        for root in range(1, nodes + 1):
            left = root - 1
            right = nodes - root
            total += num_tree[left] * num_tree[right]
        num_tree[nodes] = total

    return num_tree[n]
    # Time: O(n ^ 2)
    # Space: O(n)


def main():
    result = num_trees(3)
    print(result) # 5

    result = num_trees(1)
    print(result) # 1

if __name__ == "__main__":
    main()
