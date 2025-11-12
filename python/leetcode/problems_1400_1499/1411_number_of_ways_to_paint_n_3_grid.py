# -------------------------------------------
# 1411. Number of Ways to Paint N × 3 Grid 🫟
# -------------------------------------------

# Problem: https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid
#
# You have a grid of size n x 3 and you want to paint each cell of the grid with
# exactly one of the three colors: Red, Yellow, or Green while making sure that no
# two adjacent cells have the same color (i.e., no two cells that share vertical
# or horizontal sides have the same color).
# 
# Given n the number of rows of the grid, return the number of ways you can paint
# this grid. As the answer may grow large, the answer must be computed modulo 
# 10⁹ + 7.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/03/26/e1.png
# 
# Input: n = 1
# Output: 12
# 
# Explanation: There are 12 possible way to paint the grid as shown.
# 
# Example 2:
# 
# Input: n = 5000
# Output: 30228214
# 
# 
# Constraints:
#         n == grid.length
#         1 <= n <= 5000


# Solution: https://algo.monster/liteproblems/1411
# Credit: AlgoMonster
def num_of_ways(n):
    MOD = 10**9 + 7
    
    # Initialize counters for the first column
    # aba_pattern_count: Number of ways to paint a column with ABA pattern (same first and last color)
    # abc_pattern_count: Number of ways to paint a column with ABC pattern (all different colors)
    # Both start with 6 ways each (3 colors × 2 permutations each)
    aba_pattern_count = 6  # Patterns like: RGR, GRG, BRB, RBR, GBG, BGB
    abc_pattern_count = 6  # Patterns like: RGB, RBG, GRB, GBR, BRG, BGR
    
    # Build up the solution column by column
    for column_index in range(n - 1):
        # Calculate valid patterns for the next column based on current column
        # From ABA pattern: can transition to 3 ABA patterns + 2 ABC patterns
        # From ABC pattern: can transition to 2 ABA patterns + 2 ABC patterns
        next_aba_count = (3 * aba_pattern_count + 2 * abc_pattern_count) % MOD
        next_abc_count = (2 * aba_pattern_count + 2 * abc_pattern_count) % MOD
        
        # Update pattern counts for the next iteration
        aba_pattern_count = next_aba_count
        abc_pattern_count = next_abc_count
    
    # Return the total number of valid ways
    return (aba_pattern_count + abc_pattern_count) % MOD
    # Time: O(n)
    # Space: O(1)


def main():
    result = num_of_ways(n = 1)
    print(result) # 12

    result = num_of_ways(n = 5000)
    print(result) # 30228214

if __name__ == "__main__":
    main()
