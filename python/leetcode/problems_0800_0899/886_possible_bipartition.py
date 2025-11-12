# -------------------------
# 886. Possible Bipartition
# -------------------------

# Problem: https://leetcode.com/problems/possible-bipartition
#
# We want to split a group of n people (labeled from 1 to n) into two groups of
# any size. Each person may dislike some other people, and they should not go into
# the same group.
# 
# Given the integer n and the array dislikes where dislikes[i] = [aᵢ, bᵢ]
# indicates that the person labeled aᵢ does not like the person labeled bᵢ, return
# true if it is possible to split everyone into two groups in this way.
# 
# Example 1:
# 
# Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# 
# Explanation: The first group has [1,4], and the second group has [2,3].
# 
# Example 2:
# 
# Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# 
# Explanation: We need at least 3 groups to divide them. We cannot put them in two
# groups.
# 
# 
# Constraints:
#         1 <= n <= 2000
#         0 <= dislikes.length <= 10⁴
#         dislikes[i].length == 2
#         1 <= aᵢ < bᵢ <= n
#         All the pairs of dislikes are unique.

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/886
# Credit: AlgoMonster
def possible_bipartition(n, dislikes):

    def dfs(node, assigned_color):
        # Assign color to current node
        colors[node] = assigned_color
        
        # Check all neighbors
        for neighbor in adjacency_list[node]:
            # If neighbor has same color, graph is not bipartite
            if colors[neighbor] == assigned_color:
                return False
            
            # If neighbor is uncolored, recursively color it with opposite color
            # Use 3 - assigned_color to alternate between colors 1 and 2
            if colors[neighbor] == 0 and not dfs(neighbor, 3 - assigned_color):
                return False
        
        return True
    
    # Build adjacency list for undirected graph
    adjacency_list = defaultdict(list)
    
    # Initialize colors array (0 = uncolored, 1 = color1, 2 = color2)
    colors = [0] * n
    
    # Convert to 0-indexed and build adjacency list
    for person_a, person_b in dislikes:
        person_a -= 1  # Convert to 0-indexed
        person_b -= 1  # Convert to 0-indexed
        adjacency_list[person_a].append(person_b)
        adjacency_list[person_b].append(person_a)
    
    # Try to color each connected component
    # If node is already colored (color != 0), skip it
    # Otherwise, start DFS coloring from this node with color 1
    return all(color != 0 or dfs(node_idx, 1) 
                for node_idx, color in enumerate(colors))
    # Time: O(v + e)
    # Space: O(v + e)
    # v = the number of people (n)
    # e = the number of dislike relationships.

# Alternative Solution: Using Union Find. 
# Solution: https://leetcode.com/problems/possible-bipartition/solutions/655842/python-union-find-dfs-bfs-with-explanation
# Credit: https://leetcode.com/u/idontknoooo/


def main():
    result = possible_bipartition(n = 4, dislikes = [[1,2],[1,3],[2,4]])
    print(result) # True

    result = possible_bipartition(n = 3, dislikes = [[1,2],[1,3],[2,3]])
    print(result) # False

if __name__ == "__main__":
    main()
