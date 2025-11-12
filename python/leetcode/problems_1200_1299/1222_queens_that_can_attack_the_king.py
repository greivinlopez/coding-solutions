# -------------------------------------
# 1222. Queens That Can Attack the King
# -------------------------------------

# Problem: https://leetcode.com/problems/queens-that-can-attack-the-king
#
# On a 0-indexed 8 x 8 chessboard, there can be multiple black queens and one
# white king.
# 
# You are given a 2D integer array queens where queens[i] = [xQueenᵢ, yQueenᵢ]
# represents the position of the iᵗʰ black queen on the chessboard. You are also
# given an integer array king of length 2 where king = [xKing, yKing] represents
# the position of the white king.
# 
# Return the coordinates of the black queens that can directly attack the king.
# You may return the answer in any order.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2022/12/21/chess1.jpg
# 
# Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
# Output: [[0,1],[1,0],[3,3]]
# 
# Explanation: The diagram above shows the three queens that can directly attack
# the king and the three queens that cannot attack the king (i.e., marked with red
# dashes).
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2022/12/21/chess2.jpg
# 
# nput: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
# Output: [[2,2],[3,4],[4,4]]
# 
# Explanation: The diagram above shows the three queens that can directly attack
# the king and the three queens that cannot attack the king (i.e., marked with red
# dashes).
# 
# 
# Constraints:
#         1 <= queens.length < 64
#         queens[i].length == king.length == 2
#         0 <= xQueenᵢ, yQueenᵢ, xKing, yKing < 8
#         All the given positions are unique.


# Solution: https://algo.monster/liteproblems/1222
# Credit: AlgoMonster
def queens_attack_the_king(queens, king):
    # Board size for standard chess board
    BOARD_SIZE = 8
    
    # Convert queens list to a set of tuples for O(1) lookup
    queen_positions = {(row, col) for row, col in queens}
    
    # Result list to store queens that can attack the king
    attacking_queens = []
    
    # Check all 8 directions: horizontal, vertical, and diagonal
    for row_direction in range(-1, 2):
        for col_direction in range(-1, 2):
            # Skip the case where both directions are 0 (no movement)
            if row_direction == 0 and col_direction == 0:
                continue
            
            # Start from king's position
            current_row, current_col = king
            
            # Move in the current direction until we hit a boundary or find a queen
            while (0 <= current_row + row_direction < BOARD_SIZE and 
                    0 <= current_col + col_direction < BOARD_SIZE):
                # Move one step in the current direction
                current_row += row_direction
                current_col += col_direction
                
                # Check if there's a queen at this position
                if (current_row, current_col) in queen_positions:
                    # Found the first queen in this direction - it can attack the king
                    attacking_queens.append([current_row, current_col])
                    break  # Stop searching in this direction
    
    return attacking_queens
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = queens_attack_the_king(queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0])
    print(result) # [[0, 1], [1, 0], [3, 3]]

    result = queens_attack_the_king(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3])
    print(result) # [[2, 2], [3, 4], [4, 4]]

if __name__ == "__main__":
    main()
