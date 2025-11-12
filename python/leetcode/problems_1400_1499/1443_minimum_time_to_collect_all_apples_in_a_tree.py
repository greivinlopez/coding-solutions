# -----------------------------------------------------
# 1443. Minimum Time to Collect All Apples in a Tree 🍎
# -----------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree
#
# Given an undirected tree consisting of n vertices numbered from 0 to n-1, which
# has some apples in their vertices. You spend 1 second to walk over one edge of
# the tree. Return the minimum time in seconds you have to spend to collect all
# apples in the tree, starting at vertex 0 and coming back to this vertex.
# 
# The edges of the undirected tree are given in the array edges, where edges[i] =
# [aᵢ, bᵢ] means that exists an edge connecting the vertices aᵢ and bᵢ.
# Additionally, there is a boolean array hasApple, where hasApple[i] = true means
# that vertex i has an apple; otherwise, it does not have any apple.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/04/23/min_time_collect_apple_1.png
# 
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,true,false,true,true,false]
# Output: 8
# 
# Explanation: The figure above represents the given tree where red vertices have
# an apple. One optimal path to collect all apples is shown by the green arrows.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/04/23/min_time_collect_apple_2.png
# 
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,true,false,false,true,false]
# Output: 6
# 
# Explanation: The figure above represents the given tree where red vertices have
# an apple. One optimal path to collect all apples is shown by the green arrows.
# 
# Example 3:
# 
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,false,false,false,false,false]
# Output: 0
# 
# 
# Constraints:
#         1 <= n <= 10⁵
#         edges.length == n - 1
#         edges[i].length == 2
#         0 <= aᵢ < bᵢ <= n - 1
#         hasApple.length == n


# Solution: https://youtu.be/Xdt5Z583auM
# Credit: Navdeep Singh founder of NeetCode
def min_time(n, edges, hasApple):
    adj = {i: [] for i in range(n)}
    
    for par, child in edges:
        adj[par].append(child)
        adj[child].append(par)

    def dfs(cur, par):
        time = 0
        
        for child in adj[cur]:
            if child == par:
                continue
            
            childTime = dfs(child, cur)
            if childTime or hasApple[child]:
                time += 2 + childTime
        
        return time
    
    return dfs(0, -1)
    # Time: O(n)
    # Space: O(n)


def main():
    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False,False,True,False,True,True,False]
    result = min_time(n, edges, hasApple)
    print(result) # 8

    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False,False,True,False,False,True,False]
    result = min_time(n, edges, hasApple)
    print(result) # 6

    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False,False,False,False,False,False,False]
    result = min_time(n, edges, hasApple)
    print(result) # 0

if __name__ == "__main__":
    main()
