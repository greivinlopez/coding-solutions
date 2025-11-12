# ------------------------
# 785. Is Graph Bipartite?
# ------------------------

# Problem: https://leetcode.com/problems/is-graph-bipartite/
# 
# There is an undirected graph with n nodes, where each node is numbered 
# between 0 and n - 1. You are given a 2D array graph, where graph[u] is an 
# array of nodes that node u is adjacent to. More formally, for each v in 
# graph[u], there is an undirected edge between node u and node v. The graph 
# has the following properties:
# 
#   * There are no self-edges (graph[u] does not contain u).
#   * There are no parallel edges (graph[u] does not contain duplicate values).
#   * If v is in graph[u], then u is in graph[v] (the graph is undirected).
#   * The graph may not be connected, meaning there may be two nodes u and v such 
#     that there is no path between them.
#   * A graph is bipartite if the nodes can be partitioned into two independent 
#     sets A and B such that every edge in the graph connects a node in set A and 
#     a node in set B.
# 
# Return true if and only if it is bipartite.
#  
# 
# Example 1:
# 
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets 
# such that every edge connects a node in one and a node in the other.
# 
# 
# Example 2:
# 
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
# 
#  
# Constraints:
# 
#   graph.length == n
#   1 <= n <= 100
#   0 <= graph[u].length < n
#   0 <= graph[u][i] <= n - 1
#   graph[u] does not contain u.
#   All the values of graph[u] are unique.
#   If graph[u] contains v, then graph[v] contains u.

from collections import deque

# Solution: https://youtu.be/mev55LTubBY
# Credit: Navdeep Singh founder of NeetCode
def is_bipartite(graph):
    # BFS solution
    colors = [-1] * len(graph)
    
    for i in range(len(graph)):
        if colors[i] == -1:
            q = deque([i])
            colors[i] = 0
            
            while q:
                node = q.popleft()
                
                for nbh in graph[node]:
                    if colors[nbh] == -1:
                        colors[nbh] = 1 - colors[node]
                        q.append(nbh)
                    elif colors[nbh] == colors[node]:
                        return False  
    
    return True

def is_bipartite_dfs(graph):
    # DFS solution
    colors = [-1] * len(graph)

    def dfs(node, c):
        colors[node] = c
        
        for nbh in graph[node]:
            if colors[nbh] == -1:
                if not dfs(nbh, 1 - c):
                    return False
            elif colors[nbh] == colors[node]:
                return False
        
        return True

    for i in range(len(graph)):
        if colors[i] == -1:
            if not dfs(i, 0):
                return False
    
    return True


def main():
    result = is_bipartite([[1,2,3],[0,2],[0,1,3],[0,2]])
    print(result) # True

    result = is_bipartite([[1,3],[0,2],[1,3],[0,2]])
    print(result) # False

if __name__ == "__main__":
    main()
