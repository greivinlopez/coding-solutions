# ------------------------
# 547. Number of Provinces
# ------------------------

# Problem: https://leetcode.com/problems/number-of-provinces
#
# There are n cities. Some of them are connected, while some are not. If city a is
# connected directly with city b, and city b is connected directly with city c,
# then city a is connected indirectly with city c.
# 
# A province is a group of directly or indirectly connected cities and no other
# cities outside of the group.
# 
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the iᵗʰ
# city and the jᵗʰ city are directly connected, and isConnected[i][j] = 0
# otherwise.
# 
# Return the total number of provinces.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg
# 
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg
# 
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# 
# 
# Constraints:
#         1 <= n <= 200
#         n == isConnected.length
#         n == isConnected[i].length
#         isConnected[i][j] is 1 or 0.
#         isConnected[i][i] == 1
#         isConnected[i][j] == isConnected[j][i]


# Solution: https://algo.monster/liteproblems/547
# Credit: AlgoMonster
def find_circle_num(isConnected):
    def dfs(city_index):
        visited[city_index] = True
        
        # Explore all neighboring cities
        for neighbor_index, is_connected_to_neighbor in enumerate(isConnected[city_index]):
            # If the neighbor hasn't been visited and is connected to current city
            if not visited[neighbor_index] and is_connected_to_neighbor:
                dfs(neighbor_index)
    
    # Get the number of cities
    num_cities = len(isConnected)
    
    # Initialize visited array to track which cities have been explored
    visited = [False] * num_cities
    
    # Counter for the number of provinces
    province_count = 0
    
    # Iterate through all cities
    for city_index in range(num_cities):
        # If the city hasn't been visited, it's part of a new province
        if not visited[city_index]:
            # Explore all cities in this province
            dfs(city_index)
            # Increment the province count
            province_count += 1
    
    return province_count
    # Time: O(n²)
    # Space: O(n)


def main():
    result = find_circle_num(isConnected = [[1,1,0],[1,1,0],[0,0,1]])
    print(result) # 2

    result = find_circle_num(isConnected = [[1,0,0],[0,1,0],[0,0,1]])
    print(result) # 3

if __name__ == "__main__":
    main()
