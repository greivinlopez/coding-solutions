# -------------------------------
# 782. Transform to Chessboard ♟️
# -------------------------------

# Problem: https://leetcode.com/problems/transform-to-chessboard
#
# You are given an n x n binary grid board. In each move, you can swap any two
# rows with each other, or any two columns with each other.
# 
# Return the minimum number of moves to transform the board into a chessboard
# board. If the task is impossible, return -1.
# 
# A chessboard board is a board where no 0's and no 1's are 4-directionally
# adjacent.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/06/29/chessboard1-grid.jpg
# 
# Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
# Output: 2
# 
# Explanation: One potential sequence of moves is shown.
# The first move swaps the first and second column.
# The second move swaps the second and third row.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/06/29/chessboard2-grid.jpg
# 
# Input: board = [[0,1],[1,0]]
# Output: 0
# 
# Explanation: Also note that the board with 0 in the top left corner, is also a
# valid chessboard.
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2021/06/29/chessboard3-grid.jpg
# 
# Input: board = [[1,0],[1,0]]
# Output: -1
# 
# Explanation: No matter what sequence of moves you make, you cannot end with a
# valid chessboard.
# 
# 
# Constraints:
#         n == board.length
#         n == board[i].length
#         2 <= n <= 30
#         board[i][j] is either 0 or 1.


# Solution: https://algo.monster/liteproblems/782
# Credit: AlgoMonster
def moves_to_chessboard(board):
    def calculate_min_swaps(pattern_mask, same_count):
        # Python 3.10+:
        # ones_count = pattern_mask.bit_count()
        ones_count = bin(pattern_mask).count('1')

        if n & 1:  # Odd board size
            # For odd n, difference between 0s and 1s must be exactly 1
            if abs(n - 2 * ones_count) != 1 or abs(n - 2 * same_count) != 1:
                return -1
            
            # Check which pattern to use based on ones count
            if ones_count == n // 2:
                # Pattern starts with 0 (0xAAAA... represents 1010...)
                # return n // 2 - (pattern_mask & 0xAAAAAAAA).bit_count()
                return n // 2 - bin(pattern_mask & 0xAAAAAAAA).count('1')
            else:
                # Pattern starts with 1 (0x5555... represents 0101...)
                # return (n + 1) // 2 - (pattern_mask & 0x55555555).bit_count()
                return (n + 1) // 2 - bin(pattern_mask & 0x55555555).count('1')
        else:  # Even board size
            # For even n, must have equal 0s and 1s
            if ones_count != n // 2 or same_count != n // 2:
                return -1
            
            # Try both patterns and choose minimum
            # swaps_pattern_0 = n // 2 - (pattern_mask & 0xAAAAAAAA).bit_count()
            # swaps_pattern_1 = n // 2 - (pattern_mask & 0x55555555).bit_count()
            swaps_pattern_0 = n // 2 - bin(pattern_mask & 0xAAAAAAAA).count('1')
            swaps_pattern_1 = n // 2 - bin(pattern_mask & 0x55555555).count('1')
            return min(swaps_pattern_0, swaps_pattern_1)
    
    n = len(board)
    all_bits_mask = (1 << n) - 1  # Mask with all n bits set to 1
    
    # Create bit masks for first row and first column
    first_row_mask = 0
    first_col_mask = 0
    for i in range(n):
        first_row_mask |= board[0][i] << i
        first_col_mask |= board[i][0] << i
    
    # Create inverted masks (complement patterns)
    inverted_row_mask = all_bits_mask ^ first_row_mask
    inverted_col_mask = all_bits_mask ^ first_col_mask
    
    # Count rows/columns matching the first row/column pattern
    rows_matching_first = 0
    cols_matching_first = 0
    
    # Validate board and count matching patterns
    for i in range(n):
        current_row_mask = 0
        current_col_mask = 0
        
        # Build bit masks for current row and column
        for j in range(n):
            current_row_mask |= board[i][j] << j
            current_col_mask |= board[j][i] << j
        
        # Each row/column must match either the first pattern or its inverse
        if (current_row_mask not in (first_row_mask, inverted_row_mask) or 
            current_col_mask not in (first_col_mask, inverted_col_mask)):
            return -1
        
        # Count matches with first pattern
        rows_matching_first += (current_row_mask == first_row_mask)
        cols_matching_first += (current_col_mask == first_col_mask)
    
    # Calculate minimum swaps for rows and columns
    row_swaps = calculate_min_swaps(first_row_mask, rows_matching_first)
    col_swaps = calculate_min_swaps(first_col_mask, cols_matching_first)
    
    # Return total swaps or -1 if impossible
    if row_swaps == -1 or col_swaps == -1:
        return -1
    return row_swaps + col_swaps
    # Time: O(n²)
    # Space: O(1)


def main():
    result = moves_to_chessboard(board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]])
    print(result) # 2

    result = moves_to_chessboard(board = [[0,1],[1,0]])
    print(result) # 0

    result = moves_to_chessboard(board = [[1,0],[1,0]])
    print(result) # -1

if __name__ == "__main__":
    main()
