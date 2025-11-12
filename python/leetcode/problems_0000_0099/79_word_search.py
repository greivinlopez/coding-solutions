# -----------------
# 79. Word Search
# -----------------

# Problem: https://leetcode.com/problems/word-search/
# 
# Given an m x n grid of characters board and a string word, return true if word 
# exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where 
# adjacent cells are horizontally or vertically neighboring. The same letter cell 
# may not be used more than once.

# Solution: https://youtu.be/pfiQ_PS1g8E
# Credit: Navdeep Singh founder of NeetCode
from collections import Counter
def exist(board, word):
    # O(n * m * 4^n)
    ROWS, COLS = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (
            min(r, c) < 0
            or r >= ROWS
            or c >= COLS
            or word[i] != board[r][c]
            or (r, c) in path
        ):
            return False
        path.add((r, c))
        res = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )
        path.remove((r, c))
        return res

    # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
    count = sum(map(Counter, board), Counter())
    if count[word[0]] > count[word[-1]]:
        word = word[::-1]
        
    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
    return False

# Solution: https://youtu.be/Sn2DqF-S2h8
# Credit: Greg Hogg
def exist_alt(board, word):
    # Time: O((m*n)^2)
    # Space: O(W)
    m = len(board)
    n = len(board[0])
    W = len(word)

    if m == 1 and n == 1:
        return board[0][0] == word

    def backtrack(pos, index):
        i, j = pos

        if index == W:
            return True

        if board[i][j] != word[index]:
            return False

        char = board[i][j]
        board[i][j] = "#"

        for i_off, j_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            r, c = i + i_off, j + j_off

            if 0 <= r < m and 0 <= c < n:
                if backtrack((r, c), index + 1):
                    return True

        board[i][j] = char
        return False

    for i in range(m):
        for j in range(n):
            if backtrack((i, j), 0):
                return True

    return False

def main():
    result = exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") # True
    print(result)
    result = exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE") # True
    print(result)
    result = exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB") # False
    print(result)

if __name__ == "__main__":
    main()