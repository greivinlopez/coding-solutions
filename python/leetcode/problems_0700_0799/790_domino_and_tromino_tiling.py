# ------------------------------
# 790. Domino and Tromino Tiling
# ------------------------------

# Problem: https://leetcode.com/problems/domino-and-tromino-tiling
#
# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may
# rotate these shapes.
# 
# https://assets.leetcode.com/uploads/2021/07/15/lc-domino.jpg
# 
# Given an integer n, return the number of ways to tile an 2 x n board. Since the
# answer may be very large, return it modulo 10⁹ + 7.
# 
# In a tiling, every square must be covered by a tile. Two tilings are different
# if and only if there are two 4-directionally adjacent cells on the board such
# that exactly one of the tilings has both squares occupied by a tile.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/07/15/lc-domino1.jpg
# 
# Input: n = 3
# Output: 5
# 
# Explanation: The five different ways are shown above.
# 
# Example 2:
# 
# Input: n = 1
# Output: 1
# 
# 
# Constraints:
#         1 <= n <= 1000

from functools import lru_cache

# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def num_tilings(n):
    # A helper function with memoization to count the number of ways to tile the board.
    # i represents the tiles placed in the first row, and j represents the tiles in the second row.
    @lru_cache(None)  # Use lru_cache for memoization to improve performance
    def count_ways(first_row: int, second_row: int) -> int:
        # Base case: If we exceed the board size, there's no way to tile.
        if first_row > n or second_row > n:
            return 0
        # Base case: If both rows are completely tiled, we've found one valid tiling.
        if first_row == n and second_row == n:
            return 1
        
        # Initialization of possible ways to tile.
        ways = 0 
        # When both rows have the same number of points covered by tiles.
        if first_row == second_row:
            ways = (
                count_ways(first_row + 2, second_row + 2) +  # Place a 2x2 square.
                count_ways(first_row + 1, second_row + 1) +  # Place two 2x1 tiles, one in each row.
                count_ways(first_row + 2, second_row + 1) +  # Place a 'L' shaped tromino.
                count_ways(first_row + 1, second_row + 2)    # Place an inverted 'L' shaped tromino.
            )
        elif first_row > second_row:
            # If the first row has more tiles than the second row.
            ways = count_ways(first_row, second_row + 2) + count_ways(first_row + 1, second_row + 2)
        else:
            # If the second row has more tiles than the first row.
            ways = count_ways(first_row + 2, second_row) + count_ways(first_row + 2, second_row + 1)

        # Return the ways modulo MOD, which represents the maximum number of unique tilings.
        return ways % MOD

    # Define the modulo constant to prevent large number arithmetic issues.
    MOD = 10**9 + 7
    # Call the helper function with the initial states of the board (0 tiles placed).
    return count_ways(0, 0)
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = num_tilings(3)
    print(result) # 5

    result = num_tilings(1)
    print(result) # 1

if __name__ == "__main__":
    main()
