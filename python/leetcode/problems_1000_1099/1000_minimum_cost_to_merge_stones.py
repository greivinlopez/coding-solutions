# ---------------------------------
# 1000. Minimum Cost to Merge Stones
# ---------------------------------

# Problem: https://leetcode.com/problems/minimum-cost-to-merge-stones
#
# There are n piles of stones arranged in a row. The iᵗʰ pile has stones[i]
# stones.
# 
# A move consists of merging exactly k consecutive piles into one pile, and the
# cost of this move is equal to the total number of stones in these k piles.
# 
# Return the minimum cost to merge all piles of stones into one pile. If it is
# impossible, return -1.
# 
# Example 1:
# 
# Input: stones = [3,2,4,1], k = 2
# Output: 20
# 
# Explanation: We start with [3, 2, 4, 1].
# We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
# We merge [4, 1] for a cost of 5, and we are left with [5, 5].
# We merge [5, 5] for a cost of 10, and we are left with [10].
# The total cost was 20, and this is the minimum possible.
# 
# Example 2:
# 
# Input: stones = [3,2,4,1], k = 3
# Output: -1
# 
# Explanation: After any merge operation, there are 2 piles left, and we can't
# merge anymore.  So the task is impossible.
# 
# Example 3:
# 
# Input: stones = [3,5,1,2,6], k = 3
# Output: 25
# 
# Explanation: We start with [3, 5, 1, 2, 6].
# We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
# We merge [3, 8, 6] for a cost of 17, and we are left with [17].
# The total cost was 25, and this is the minimum possible.
# 
# 
# Constraints:
#         n == stones.length
#         1 <= n <= 30
#         1 <= stones[i] <= 100
#         2 <= k <= 30


# Solution: https://algo.monster/liteproblems/1000
# Credit: AlgoMonster
def merge_stones(stones, k):
    n = len(stones)
    
    # Check if it's possible to merge all stones into one pile
    # We need exactly (n-1)/(K-1) merge operations
    if (n - 1) % (k - 1) != 0:
        return -1
    
    # Build prefix sum array for quick range sum calculation
    # prefix_sum[i] = sum of stones[0] to stones[i-1]
    prefix_sum = [0]
    for stone in stones:
        prefix_sum.append(prefix_sum[-1] + stone)
    
    # dp[i][j][m] = minimum cost to merge stones[i-1] to stones[j-1] into m piles
    # Initialize with infinity (impossible states)
    dp = [[[float('inf')] * (k + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    
    # Base case: single stone forms 1 pile with cost 0
    for i in range(1, n + 1):
        dp[i][i][1] = 0
    
    # Iterate over all possible subarray lengths
    for length in range(2, n + 1):
        # Iterate over all possible starting positions
        for start in range(1, n - length + 2):
            end = start + length - 1
            
            # Try to form different number of piles
            for num_piles in range(2, k + 1):
                # Try different split points
                for split in range(start, end, k - 1):
                    # Merge left part into 1 pile and right part into (num_piles - 1) piles
                    dp[start][end][num_piles] = min(
                        dp[start][end][num_piles],
                        dp[start][split][1] + dp[split + 1][end][num_piles - 1]
                    )
            
            # Merge K piles into 1 pile
            # The cost is the sum of all stones in the range
            dp[start][end][1] = dp[start][end][k] + prefix_sum[end] - prefix_sum[start - 1]
    
    # Return minimum cost to merge all stones into 1 pile
    return dp[1][n][1]
    # Time: O(n³ * k)
    # Space: O(n² * K)


def main():
    result = merge_stones(stones = [3,2,4,1], k = 2)
    print(result) # 20

    result = merge_stones(stones = [3,2,4,1], k = 3)
    print(result) # -1

    result = merge_stones(stones = [3,5,1,2,6], k = 3)
    print(result) # 25

if __name__ == "__main__":
    main()
