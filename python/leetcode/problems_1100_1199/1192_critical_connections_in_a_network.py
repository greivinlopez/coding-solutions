# ---------------------------------------
# 1192. Critical Connections in a Network
# ---------------------------------------

# Problem: https://leetcode.com/problems/critical-connections-in-a-network
#
# There are n servers numbered from 0 to n - 1 connected by undirected server-to-
# server connections forming a network where connections[i] = [aᵢ, bᵢ] represents
# a connection between servers aᵢ and bᵢ. Any server can reach other servers
# directly or indirectly through the network.
# 
# A critical connection is a connection that, if removed, will make some servers
# unable to reach some other server.
# 
# Return all critical connections in the network in any order.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/09/03/1537_ex1_2.png
# 
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# 
# Explanation: [[3,1]] is also accepted.
# 
# Example 2:
# 
# Input: n = 2, connections = [[0,1]]
# Output: [[0,1]]
# 
# 
# Constraints:
#         2 <= n <= 10⁵
#         n - 1 <= connections.length <= 10⁵
#         0 <= aᵢ, bᵢ <= n - 1
#         aᵢ != bᵢ
#         There are no repeated connections.


# Solution: https://algo.monster/liteproblems/1192
# Credit: AlgoMonster
def critical_connections(n, connections):
    
    def tarjan_dfs(current_node, parent_node):
        nonlocal timestamp
        
        # Assign discovery time and initialize low-link value
        timestamp += 1
        discovery_time[current_node] = timestamp
        low_link[current_node] = timestamp
        
        # Explore all neighbors
        for neighbor in adjacency_list[current_node]:
            # Skip the edge back to parent (avoid going back on the same edge)
            if neighbor == parent_node:
                continue
            
            if discovery_time[neighbor] == 0:  # Neighbor not yet visited
                # Recursively visit the neighbor
                tarjan_dfs(neighbor, current_node)
                
                # Update low-link value after returning from DFS
                low_link[current_node] = min(
                    low_link[current_node], 
                    low_link[neighbor]
                )
                
                # Check if the edge is a bridge
                # If low_link[neighbor] > discovery_time[current], then neighbor
                # cannot reach current or any ancestor without using edge (current, neighbor)
                if low_link[neighbor] > discovery_time[current_node]:
                    critical_edges.append([current_node, neighbor])
            else:
                # Neighbor already visited (back edge)
                # Update low-link value using discovery time of neighbor
                low_link[current_node] = min(
                    low_link[current_node], 
                    discovery_time[neighbor]
                )
    
    # Build adjacency list representation of the graph
    adjacency_list = [[] for _ in range(n)]
    for node_a, node_b in connections:
        adjacency_list[node_a].append(node_b)
        adjacency_list[node_b].append(node_a)
    
    # Initialize arrays for Tarjan's algorithm
    discovery_time = [0] * n  # Discovery time for each node (0 means unvisited)
    low_link = [0] * n        # Lowest discovery time reachable from subtree
    timestamp = 0             # Global timestamp counter
    critical_edges = []       # Result list to store bridges
    
    # Start DFS from node 0 (assuming graph is connected)
    # Use -1 as parent for the root node
    tarjan_dfs(0, -1)
    
    return critical_edges
    # Time: O(v + e)
    # Space: O(v + e)


def main():
    result = critical_connections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]])
    print(result) # [[1, 3]]

    result = critical_connections(n = 2, connections = [[0,1]])
    print(result) # [[0, 1]]

if __name__ == "__main__":
    main()
