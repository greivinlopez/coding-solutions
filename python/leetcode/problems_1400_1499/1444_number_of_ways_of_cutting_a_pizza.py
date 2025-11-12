# ------------------------------------------
# 1444. Number of Ways of Cutting a Pizza 🍕
# ------------------------------------------

# Problem: https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza
#
# Given a rectangular pizza represented as a rows x cols matrix containing the
# following characters: 'A' (an apple) and '.' (empty cell) and given the integer
# k. You have to cut the pizza into k pieces using k-1 cuts. 
# 
# For each cut you choose the direction: vertical or horizontal, then you choose a
# cut position at the cell boundary and cut the pizza into two pieces. If you cut
# the pizza vertically, give the left part of the pizza to a person. If you cut
# the pizza horizontally, give the upper part of the pizza to a person. Give the
# last piece of pizza to the last person.
# 
# Return the number of ways of cutting the pizza such that each piece contains at
# least one apple. Since the answer can be a huge number, return this modulo 
# 10^9 + 7.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/04/23/ways_to_cut_apple_1.png
# 
# Input: pizza = ["A..","AAA","..."], k = 3
# Output: 3
# 
# Explanation: The figure above shows the three ways to cut the pizza. Note that
# pieces must contain at least one apple.
# 
# Example 2:
# 
# Input: pizza = ["A..","AA.","..."], k = 3
# Output: 1
# 
# Example 3:
# 
# Input: pizza = ["A..","A..","..."], k = 1
# Output: 1
# 
# 
# Constraints:
#         1 <= rows, cols <= 50
#         rows == pizza.length
#         cols == pizza[i].length
#         1 <= k <= 10
#         pizza consists of characters 'A' and '.' only.


# Solution: https://algo.monster/liteproblems/1444
# Credit: AlgoMonster
def ways(pizza, k):
    from functools import cache

    MOD = 10**9 + 7
    rows, cols = len(pizza), len(pizza[0])
    
    # Build 2D prefix sum array to quickly calculate apples in any rectangle
    # prefix_sum[i][j] represents total apples in rectangle from (0,0) to (i-1,j-1)
    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            # Add current cell value (1 if apple, 0 otherwise)
            # Use inclusion-exclusion principle for 2D prefix sum
            prefix_sum[row][col] = (prefix_sum[row - 1][col] + 
                                    prefix_sum[row][col - 1] - 
                                    prefix_sum[row - 1][col - 1] + 
                                    int(pizza[row - 1][col - 1] == 'A'))
    
    @cache
    def count_ways(top_row: int, left_col: int, cuts_remaining: int) -> int:
        # Base case: no more cuts needed
        if cuts_remaining == 0:
            # Check if remaining piece has at least one apple
            # Calculate apples in rectangle from (top_row, left_col) to (rows-1, cols-1)
            apples_in_piece = (prefix_sum[rows][cols] - 
                                prefix_sum[top_row][cols] - 
                                prefix_sum[rows][left_col] + 
                                prefix_sum[top_row][left_col])
            return 1 if apples_in_piece > 0 else 0
        
        total_ways = 0
        
        # Try horizontal cuts - give away top portion
        for cut_row in range(top_row + 1, rows):
            # Check if top piece (from top_row to cut_row-1) has at least one apple
            apples_in_top = (prefix_sum[cut_row][cols] - 
                                prefix_sum[top_row][cols] - 
                                prefix_sum[cut_row][left_col] + 
                                prefix_sum[top_row][left_col])
            if apples_in_top > 0:
                # Recursively process remaining bottom piece
                total_ways += count_ways(cut_row, left_col, cuts_remaining - 1)
        
        # Try vertical cuts - give away left portion
        for cut_col in range(left_col + 1, cols):
            # Check if left piece (from left_col to cut_col-1) has at least one apple
            apples_in_left = (prefix_sum[rows][cut_col] - 
                                prefix_sum[top_row][cut_col] - 
                                prefix_sum[rows][left_col] + 
                                prefix_sum[top_row][left_col])
            if apples_in_left > 0:
                # Recursively process remaining right piece
                total_ways += count_ways(top_row, cut_col, cuts_remaining - 1)
        
        return total_ways % MOD
    
    # Start with full pizza (0,0) and need to make k-1 cuts to get k pieces
    return count_ways(0, 0, k - 1)
    # Time: O(k * m * n * (m + n))
    # Space: O(m * n * k + m * n)


def main():
    result = ways(pizza = ["A..","AAA","..."], k = 3)
    print(result) # 3

    result = ways(pizza = ["A..","AA.","..."], k = 3)
    print(result) # 1

    result = ways(pizza = ["A..","A..","..."], k = 1)
    print(result) # 1

if __name__ == "__main__":
    main()
