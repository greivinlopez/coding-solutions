# -----------------------------
# 1388. Pizza With 3n Slices 🍕
# -----------------------------

# Problem: https://leetcode.com/problems/pizza-with-3n-slices
#
# There is a pizza with 3n slices of varying size, you and your friends will take
# slices of pizza as follows:
#         
#   * You will pick any pizza slice.
#   * Your friend Alice will pick the next slice in the anti-clockwise direction 
#     of your pick.
#   * Your friend Bob will pick the next slice in the clockwise direction of your 
#     pick.
#   * Repeat until there are no more slices of pizzas.
# 
# Given an integer array slices that represent the sizes of the pizza slices in a
# clockwise direction, return the maximum possible sum of slice sizes that you can
# pick.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/02/18/sample_3_1723.png
# 
# Input: slices = [1,2,3,4,5,6]
# Output: 10
# 
# Explanation: Pick pizza slice of size 4, Alice and Bob will pick slices with
# size 3 and 5 respectively. Then Pick slices with size 6, finally Alice and Bob
# will pick slice of size 2 and 1 respectively. Total = 4 + 6.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/02/18/sample_4_1723.png
# 
# Input: slices = [8,9,8,6,1,1]
# Output: 16
# 
# Explanation: Pick pizza slice of size 8 in each turn. If you pick slice with
# size 9 your partners will pick slices of size 8.
# 
# 
# Constraints:
#         3 * n == slices.length
#         1 <= slices.length <= 500
#         1 <= slices[i] <= 1000


# Solution: https://algo.monster/liteproblems/1388
# Credit: AlgoMonster
def max_size_slices(slices):

    def max_sum_non_adjacent(nums):
        array_length = len(nums)
        
        # dp[i][j] represents max sum when considering first i elements 
        # and selecting exactly j elements
        dp = [[0] * (slices_to_pick + 1) for _ in range(array_length + 1)]
        
        # Fill the DP table
        for i in range(1, array_length + 1):
            for j in range(1, slices_to_pick + 1):
                # Option 1: Don't take current element
                dont_take = dp[i - 1][j]
                
                # Option 2: Take current element (if possible)
                # We need at least 2 elements to have a previous non-adjacent element
                take = (dp[i - 2][j - 1] if i >= 2 else 0) + nums[i - 1]
                
                dp[i][j] = max(dont_take, take)
        
        return dp[array_length][slices_to_pick]
    
    # Calculate number of slices we need to pick (n/3 of total)
    slices_to_pick = len(slices) // 3
    
    # Handle circular array by considering two cases:
    # Case 1: Exclude last element (so first and last aren't both selected)
    max_without_last = max_sum_non_adjacent(slices[:-1])
    
    # Case 2: Exclude first element (so first and last aren't both selected)
    max_without_first = max_sum_non_adjacent(slices[1:])
    
    # Return the maximum of both cases
    return max(max_without_last, max_without_first)
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = max_size_slices(slices = [1,2,3,4,5,6])
    print(result) # 10

    result = max_size_slices(slices = [8,9,8,6,1,1])
    print(result) # 16

if __name__ == "__main__":
    main()
