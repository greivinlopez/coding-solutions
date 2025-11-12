# ---------------------------
# 1478. Allocate Mailboxes 📬
# ---------------------------

# Problem: https://leetcode.com/problems/allocate-mailboxes
#
# Given the array houses where houses[i] is the location of the ith house along a
# street and an integer k, allocate k mailboxes in the street.
# 
# Return the minimum total distance between each house and its nearest mailbox.
# 
# The test cases are generated so that the answer fits in a 32-bit integer.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/05/07/sample_11_1816.png
# 
# Input: houses = [1,4,8,10,20], k = 3
# Output: 5
# 
# Explanation: Allocate mailboxes in position 3, 9 and 20.
# Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| +
# |9-8| + |10-9| + |20-20| = 5
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/05/07/sample_2_1816.png
# 
# Input: houses = [2,3,5,12,18], k = 2
# Output: 9
# 
# Explanation: Allocate mailboxes in position 3 and 14.
# Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| +
# |5-3| + |12-14| + |18-14| = 9.
# 
# 
# Constraints:
#         1 <= k <= houses.length <= 100
#         1 <= houses[i] <= 10⁴
#         All the integers of houses are unique.


# Solution: https://algo.monster/liteproblems/1478
# Credit: AlgoMonster
def min_distance(houses, k):
    # Sort houses by position for optimal mailbox placement
    houses.sort()
    n = len(houses)
    
    # cost[i][j] = minimum cost to place one mailbox for houses[i] to houses[j]
    # The optimal position for one mailbox is the median of the houses
    cost = [[0] * n for _ in range(n)]
    
    # Build cost matrix from right-bottom to left-top
    # For sorted houses, placing mailbox at median minimizes total distance
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            # Recurrence: extend the range by adding houses at both ends
            # The new cost adds the distance between the new pair of houses
            cost[i][j] = cost[i + 1][j - 1] + houses[j] - houses[i]
    
    # dp[i][j] = minimum distance for houses[0..i] using j mailboxes
    dp = [[float('inf')] * (k + 1) for _ in range(n)]
    
    # Process each house position
    for i in range(n):
        # Base case: one mailbox for houses[0..i]
        dp[i][1] = cost[0][i]
        
        # Try using 2 to min(k, i+1) mailboxes
        # Can't use more mailboxes than houses up to position i
        for j in range(2, min(k + 1, i + 2)):
            # Try all possible positions for the (j-1)th mailbox
            for p in range(i):
                # Split: houses[0..p] use j-1 mailboxes
                #         houses[p+1..i] use 1 mailbox
                dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p + 1][i])
    
    # Return minimum distance for all houses using k mailboxes
    return dp[-1][k]
    # Time: O(n² * k)
    # Space: O(n²)


def main():
    result = min_distance(houses = [1,4,8,10,20], k = 3)
    print(result) # 5

    result = min_distance(houses = [2,3,5,12,18], k = 2)
    print(result) # 9

if __name__ == "__main__":
    main()
