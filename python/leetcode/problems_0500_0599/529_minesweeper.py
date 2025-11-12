# ----------------
# 529. Minesweeper
# ----------------

# Problem: https://leetcode.com/problems/minesweeper
#
# Let's play the minesweeper game (Wikipedia, online game)!
# 
# You are given an m x n char matrix board representing the game board where:
# 
#   * 'M' represents an unrevealed mine,
#   * 'E' represents an unrevealed empty square,
#   * 'B' represents a revealed blank square that has no adjacent mines (i.e., 
#      above, below, left, right, and all 4 diagonals),
#   * digit ('1' to '8') represents how many mines are adjacent to this revealed 
#     square, and 
#   * 'X' represents a revealed mine.
# 
# You are also given an integer array click where click = [clickr, clickc]
# represents the next click position among all the unrevealed squares ('M' or
# 'E').
# 
# Return the board after revealing this position according to the following rules:
# 
#   1. If a mine 'M' is revealed, then the game is over. You should change it
#      to 'X'.
#   2. If an empty square 'E' with no adjacent mines is revealed, then change
#      it to a revealed blank 'B' and all of its adjacent unrevealed squares should be
#      revealed recursively.
#   3. If an empty square 'E' with at least one adjacent mine is revealed, then
#      change it to a digit ('1' to '8') representing the number of adjacent mines.
#   4. Return the board when no more squares will be revealed.
# 
# Example 1:
# 
# Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"
# ],["E","E","E","E","E"]], click = [3,0]
# Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B",
# "B","B","B","B"]]
# 
# Example 2:
# 
# Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"
# ],["B","B","B","B","B"]], click = [1,2]
# Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B",
# "B","B","B","B"]]
# 
# Constraints:
#         m == board.length
#         n == board[i].length
#         1 <= m, n <= 50
#         board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
#         click.length == 2
#         0 <= clickᵣ < m
#         0 <= click꜀ < n
#         board[clickᵣ][click꜀] is either 'M' or 'E'.


# Solution: https://algo.monster/liteproblems/529
# Credit: AlgoMonster
def update_board(board, click):
    def dfs(row, col):
        # Count adjacent mines
        mine_count = 0
        for x in range(row - 1, row + 2):
            for y in range(col - 1, col + 2):
                # Check if position is valid and contains a mine
                if 0 <= x < rows and 0 <= y < cols and board[x][y] == "M":
                    mine_count += 1
        
        if mine_count > 0:
            # If there are adjacent mines, show the count
            board[row][col] = str(mine_count)
        else:
            # No adjacent mines, mark as blank and continue revealing
            board[row][col] = "B"
            
            # Recursively reveal all adjacent empty cells
            for x in range(row - 1, row + 2):
                for y in range(col - 1, col + 2):
                    # Only process valid positions with unrevealed empty cells
                    if 0 <= x < rows and 0 <= y < cols and board[x][y] == "E":
                        dfs(x, y)
    
    # Get board dimensions
    rows, cols = len(board), len(board[0])
    
    # Extract click coordinates
    click_row, click_col = click
    
    # Handle click on mine
    if board[click_row][click_col] == "M":
        board[click_row][click_col] = "X"  # Game over - mine exploded
    else:
        # Click on empty cell - start revealing process
        dfs(click_row, click_col)
    
    return board


def main():
    board = [["E","E","E","E","E"],
             ["E","E","M","E","E"],
             ["E","E","E","E","E"],
             ["E","E","E","E","E"]]
    result = update_board(board, [3,0])
    print(result) # [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]

    board = [["B","1","E","1","B"],
             ["B","1","M","1","B"],
             ["B","1","1","1","B"],
             ["B","B","B","B","B"]]
    result = update_board(board, [1,2])
    print(result) # [['B', '1', 'E', '1', 'B'], ['B', '1', 'X', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]

if __name__ == "__main__":
    main()
