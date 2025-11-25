# -------------------------------------------------------
# 1621. Number of Sets of K Non-Overlapping Line Segments
# -------------------------------------------------------

# Problem: https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments
#
# Given n points on a 1-D plane, where the iᵗʰ point (from 0 to n-1) is at x = i,
# find the number of ways we can draw exactly k non-overlapping line segments such
# that each segment covers two or more points. The endpoints of each segment must
# have integral coordinates. The k line segments do not have to cover all n
# points, and they are allowed to share endpoints.
# 
# Return the number of ways we can draw k non-overlapping line segments. Since
# this number can be huge, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/07/ex1.png
# 
# Input: n = 4, k = 2
# Output: 5
# 
# Explanation: The two line segments are shown in red and blue.
# The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)},
# {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.
# 
# Example 2:
# 
# Input: n = 3, k = 1
# Output: 3
# 
# Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.
# 
# Example 3:
# 
# Input: n = 30, k = 7
# Output: 796297179
# 
# Explanation: The total number of possible ways to draw 7 line segments is
# 3796297200. Taking this number modulo 109 + 7 gives us 796297179.
# 
# 
# Constraints:
#         2 <= n <= 1000
#         1 <= k <= n-1


# Solution: https://algo.monster/liteproblems/1621
# Credit: AlgoMonster
def number_of_sets(n, k):
    MOD = 10**9 + 7
    
    # dp_closed[i][j] = number of ways to partition i points into j+1 segments
    # where the last segment is "closed" (doesn't extend to point i)
    dp_closed = [[0] * (k + 1) for _ in range(n + 1)]
    
    # dp_open[i][j] = number of ways to partition i points into j+1 segments  
    # where the last segment is "open" (extends to point i)
    dp_open = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: 1 point with 0 segments (1 way - the point itself)
    dp_closed[1][0] = 1
    
    # Fill the DP table for each number of points
    for num_points in range(2, n + 1):
        for num_segments in range(k + 1):
            # A closed segment at position i can come from:
            # 1. A closed segment at i-1 (we don't extend it)
            # 2. An open segment at i-1 (we close it here)
            dp_closed[num_points][num_segments] = (
                dp_closed[num_points - 1][num_segments] + 
                dp_open[num_points - 1][num_segments]
            ) % MOD
            
            # An open segment at position i extends from i-1
            dp_open[num_points][num_segments] = dp_open[num_points - 1][num_segments]
            
            if num_segments > 0:
                # We can also start a new open segment at position i
                # This requires one less segment to be already formed at i-1
                dp_open[num_points][num_segments] = (
                    dp_open[num_points][num_segments] +
                    dp_closed[num_points - 1][num_segments - 1] +
                    dp_open[num_points - 1][num_segments - 1]
                ) % MOD
    
    # Return the total number of ways (both closed and open final segments)
    return (dp_closed[n][k] + dp_open[n][k]) % MOD
    # Time: O(n * k)
    # Space: O(n * k)


def main():
    result = number_of_sets(n = 4, k = 2)
    print(result) # 5

    result = number_of_sets(n = 3, k = 1)
    print(result) # 3

    result = number_of_sets(n = 30, k = 7)
    print(result) # 796297179

if __name__ == "__main__":
    main()
