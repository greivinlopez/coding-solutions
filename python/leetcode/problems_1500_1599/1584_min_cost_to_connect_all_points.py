# ------------------------------------
# 1584. Min Cost To Connect All Points
# ------------------------------------

# Problem: https://leetcode.com/problems/min-cost-to-connect-all-points
#
# You are given an array points representing integer coordinates of some points on
# a 2D-plane, where points[i] = [xᵢ, yᵢ].
# 
# The cost of connecting two points [xᵢ, yᵢ] and [xⱼ, yⱼ] is the manhattan
# distance between them: |xᵢ - xⱼ| + |yᵢ - yⱼ|, where |val| denotes the absolute
# value of val.
# 
# Return the minimum cost to make all points connected. All points are connected
# if there is exactly one simple path between any two points.
# 
# Example 1:
# 
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation:
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# 
# Example 2:
# 
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
# 
# 
# Constraints:
#         1 <= points.length <= 1000
#         -10⁶ <= xᵢ, yᵢ <= 10⁶
#         All pairs (xᵢ, yᵢ) are distinct.

import heapq

# Solution: https://youtu.be/f7JOBJIC-NA
# Credit: Navdeep Singh founder of NeetCode
def min_cost_connect_points(points):
    N = len(points)
    adj = {i: [] for i in range(N)}  # i : list of [cost, node]
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i + 1, N):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])

    # Prim's
    res = 0
    visit = set()
    minH = [[0, 0]]  # [cost, point]
    while len(visit) < N:
        cost, i = heapq.heappop(minH)
        if i in visit:
            continue
        res += cost
        visit.add(i)
        for neiCost, nei in adj[i]:
            if nei not in visit:
                heapq.heappush(minH, [neiCost, nei])
    return res
    # Time: O(n² * log(n))
    # Space: O(n²)

# Solution: https://youtu.be/f7JOBJIC-NA
# Credit: Greg Hogg
def min_cost_connect_points_alt(points):
    # Prim's algorithm to create a MST (Minimum Spanning Tree)
    n = len(points)
    total_cost = 0
    heap = [(0, 0)]
    seen = set()

    while len(seen) < n:
        dist, i = heapq.heappop(heap)
        if i in seen:
            continue
        
        seen.add(i)
        total_cost += dist
        xi, yi = points[i]

        for j in range(n):
            if j not in seen:
                xj, yj = points[j]
                nei_dist = abs(xi-xj) + abs(yi-yj)
                heapq.heappush(heap, (nei_dist, j))
    
    return total_cost       
    # Time: O(n² * log(n)) where n is the number of points
    #    or O(E log(E)) where E is the number of edges, which is n²
    # Space: O(n²) or O(E)


def main():
    result = min_cost_connect_points([[0,0],[2,2],[3,10],[5,2],[7,0]])
    print(result) # 20

    result = min_cost_connect_points([[3,12],[-2,5],[-4,1]])
    print(result) # 18

if __name__ == "__main__":
    main()
