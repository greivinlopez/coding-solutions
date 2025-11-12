# ----------------------------------------------------
# 1319. Number of Operations to Make Network Connected
# ----------------------------------------------------

# Problem: https://leetcode.com/problems/number-of-operations-to-make-network-connected
#
# There are n computers numbered from 0 to n - 1 connected by ethernet cables
# connections forming a network where connections[i] = [aᵢ, bᵢ] represents a
# connection between computers aᵢ and bᵢ. Any computer can reach any other
# computer directly or indirectly through the network.
# 
# You are given an initial computer network connections. You can extract certain
# cables between two directly connected computers, and place them between any pair
# of disconnected computers to make them directly connected.
# 
# Return the minimum number of times you need to do this in order to make all the
# computers connected. If it is not possible, return -1.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/01/02/sample_1_1677.png
# 
# Input: n = 4, connections = [[0,1],[0,2],[1,2]]
# Output: 1
# 
# Explanation: Remove cable between computer 1 and 2 and place between computers 1
# and 3.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/01/02/sample_2_1677.png
# 
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# Output: 2
# 
# Example 3:
# 
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
# Output: -1
# 
# Explanation: There are not enough cables.
# 
# 
# Constraints:
#         1 <= n <= 10⁵
#         1 <= connections.length <= min(n * (n - 1) / 2, 10⁵)
#         connections[i].length == 2
#         0 <= aᵢ, bᵢ < n
#         aᵢ != bᵢ
#         There are no repeated connections.
#         No two computers are connected by more than one cable.


# Solution: https://algo.monster/liteproblems/1319
# Credit: AlgoMonster
def make_connected(n, connections):

    def find(node: int) -> int:
        if parent[node] != node:
            # Path compression: directly connect node to root
            parent[node] = find(parent[node])
        return parent[node]
    
    # Count redundant connections (cables that can be reused)
    redundant_cables = 0
    
    # Initialize parent array where each node is its own parent
    parent = list(range(n))
    
    # Number of connected components (starts at n, decreases with each union)
    num_components = n
    
    # Process each connection
    for computer_a, computer_b in connections:
        # Find root parents of both computers
        root_a = find(computer_a)
        root_b = find(computer_b)
        
        if root_a == root_b:
            # Already in same component, this cable is redundant
            redundant_cables += 1
        else:
            # Union: connect the two components
            parent[root_a] = root_b
            # Decrease component count
            num_components -= 1
    
    # Need (num_components - 1) cables to connect all components
    # Check if we have enough redundant cables
    cables_needed = num_components - 1
    
    if cables_needed > redundant_cables:
        return -1  # Not enough cables to connect all components
    else:
        return cables_needed  # Number of operations needed
    # Time: O(m * α(n))
    # Space: O(n)
    # m = the number of connections
    # α(n) is the inverse Ackermann function


def main():
    result = make_connected(n = 4, connections = [[0,1],[0,2],[1,2]])
    print(result) # 1

    result = make_connected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]])
    print(result) # 2

    result = make_connected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2]])
    print(result) # -1

if __name__ == "__main__":
    main()
