# -------------------------------------
# 688. Knight Probability in Chessboard
# -------------------------------------

# Problem: https://leetcode.com/problems/knight-probability-in-chessboard
#
# On an n x n chessboard, a knight starts at the cell (row, column) and attempts
# to make exactly k moves. The rows and columns are 0-indexed, so the top-left
# cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
# 
# A chess knight has eight possible moves it can make, as illustrated below. Each
# move is two cells in a cardinal direction, then one cell in an orthogonal
# direction.
# 
# https://assets.leetcode.com/uploads/2018/10/12/knight.png
# 
# Each time the knight is to move, it chooses one of eight possible moves
# uniformly at random (even if the piece would go off the chessboard) and moves
# there.
# 
# The knight continues moving until it has made exactly k moves or has moved off
# the chessboard.
# 
# Return the probability that the knight remains on the board after it has stopped
# moving.
# 
# Example 1:
# 
# Input: n = 3, k = 2, row = 0, column = 0
# Output: 0.06250
# 
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on
# the board.
# From each of those positions, there are also two moves that will keep the knight
# on the board.
# The total probability the knight stays on the board is 0.0625.
# 
# Example 2:
# 
# Input: n = 1, k = 0, row = 0, column = 0
# Output: 1.00000
# 
# 
# Constraints:
#         1 <= n <= 25
#         0 <= k <= 100
#         0 <= row, column <= n - 1


# Solution: https://algo.monster/liteproblems/688
# Credit: AlgoMonster
def knight_probability(n, k, row, column):
    # dp[moves][r][c] represents the probability of knight staying on board
    # after 'moves' moves starting from position (r, c)
    dp = [[[0.0] * n for _ in range(n)] for _ in range(k + 1)]
    
    # Base case: with 0 moves, knight is always on board (probability = 1)
    for r in range(n):
        for c in range(n):
            dp[0][r][c] = 1.0
    
    # All 8 possible knight moves: (row_offset, col_offset)
    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    
    # Fill the dp table for each number of moves from 1 to k
    for moves in range(1, k + 1):
        for r in range(n):
            for c in range(n):
                # For each position, calculate probability by summing
                # probabilities from all valid previous positions
                for row_offset, col_offset in knight_moves:
                    prev_row = r + row_offset
                    prev_col = c + col_offset
                    
                    # Check if the previous position is within the board
                    if 0 <= prev_row < n and 0 <= prev_col < n:
                        # Add probability from previous position divided by 8
                        # (since knight has 8 possible moves)
                        dp[moves][r][c] += dp[moves - 1][prev_row][prev_col] / 8.0
    
    # Return the probability at the starting position after k moves
    return dp[k][row][column]
    # Time: O(k * n²)
    # Space: O(k * n²)


def main():
    result = knight_probability(n = 3, k = 2, row = 0, column = 0)
    print(result) # 0.06250

    result = knight_probability(n = 1, k = 0, row = 0, column = 0)
    print(result) # 1.00000

if __name__ == "__main__":
    main()
