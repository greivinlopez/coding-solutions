# ------------------------------------
# 1530. Number of Good Leaf Nodes Pairs
# ------------------------------------

# Problem: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs
#
# You are given the root of a binary tree and an integer distance. A pair of two
# different leaf nodes of a binary tree is said to be good if the length of the
# shortest path between them is less than or equal to distance.
# 
# Return the number of good leaf node pairs in the tree.
# 
# Example 1:
# 
# Input: root = [1,2,3,null,4], distance = 3
# Output: 1
# 
# Explanation: The leaf nodes of the tree are 3 and 4 and the length of the
# shortest path between them is 3. This is the only good pair.
# 
# Example 2:
# 
# Input: root = [1,2,3,4,5,6,7], distance = 3
# Output: 2
# 
# Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair
# [4,6] is not good because the length of ther shortest path between them is 4.
# 
# Example 3:
# 
# Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
# Output: 1
# 
# Explanation: The only good pair is [2,5].
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 2^10].
#         1 <= Node.val <= 100
#         1 <= distance <= 10

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree, TreeNode
from collections import defaultdict, deque

# Solution: https://youtu.be/f_epkBeS1LQ
# Credit: Navdeep Singh founder of NeetCode
def count_pairs(root, distance):
    adj = defaultdict(list)
    leaf_set = set()

    def build_graph(node):
        if not node:
            return

        if node.left:
            adj[node].append(node.left)
            adj[node.left].append(node)
        
        if node.right:
            adj[node].append(node.right)
            adj[node.right].append(node)
        
        if not node.left and not node.right:
            leaf_set.add(node)
            
        build_graph(node.left)
        build_graph(node.right)

    def bfs(node):
        nonlocal pairs
        visit = set([node])
        q = deque([(node, 0)])

        while q:
            curr, dist = q.popleft()

            if curr != node and curr in leaf_set and dist <= distance:
                pairs += 1

            for nei in adj[curr]:
                if nei not in visit:
                    q.append((nei, dist + 1))
                    visit.add(nei)

    build_graph(root)
    pairs = 0
    
    for node in leaf_set:
        bfs(node)

    return pairs // 2
    # Time: O(n^2)
    # Space: O(n) 


def main():
    root = get_tree("[1,2,3,null,4]")
    result = count_pairs(root, 3)
    print(result) # 1

    root = get_tree("[1,2,3,4,5,6,7]")
    result = count_pairs(root, 3)
    print(result) # 2

    root = get_tree("[7,1,4,6,null,5,3,null,null,null,null,null,2]")
    result = count_pairs(root, 3)
    print(result) # 1

if __name__ == "__main__":
    main()
