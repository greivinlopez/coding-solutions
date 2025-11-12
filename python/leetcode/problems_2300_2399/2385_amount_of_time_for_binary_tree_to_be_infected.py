# ---------------------------------------------------
# 2385. Amount of Time for Binary Tree to Be Infected
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected
#
# You are given the root of a binary tree with unique values, and an integer
# start. At minute 0, an infection starts from the node with value start.
# 
# Each minute, a node becomes infected if:
#         The node is currently uninfected.
#         The node is adjacent to an infected node.
# 
# Return the number of minutes needed for the entire tree to be infected.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2022/06/25/image-20220625231744-1.png
# 
# Input: root = [1,5,3,null,4,10,6,9,2], start = 3
# Output: 4
# 
# Explanation: The following nodes are infected during:
# - Minute 0: Node 3
# - Minute 1: Nodes 1, 10 and 6
# - Minute 2: Node 5
# - Minute 3: Node 4
# - Minute 4: Nodes 9 and 2
# It takes 4 minutes for the whole tree to be infected so we return 4.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2022/06/25/image-20220625231812-2.png
# 
# Input: root = [1], start = 1
# Output: 0
# 
# Explanation: At minute 0, the only node in the tree is infected so we return 0.
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10⁵].
#         1 <= Node.val <= 10⁵
#         Each node has a unique value.
#         A node with a value of start exists in the tree.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree, TreeNode
from collections import defaultdict, deque


# Credit: Jeel Gajera -> https://github.com/JeelGajera
def amount_of_time(root, start):

    def convertBSTtoGraph(root, graph):
        if root:
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                convertBSTtoGraph(root.left, graph)

            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                convertBSTtoGraph(root.right, graph)

    def bfs(graph, start):
        visited = set()

        queue = deque([(start, 0)])
        visited.add(start)

        max_distance = 0

        while queue:
            current, dist = queue.popleft()

            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

                    if dist + 1 > max_distance:
                        max_distance = dist + 1

        return max_distance
    
    graph = defaultdict(list)
    convertBSTtoGraph(root, graph)

    return bfs(graph, start)
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[1,5,3,null,4,10,6,9,2]")
    result = amount_of_time(root, 3)
    print(result) # 4

    root = get_tree("[1]")
    result = amount_of_time(root, 1)
    print(result) # 0

if __name__ == "__main__":
    main()
