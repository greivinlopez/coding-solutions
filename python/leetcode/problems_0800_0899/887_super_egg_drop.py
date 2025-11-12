# ----------------------
# 887. Super Egg Drop 🥚
# ----------------------

# Problem: https://leetcode.com/problems/super-egg-drop
#
# You are given k identical eggs and you have access to a building with n floors
# labeled from 1 to n.
# 
# You know that there exists a floor f where 0 <= f <= n such that any egg dropped
# at a floor higher than f will break, and any egg dropped at or below floor f
# will not break.
# 
# Each move, you may take an unbroken egg and drop it from any floor x (where 1 <=
# x <= n). If the egg breaks, you can no longer use it. However, if the egg does
# not break, you may reuse it in future moves.
# 
# Return the minimum number of moves that you need to determine with certainty
# what the value of f is.
# 
# Example 1:
# 
# Input: k = 1, n = 2
# Output: 2
# 
# Explanation:
# Drop the egg from floor 1. If it breaks, we know that f = 0.
# Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
# If it does not break, then we know f = 2.
# Hence, we need at minimum 2 moves to determine with certainty what the value of
# f is.
# 
# Example 2:
# 
# Input: k = 2, n = 6
# Output: 3
# 
# Example 3:
# 
# Input: k = 3, n = 14
# Output: 4
# 
# 
# Constraints:
#         1 <= k <= 100
#         1 <= n <= 10⁴


# Solution: https://algo.monster/liteproblems/887
# Credit: AlgoMonster
def super_egg_drop(k, n):
    from functools import cache
    
    @cache
    def dp(floors, eggs):
        # Base case: No floors to check
        if floors < 1:
            return 0
        
        # Base case: Only 1 egg left, must check linearly from bottom
        if eggs == 1:
            return floors
        
        # Binary search to find optimal floor to drop egg from
        # We're looking for the floor that minimizes the worst case
        left, right = 1, floors
        
        while left < right:
            # Calculate middle point (ceiling division)
            mid = (left + right + 1) >> 1
            
            # Case 1: Egg breaks at floor mid
            # Check floors below with one less egg
            egg_breaks = dp(mid - 1, eggs - 1)
            
            # Case 2: Egg doesn't break at floor mid  
            # Check floors above with same number of eggs
            egg_survives = dp(floors - mid, eggs)
            
            # Binary search to find the floor where the two cases balance
            # This minimizes the maximum of the two cases
            if egg_breaks <= egg_survives:
                left = mid
            else:
                right = mid - 1
        
        # Return worst case scenario (max of two cases) plus current move
        return max(dp(left - 1, eggs - 1), dp(floors - left, eggs)) + 1
    
    # Start with n floors and k eggs
    return dp(n, k)
    # Time: O(k * n * log(n))
    # Space: O(k * n)


def main():
    result = super_egg_drop(k = 1, n = 2)
    print(result) # 2

    result = super_egg_drop(k = 2, n = 6)
    print(result) # 3

    result = super_egg_drop(k = 3, n = 14)
    print(result) # 4

if __name__ == "__main__":
    main()
