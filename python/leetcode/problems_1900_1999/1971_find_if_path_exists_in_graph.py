# ----------------------------------
# 1971. Find if Path Exists in Graph
# ----------------------------------

# Problem: https://leetcode.com/problems/find-if-path-exists-in-graph/
# 
# There is a bi-directional graph with n vertices, where each vertex is labeled 
# from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D 
# integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional 
# edge between vertex ui and vertex vi. Every vertex pair is connected by at 
# most one edge, and no vertex has an edge to itself.
# 
# You want to determine if there is a valid path that exists from vertex source 
# to vertex destination.
# 
# Given edges and the integers n, source, and destination, return true if there 
# is a valid path from source to destination, or false otherwise.
# 
#  
# Example 1:
# 
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2
# 
# Example 2:
# 
# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.
# 
# 
# Constraints:
# 
#   1 <= n <= 2 * 10^5
#   0 <= edges.length <= 2 * 10^5
#   edges[i].length == 2
#   0 <= ui, vi <= n - 1
#   ui != vi
#   0 <= source, destination <= n - 1
#   There are no duplicate edges.
#   There are no self edges.

from collections import defaultdict
from collections import deque

# Solution: https://youtu.be/knLFe7hEp3Y
# Credit: Greg Hogg
def valid_path(n, edges, source, destination):
    # Recursive DFS
    if source == destination:
        return True
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    seen = set()
    seen.add(source)

    def dfs(i):
        if i == destination:
            return True
        
        for nei_node in graph[i]:
            if nei_node not in seen:
                seen.add(nei_node)
                if dfs(nei_node):
                    return True
        
        return False
    
    return dfs(source)

def valid_path_iter(n, edges, source, destination):
    # Iterative DFS with Stack
    if source == destination:
        return True
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    seen = set()
    seen.add(source)
    stack = [source]

    while stack:
        node = stack.pop()
        if node == destination:
            return True
        for nei_node in graph[node]:
            if nei_node not in seen:
                seen.add(nei_node)
                stack.append(nei_node)
    
    return False

def valid_path_bfs(n, edges, source, destination):
    # BFS With Queue
    if source == destination:
        return True
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    seen = set()
    seen.add(source)
    q = deque()
    q.append(source)

    while q:
        node = q.popleft()
        if node == destination:
            return True
        for nei_node in graph[node]:
            if nei_node not in seen:
                seen.add(nei_node)
                q.append(nei_node)
    
    return False 
    # Time: O(N + E)
    # Space: O(N + E)

def main():
    result = valid_path(n=3, edges=[[0,1],[1,2],[2,0]], source=0, destination=2)
    print(result) # True

    result = valid_path(n=6, edges=[[0,1],[0,2],[3,5],[5,4],[4,3]], source=0, destination=5)
    print(result) # False

if __name__ == "__main__":
    main()
