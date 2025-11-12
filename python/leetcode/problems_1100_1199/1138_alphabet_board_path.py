# -------------------------
# 1138. Alphabet Board Path
# -------------------------

# Problem: https://leetcode.com/problems/alphabet-board-path
#
# On an alphabet board, we start at position (0, 0), corresponding to
# character board[0][0].
# 
# Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in
# the diagram below.
# 
# https://assets.leetcode.com/uploads/2019/07/28/azboard.png
# 
# We may make the following moves:
#         
#   * 'U' moves our position up one row, if the position exists on the board;
#   * 'D' moves our position down one row, if the position exists on the board;
#   * 'L' moves our position left one column, if the position exists on the board;
#   * 'R' moves our position right one column, if the position exists on the board;
#   * '!' adds the character board[r][c] at our current position (r, c) to the 
#     answer.
# 
# (Here, the only positions that exist on the board are positions with letters on
# them.)
# 
# Return a sequence of moves that makes our answer equal to target in the minimum
# number of moves.  You may return any path that does so.
# 
# Example 1:
# 
# Input: target = "leet"
# Output: "DDR!UURRR!!DDD!"
# 
# Example 2:
# 
# Input: target = "code"
# Output: "RR!DDRR!UUL!R!"
# 
# 
# Constraints:
#         1 <= target.length <= 100
#         target consists only of English lowercase letters.


# Solution: https://algo.monster/liteproblems/1138
# Credit: AlgoMonster
def alphabet_board_path(target):
    # Initialize starting position at 'a' (0, 0)
    current_row = 0
    current_col = 0
    result_path = []
    
    for char in target:
        # Calculate target position on the board
        # Each row has 5 characters, so divmod by 5 gives row and column
        char_value = ord(char) - ord('a')
        target_row = char_value // 5
        target_col = char_value % 5
        
        # Move left first (important for handling 'z' at position (5, 0))
        # Moving left before down prevents going out of bounds
        while current_col > target_col:
            current_col -= 1
            result_path.append('L')
        
        # Move up
        while current_row > target_row:
            current_row -= 1
            result_path.append('U')
        
        # Move right
        while current_col < target_col:
            current_col += 1
            result_path.append('R')
        
        # Move down last (important for handling 'z' at position (5, 0))
        # Moving down after right ensures we don't go out of bounds
        while current_row < target_row:
            current_row += 1
            result_path.append('D')
        
        # Add selection marker for current character
        result_path.append('!')
    
    # Join all moves into a single string
    return ''.join(result_path)
    # Time: O(n)
    # Space: O(1)


def main():
    result = alphabet_board_path(target = "leet")
    print(result) # RDD!UURRR!!DDD!

    result = alphabet_board_path(target = "code")
    print(result) # RR!RRDD!LUU!R!

if __name__ == "__main__":
    main()
