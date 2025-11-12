# --------------------------
# 1615. Maximal Network Rank
# --------------------------

# Problem: https://leetcode.com/problems/maximal-network-rank
#
# There is an infrastructure of n cities with some number of roads connecting
# these cities. Each roads[i] = [aᵢ, bᵢ] indicates that there is a bidirectional
# road between cities aᵢ and bᵢ.
# 
# The network rank of two different cities is defined as the total number
# of directly connected roads to either city. If a road is directly connected to
# both cities, it is only counted once.
# 
# The maximal network rank of the infrastructure is the maximum network rank of
# all pairs of different cities.
# 
# Given the integer n and the array roads, return the maximal network rank of the
# entire infrastructure.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/21/ex1.png
# 
# Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
# Output: 4
# Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that
# are connected to either 0 or 1. The road between 0 and 1 is only counted once.
# 
# Example 2:
# 
# Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
# Output: 5
# 
# Explanation: There are 5 roads that are connected to cities 1 or 2.
# 
# Example 3:
# 
# Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
# Output: 5
# 
# Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not
# have to be connected.
# 
# 
# Constraints:
#         2 <= n <= 100
#         0 <= roads.length <= n * (n - 1) / 2
#         roads[i].length == 2
#         0 <= aᵢ, bᵢ <= n-1
#         aᵢ != bᵢ
#         Each pair of cities has at most one road connecting them.

from collections import defaultdict

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def maximal_network_rank(n, roads):
    maxRank = 0
    adj = defaultdict(set)
    
    for road in roads:
        adj[road[0]].add(road[1])
        adj[road[1]].add(road[0])
        
    for node1 in range(n):
        for node2 in range(node1 + 1, n):
            currentRank = len(adj[node1]) + len(adj[node2])
            if node2 in adj[node1]:
                currentRank -= 1
                
            maxRank = max(maxRank, currentRank)
    
    return maxRank
    # Time: O(n²)
    # Space: O(n + r)
    # n = the number of cities (nodes)
    # r = is the number of roads (edges


def main():
    result = maximal_network_rank(n = 4, roads = [[0,1],[0,3],[1,2],[1,3]])
    print(result) # 4

    result = maximal_network_rank(n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]])
    print(result) # 5

    result = maximal_network_rank(n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]])
    print(result) # 5

if __name__ == "__main__":
    main()
