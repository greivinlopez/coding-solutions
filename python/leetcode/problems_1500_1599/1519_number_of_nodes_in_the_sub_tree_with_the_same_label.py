# ---------------------------------------------------------
# 1519. Number of Nodes in the Sub-Tree With the Same Label
# ---------------------------------------------------------

# Problem: https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label
#
# You are given a tree (i.e. a connected, undirected graph that has no cycles)
# consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root
# of the tree is the node 0, and each node of the tree has a label which is a
# lower-case character given in the string labels (i.e. The node with the number i
# has the label labels[i]).
# 
# The edges array is given on the form edges[i] = [ai, bi], which means there is
# an edge between nodes ai and bi in the tree.
# 
# Return an array of size n where ans[i] is the number of nodes in the subtree of
# the ith node which have the same label as node i.
# 
# A subtree of a tree T is the tree consisting of a node in T and all of its
# descendant nodes.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/07/01/q3e1.jpg
# 
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
# Output: [2,1,1,1,1,1,1]
# 
# Explanation: Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as
# well, thus the answer is 2. Notice that any node is part of its sub-tree.
# Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as
# nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node
# itself).
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/07/01/q3e2.jpg
# 
# Input: n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
# Output: [4,2,1,1]
# 
# Explanation: The sub-tree of node 2 contains only node 2, so the answer is 1.
# The sub-tree of node 3 contains only node 3, so the answer is 1.
# The sub-tree of node 1 contains nodes 1 and 2, both have label 'b', thus the
# answer is 2.
# The sub-tree of node 0 contains nodes 0, 1, 2 and 3, all with label 'b', thus
# the answer is 4.
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2020/07/01/q3e3.jpg
# 
# Input: n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
# Output: [3,2,1,1,1]
# 
# 
# Constraints:
#         1 <= n <= 10⁵
#         edges.length == n - 1
#         edges[i].length == 2
#         0 <= aᵢ, bᵢ < n
#         aᵢ != bᵢ
#         labels.length == n
#         labels is consisting of only of lowercase English letters.

from collections import defaultdict, Counter

# Solution: https://algo.monster/liteproblems/1519
# Credit: AlgoMonster
def count_sub_trees(n, edges, labels):
 
    def dfs(node, parent):
        # Store the count of current node's label before exploring subtree
        result[node] -= label_counter[labels[node]]
        
        # Increment counter for current node's label
        label_counter[labels[node]] += 1
        
        # Recursively process all children
        for neighbor in adjacency_list[node]:
            if neighbor != parent:
                dfs(neighbor, node)
        
        # After processing subtree, the difference gives us the count in this subtree
        result[node] += label_counter[labels[node]]
    
    # Build adjacency list for the undirected tree
    adjacency_list = defaultdict(list)
    for node_a, node_b in edges:
        adjacency_list[node_a].append(node_b)
        adjacency_list[node_b].append(node_a)
    
    # Initialize counter for tracking label occurrences during DFS
    label_counter = Counter()
    
    # Initialize result array to store counts for each node
    result = [0] * n
    
    # Start DFS from root node (node 0) with no parent (-1)
    dfs(0, -1)
    
    return result
    # Time: O(n)
    # Space: O(n)


def main():
    result = count_sub_trees(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd")
    print(result) # [2, 1, 1, 1, 1, 1, 1]

    result = count_sub_trees(n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb")
    print(result) # [4, 2, 1, 1]

    result = count_sub_trees(n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab")
    print(result) # [3, 2, 1, 1, 1]

if __name__ == "__main__":
    main()
