# ----------------------
# 956. Tallest Billboard
# ----------------------

# Problem: https://leetcode.com/problems/tallest-billboard
#
# You are installing a billboard and want it to have the largest height. The
# billboard will have two steel supports, one on each side. Each steel support
# must be an equal height.
# 
# You are given a collection of rods that can be welded together. For example, if
# you have rods of lengths 1, 2, and 3, you can weld them together to make a
# support of length 6.
# 
# Return the largest possible height of your billboard installation. If you cannot
# support the billboard, return 0.
# 
# Example 1:
# 
# Input: rods = [1,2,3,6]
# Output: 6
# 
# Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same
# sum = 6.
# 
# Example 2:
# 
# Input: rods = [1,2,3,4,5,6]
# Output: 10
# 
# Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same
# sum = 10.
# 
# Example 3:
# 
# Input: rods = [1,2]
# Output: 0
# 
# Explanation: The billboard cannot be supported, so we return 0.
# 
# 
# Constraints:
#         1 <= rods.length <= 20
#         1 <= rods[i] <= 1000
#         sum(rods[i]) <= 5000


# Solution: https://algo.monster/liteproblems/956
# Credit: AlgoMonster
def tallest_billboard(rods):
    from functools import cache
    from math import inf
    
    @cache
    def dp(index, height_diff):
        # Base case: no more rods to consider
        if index >= len(rods):
            # Valid only if both supports have equal height
            return 0 if height_diff == 0 else -inf
        
        current_rod = rods[index]
        
        # Option 1: Skip current rod
        result = dp(index + 1, height_diff)
        
        # Option 2: Add current rod to the taller support
        result = max(result, dp(index + 1, height_diff + current_rod))
        
        # Option 3: Add current rod to the shorter support
        # The shorter support gains min(height_diff, current_rod) in effective height
        height_gain = min(height_diff, current_rod)
        new_diff = abs(current_rod - height_diff)
        result = max(result, dp(index + 1, new_diff) + height_gain)
        
        return result
    
    return dp(0, 0)
    # Time: O(n * m)
    # Space: O(n * m)
    # n = the length of the rods array
    # m = the sum of all rod lengths.


def main():
    result = tallest_billboard(rods = [1,2,3,6])
    print(result) # 6

    result = tallest_billboard(rods = [1,2,3,4,5,6])
    print(result) # 10

    result = tallest_billboard(rods = [1,2])
    print(result) # 0

if __name__ == "__main__":
    main()
