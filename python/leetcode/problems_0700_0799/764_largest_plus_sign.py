# ----------------------
# 764. Largest Plus Sign
# ----------------------

# Problem: https://leetcode.com/problems/largest-plus-sign
#
# You are given an integer n. You have an n x n binary grid grid with all values
# initially 1's except for some indices given in the array mines. The iᵗʰ element
# of the array mines is defined as mines[i] = [xᵢ, yᵢ] where grid[xᵢ][yᵢ] == 0.
# 
# Return the order of the largest axis-aligned plus sign of 1's contained in grid.
# If there is none, return 0.
# 
# An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1
# along with four arms of length k - 1 going up, down, left, and right, and made
# of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign,
# only the relevant area of the plus sign is checked for 1's.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/06/13/plus1-grid.jpg
# 
# Input: n = 5, mines = [[4,2]]
# Output: 2
# 
# Explanation: In the above grid, the largest plus sign can only be of order 2.
# One of them is shown.
# 
# Example 2:
# 
# Input: n = 1, mines = [[0,0]]
# Output: 0
# 
# Explanation: There is no plus sign, so return 0.
# 
# 
# Constraints:
#         1 <= n <= 500
#         1 <= mines.length <= 5000
#         0 <= xᵢ, yᵢ < n
#         All the pairs (xᵢ, yᵢ) are unique.


# Solution: https://algo.monster/liteproblems/764
# Credit: AlgoMonster
def order_of_largest_plus_sign(n, mines):
    # Initialize a 2D array where each cell stores the maximum possible arm length
    # of a plus sign centered at that position
    max_arm_length = [[n] * n for _ in range(n)]
    
    # Mark cells with mines as 0 (no plus sign possible there)
    for mine_row, mine_col in mines:
        max_arm_length[mine_row][mine_col] = 0
    
    # For each row and column, calculate the consecutive 1s in all four directions
    for i in range(n):
        # Variables to track consecutive 1s in each direction
        consecutive_left = 0
        consecutive_right = 0
        consecutive_up = 0
        consecutive_down = 0
        
        # Process all four directions simultaneously
        for j, k in zip(range(n), reversed(range(n))):
            # Left direction: process row i from left to right
            consecutive_left = consecutive_left + 1 if max_arm_length[i][j] != 0 else 0
            
            # Right direction: process row i from right to left
            consecutive_right = consecutive_right + 1 if max_arm_length[i][k] != 0 else 0
            
            # Up direction: process column i from top to bottom
            consecutive_up = consecutive_up + 1 if max_arm_length[j][i] != 0 else 0
            
            # Down direction: process column i from bottom to top
            consecutive_down = consecutive_down + 1 if max_arm_length[k][i] != 0 else 0
            
            # Update each cell with the minimum arm length from its current value
            # and the newly calculated consecutive count in that direction
            max_arm_length[i][j] = min(max_arm_length[i][j], consecutive_left)
            max_arm_length[i][k] = min(max_arm_length[i][k], consecutive_right)
            max_arm_length[j][i] = min(max_arm_length[j][i], consecutive_up)
            max_arm_length[k][i] = min(max_arm_length[k][i], consecutive_down)
    
    # Return the maximum arm length found in the entire grid
    # This represents the order of the largest plus sign
    return max(max(row) for row in max_arm_length)
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = order_of_largest_plus_sign(n = 5, mines = [[4,2]])
    print(result) # 2

    result = order_of_largest_plus_sign(n = 1, mines = [[0,0]])
    print(result) # 0

if __name__ == "__main__":
    main()
