# ------------------------------
# 419. Battleships in a Board ⛴️
# ------------------------------

# Problem: https://leetcode.com/problems/battleships-in-a-board
#
# Given an m x n matrix board where each cell is a battleship 'X' or empty '.',
# return the number of the battleships on board.
# 
# Battleships can only be placed horizontally or vertically on board. In other
# words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k
# rows, 1 column), where k can be of any size. At least one horizontal or vertical
# cell separates between two battleships (i.e., there are no adjacent
# battleships).
# 
# Example 1:
# 
# Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
# Output: 2
# 
# Example 2:
# 
# Input: board = [["."]]
# Output: 0
# 
# 
# Constraints:
#         m == board.length
#         n == board[i].length
#         1 <= m, n <= 200
#         board[i][j] is either '.' or 'X'.
# 
# 
# Follow up: Could you do it in one-pass, using only O(1) extra memory and without
# modifying the values board?


# Solution: https://leetcode.com/problems/battleships-in-a-board/solutions/2523176/python-o-nm-one-liner-solution-without-modifying-board
# Credit: Ahmad Elkholi -> https://leetcode.com/u/ahmadheshamzaki/
def count_battleships(board):
    count = 0
    
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == "X":
                if (i == 0 or board[i - 1][j] == ".") and\
                    (j == 0 or board[i][j - 1] == "."):
                        count += 1
                        
    return count
    # Time: O(m * n)
    # Space: O(1)
    # m = number of rows
    # n = number of columns


def main():
    result = count_battleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
    print(result) # 2

    result = count_battleships([["."]])
    print(result) # 0

if __name__ == "__main__":
    main()
