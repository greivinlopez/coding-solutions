# ---------------------------------------
# 1275. Find Winner on a Tic Tac Toe Game
# ---------------------------------------

# Problem: https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game
#
# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-
# Tac-Toe are:
#         
#   * Players take turns placing characters into empty squares ' '.
#   * The first player A always places 'X' characters, while the second player
#     B always places 'O' characters.
#   * 'X' and 'O' characters are always placed into empty squares, never on
#     filled ones.
#   * The game ends when there are three of the same (non-empty) character
#     filling any row, column, or diagonal.
#   * The game also ends if all squares are non-empty.
#   * No more moves can be played if the game is over.
# 
# Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the
# ith move will be played on grid[rowi][coli]. return the winner of the game if it
# exists (A or B). In case the game ends in a draw return "Draw". If there are
# still movements to play return "Pending".
# 
# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe),
# the grid is initially empty, and A will play first.
# 
# Example 1:
# 
# Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# Output: "A"
# 
# Explanation: A wins, they always play first.
# 
# Example 2:
# 
# Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# Output: "B"
# 
# Explanation: B wins.
# 
# Example 3:
# 
# Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# Output: "Draw"
# 
# Explanation: The game ends in a draw since there are no moves to make.
# 
# 
# Constraints:
#         1 <= moves.length <= 9
#         moves[i].length == 2
#         0 <= rowi, coli <= 2
#         There are no repeated elements on moves.
#         moves follow the rules of tic tac toe.


# Solution: https://algo.monster/liteproblems/1275
# Credit: AlgoMonster
def tictactoe(moves):
    total_moves = len(moves)
    
    # Track winning conditions:
    # Index 0-2: row counts (rows 0, 1, 2)
    # Index 3-5: column counts (columns 0, 1, 2)
    # Index 6: main diagonal count (top-left to bottom-right)
    # Index 7: anti-diagonal count (top-right to bottom-left)
    win_conditions = [0] * 8
    
    # Check moves backwards, starting from the last move
    # Step by -2 to only check moves by the same player
    for move_index in range(total_moves - 1, -1, -2):
        row, col = moves[move_index]
        
        # Increment count for this row
        win_conditions[row] += 1
        
        # Increment count for this column (offset by 3 to avoid row indices)
        win_conditions[col + 3] += 1
        
        # Check if move is on main diagonal
        if row == col:
            win_conditions[6] += 1
        
        # Check if move is on anti-diagonal
        if row + col == 2:
            win_conditions[7] += 1
        
        # Check if any winning condition is met (3 in a row/column/diagonal)
        if any(count == 3 for count in win_conditions):
            # Determine winner based on move index parity
            # Even index (0, 2, 4, 6, 8) means player A
            # Odd index (1, 3, 5, 7) means player B
            return "B" if move_index & 1 else "A"
    
    # No winner found - check if board is full
    return "Draw" if total_moves == 9 else "Pending"
    # Time: O(n)
    # Space: O(1)


def main():
    result = tictactoe(moves = [[0,0],[2,0],[1,1],[2,1],[2,2]])
    print(result) # "A"

    result = tictactoe(moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]])
    print(result) # "B"

    result = tictactoe(moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]])
    print(result) # "Draw"

if __name__ == "__main__":
    main()
