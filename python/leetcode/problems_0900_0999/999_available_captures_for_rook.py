# --------------------------------
# 999. Available Captures for Rook
# --------------------------------

# Problem: https://leetcode.com/problems/available-captures-for-rook
#
# You are given an 8 x 8 matrix representing a chessboard. There is exactly one
# white rook represented by 'R', some number of white bishops 'B', and some number
# of black pawns 'p'. Empty squares are represented by '.'.
# 
# A rook can move any number of squares horizontally or vertically (up, down,
# left, right) until it reaches another piece or the edge of the board. 
# A rook is attacking a pawn if it can move to the pawn's square in one move.
# 
# Note: A rook cannot move through other pieces, such as bishops or pawns. This
# means a rook cannot attack a pawn if there is another piece blocking the path.
# 
# Return the number of pawns the white rook is attacking.
# 
# Example 1:
# 
# Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","
# ."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".","."
# ,".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".","."
# ,".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# 
# Explanation:
# In this example, the rook is attacking all the pawns.
# 
# Example 2:
# Input: board = [[".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],
# [".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p"
# ,"B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".","."
# ,".","."],[".",".",".",".",".",".",".","."]]
# Output: 0
# 
# Explanation:
# The bishops are blocking the rook from attacking any of the pawns.
# 
# Example 3:
# 
# Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","
# ."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".","."
# ,".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p","."
# ,".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# 
# Explanation:
# The rook is attacking the pawns at positions b5, d6, and f5.
# 
# 
# Constraints:
#         board.length == 8
#         board[i].length == 8
#         board[i][j] is either 'R', '.', 'B', or 'p'
#         There is exactly one cell with board[i][j] == 'R'


# Solution: https://algo.monster/liteproblems/999
# Credit: AlgoMonster
def num_rook_captures(board):
    # Define four directions: up, right, down, left
    # Using pairwise iteration: (-1,0), (0,1), (1,0), (0,-1)
    directions = (-1, 0, 1, 0, -1)
    board_size = len(board)
    
    # Find the rook's position on the board
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == "R":
                captured_pawns = 0
                
                # Check all four directions from the rook
                for i in range(4):
                    # Get direction vector using pairwise
                    dx = directions[i]
                    dy = directions[i + 1]
                    
                    # Start from the rook's adjacent cell in current direction
                    current_row = row + dx
                    current_col = col + dy
                    
                    # Continue moving in the same direction until hitting a boundary or bishop
                    while 0 <= current_row < board_size and 0 <= current_col < board_size and board[current_row][current_col] != "B":
                        # If we find a pawn, capture it and stop in this direction
                        if board[current_row][current_col] == "p":
                            captured_pawns += 1
                            break
                        
                        # Move to the next cell in the same direction
                        current_row += dx
                        current_col += dy
                
                return captured_pawns
    # Time: O(m * n)
    # Space: O(1)


def main():
    board = [[".",".",".",".",".",".",".","."],
             [".",".",".","p",".",".",".","."],
             [".",".",".","R",".",".",".","p"],
             [".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".","."],
             [".",".",".","p",".",".",".","."],
             [".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".","."]]
    result = num_rook_captures(board)
    print(result) # 3

    board = [[".",".",".",".",".",".",".","."],
             [".","p","p","p","p","p",".","."],
             [".","p","p","B","p","p",".","."],
             [".","p","B","R","B","p",".","."],
             [".","p","p","B","p","p",".","."],
             [".","p","p","p","p","p",".","."],
             [".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".","."]]
    result = num_rook_captures(board)
    print(result) # 0

    board = [[".",".",".",".",".",".",".","."],
             [".",".",".","p",".",".",".","."],
             [".",".",".","p",".",".",".","."],
             ["p","p",".","R",".","p","B","."],
             [".",".",".",".",".",".",".","."],
             [".",".",".","B",".",".",".","."],
             [".",".",".","p",".",".",".","."],
             [".",".",".",".",".",".",".","."]]
    result = num_rook_captures(board)
    print(result) # 3

if __name__ == "__main__":
    main()
