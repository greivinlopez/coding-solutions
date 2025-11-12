# ------------------------------------------------
# 2492. Minimum Score of a Path Between Two Cities
# ------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities
#
# You are given a positive integer n representing n cities numbered from 1 to n.
# You are also given a 2D array roads where roads[i] = [aᵢ, bᵢ, distanceᵢ]
# indicates that there is a bidirectional road between cities aᵢ and bᵢ with a
# distance equal to distanceᵢ. The cities graph is not necessarily connected.
# 
# The score of a path between two cities is defined as the minimum distance of a
# road in this path.
# 
# Return the minimum possible score of a path between cities 1 and n.
# 
# Note:
#         
#   * A path is a sequence of roads between two cities.
#   * It is allowed for a path to contain the same road multiple times, and
#     you can visit cities 1 and n multiple times along the path.
#   * The test cases are generated such that there is at least one path
#     between 1 and n.
# 
# Example 1:
# 
# Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
# Output: 5
# 
# Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4.
# The score of this path is min(9,5) = 5.
# It can be shown that no other path has less score.
# 
# Example 2:
# 
# Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
# Output: 2
# 
# Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 ->
# 3 -> 4. The score of this path is min(2,2,4,7) = 2.
# 
# 
# Constraints:
#         2 <= n <= 10⁵
#         1 <= roads.length <= 10⁵
#         roads[i].length == 3
#         1 <= aᵢ, bᵢ <= n
#         aᵢ != bᵢ
#         1 <= distanceᵢ <= 10⁴
#         There are no repeated edges.
#         There is at least one path between 1 and n.

from collections import defaultdict

# Solution: https://youtu.be/K7-mXA0irhY
# Credit: Navdeep Singh founder of NeetCode
def min_score(n, roads):
    adj = defaultdict(list)
    for src, dst, dist in roads:
        adj[src].append((dst, dist))
        adj[dst].append((src, dist))

    def dfs(i):
        nonlocal res
        if i in visit:
            return

        visit.add(i)

        for nei, dist in adj[i]:
            res = min(res, dist)
            dfs(nei)

    res = float("inf")
    visit = set()
    dfs(1)

    return res
    # Time: O(v + e)    v = number of cities (nodes), e = number of roads (edges)
    # Space: O(v + e)


def main():
    roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
    result = min_score(4, roads)
    print(result) # 5

    roads = [[1,2,2],[1,3,4],[3,4,7]]
    result = min_score(4, roads)
    print(result) # 2

if __name__ == "__main__":
    main()
