# --------------------------------------------
# 1039. Minimum Score Triangulation of Polygon
# --------------------------------------------

# Problem: https://leetcode.com/problems/minimum-score-triangulation-of-polygon
#
# You have a convex n-sided polygon where each vertex has an integer value. You
# are given an integer array values where values[i] is the value of the ith vertex
# in clockwise order.
# 
# Polygon triangulation is a process where you divide a polygon into a set of
# triangles and the vertices of each triangle must also be vertices of the
# original polygon. Note that no other shapes other than triangles are allowed in
# the division. This process will result in n - 2 triangles.
# 
# You will triangulate the polygon. For each triangle, the weight of that triangle
# is the product of the values at its vertices. The total score of the
# triangulation is the sum of these weights over all n - 2 triangles.
# 
# Return the minimum possible score that you can achieve with some triangulation
# of the polygon.
# 
# Example 1:
# 
# Input: values = [1,2,3]
# Output: 6
# 
# Explanation: The polygon is already triangulated, and the score of the only
# triangle is 6.
# 
# Example 2:
# 
# Input: values = [3,7,4,5]
# Output: 144
# 
# Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 =
# 245, or 3*4*5 + 3*4*7 = 144.
# The minimum score is 144.
# 
# Example 3:
# 
# Input: values = [1,3,1,4,1,5]
# Output: 13
# 
# Explanation: The minimum score triangulation is 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 =
# 13.
# 
# 
# Constraints:
#         n == values.length
#         3 <= n <= 50
#         1 <= values[i] <= 100


# Solution: https://algo.monster/liteproblems/1039
# Credit: AlgoMonster
def min_score_triangulation(values):
    from functools import cache
    
    @cache
    def dfs(left, right):
        # Base case: adjacent vertices form an edge, not a triangle
        if left + 1 == right:
            return 0
        
        # Try all possible vertices k to form a triangle with vertices left and right
        # The triangle (left, k, right) divides the polygon into:
        # 1. Sub-polygon from left to k
        # 2. The triangle itself with score: values[left] * values[k] * values[right]
        # 3. Sub-polygon from k to right
        min_score = float('inf')
        for k in range(left + 1, right):
            current_score = (dfs(left, k) + 
                            dfs(k, right) + 
                            values[left] * values[k] * values[right])
            min_score = min(min_score, current_score)
        
        return min_score
    
    # Start with the entire polygon from vertex 0 to vertex n-1
    return dfs(0, len(values) - 1)
    # Time: O(n³)
    # Space: O(n²)


def main():
    result = min_score_triangulation(values = [1,2,3])
    print(result) # 6

    result = min_score_triangulation(values = [3,7,4,5])
    print(result) # 144

    result = min_score_triangulation(values = [1,3,1,4,1,5])
    print(result) # 13

if __name__ == "__main__":
    main()
