# ------------------------------------
# 1301. Number of Paths with Max Score
# ------------------------------------

# Problem: https://leetcode.com/problems/number-of-paths-with-max-score
#
# You are given a square board of characters. You can move on the board starting
# at the bottom right square marked with the character 'S'.
# 
# You need to reach the top left square marked with the character 'E'. The rest of
# the squares are labeled either with a numeric character 1, 2, ..., 9 or with an
# obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if
# there is no obstacle there.
# 
# Return a list of two integers: the first integer is the maximum sum of numeric
# characters you can collect, and the second is the number of such paths that you
# can take to get that maximum sum, taken modulo 10^9 + 7.
# 
# In case there is no path, return [0, 0].
# 
# Example 1:
# 
# Input: board = ["E23","2X2","12S"]
# Output: [7,1]
# 
# Example 2:
# 
# Input: board = ["E12","1X1","21S"]
# Output: [4,2]
# 
# Example 3:
# 
# Input: board = ["E11","XXX","11S"]
# Output: [0,0]
# 
# 
# Constraints:
#         2 <= board.length == board[i].length <= 100


# Solution: https://algo.monster/liteproblems/1301
# Credit: AlgoMonster
def paths_with_max_score(board):

    def update_cell(curr_row: int, curr_col: int, prev_row: int, prev_col: int) -> None:
        # Skip if previous cell is out of bounds or unreachable
        if prev_row >= board_size or prev_col >= board_size or max_score[prev_row][prev_col] == -1:
            return
        
        # Skip if current cell is obstacle or start position
        if board[curr_row][curr_col] in "XS":
            return
        
        # If previous cell has better score, update current cell
        if max_score[prev_row][prev_col] > max_score[curr_row][curr_col]:
            max_score[curr_row][curr_col] = max_score[prev_row][prev_col]
            path_count[curr_row][curr_col] = path_count[prev_row][prev_col]
        # If previous cell has same score, add its path count to current
        elif max_score[prev_row][prev_col] == max_score[curr_row][curr_col]:
            path_count[curr_row][curr_col] += path_count[prev_row][prev_col]
    
    board_size = len(board)
    
    # max_score[i][j] stores the maximum score to reach cell (i, j)
    max_score = [[-1] * board_size for _ in range(board_size)]
    
    # path_count[i][j] stores the number of paths with maximum score to reach cell (i, j)
    path_count = [[0] * board_size for _ in range(board_size)]
    
    # Initialize the end position 'S' at bottom-right corner
    max_score[-1][-1] = 0
    path_count[-1][-1] = 1
    
    # Process cells from bottom-right to top-left
    for row in range(board_size - 1, -1, -1):
        for col in range(board_size - 1, -1, -1):
            # Update current cell from three possible previous cells
            update_cell(row, col, row + 1, col)      # Cell below
            update_cell(row, col, row, col + 1)      # Cell to the right
            update_cell(row, col, row + 1, col + 1)  # Cell diagonally down-right
            
            # Add the score of current cell if it's reachable and contains a digit
            if max_score[row][col] != -1 and board[row][col].isdigit():
                max_score[row][col] += int(board[row][col])
    
    MOD = 10**9 + 7
    
    # Return result for start position 'E' at top-left corner
    if max_score[0][0] == -1:
        return [0, 0]
    else:
        return [max_score[0][0], path_count[0][0] % MOD]
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = paths_with_max_score(board = ["E23","2X2","12S"])
    print(result) # [7, 1]

    result = paths_with_max_score(board = ["E12","1X1","21S"])
    print(result) # [4, 2]

    result = paths_with_max_score(board = ["E11","XXX","11S"])
    print(result) # [0, 0]

if __name__ == "__main__":
    main()
