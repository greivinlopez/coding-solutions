# ---------------------------
# 1591. Strange Printer II 🖨️
# ---------------------------

# Problem: https://leetcode.com/problems/strange-printer-ii
#
# There is a strange printer with the following two special requirements:
#         
#   * On each turn, the printer will print a solid rectangular pattern of a
#     single color on the grid. This will cover up the existing colors in the
#     rectangle.
#   * Once the printer has used a color for the above operation, the same
#     color cannot be used again.
# 
# You are given a m x n matrix targetGrid, where targetGrid[row][col] is the color
# in the position (row, col) of the grid.
# 
# Return true if it is possible to print the matrix targetGrid, otherwise, return
# false.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/12/23/print1.jpg
# 
# Input: targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
# Output: true
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/12/23/print2.jpg
# 
# Input: targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
# Output: true
# 
# Example 3:
# 
# Input: targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
# Output: false
# 
# Explanation: It is impossible to form targetGrid because it is not allowed to
# print the same color in different turns.
# 
# 
# Constraints:
#         m == targetGrid.length
#         n == targetGrid[i].length
#         1 <= m, n <= 60
#         1 <= targetGrid[row][col] <= 60

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/1591
# Credit: AlgoMonster
def is_printable(targetGrid):
    colorRect = defaultdict(lambda: [float('inf'), float('inf'), float('-inf'), float('-inf')])

    for i in range(len(targetGrid)):
        for j in range(len(targetGrid[0])):
            color = targetGrid[i][j]
            colorRect[color][0] = min(colorRect[color][0], i)
            colorRect[color][1] = min(colorRect[color][1], j)
            colorRect[color][2] = max(colorRect[color][2], i)
            colorRect[color][3] = max(colorRect[color][3], j)

    graph = defaultdict(set)

    for color in colorRect:
        iStart, jStart, iEnd, jEnd = colorRect[color]
        for i in range(iStart, iEnd+1):
            for j in range(jStart, jEnd+1):
                if targetGrid[i][j] != color:
                    graph[color].add(targetGrid[i][j])

    colorState = defaultdict(int)

    def hasCycle(v):
        colorState[v] = 1
        for u in graph[v]:
            if colorState[u] == 1 or ((u not in colorState or colorState[u] == 0) and hasCycle(u)):
                return True
        colorState[v] = 2
        return False

    return not any(hasCycle(n) for n in range(1, 61) if n not in colorState or colorState[n] == 0)
    # Time: O(c * m * n)
    # Space: O(c²)
    # c = the number of unique colors (which is at most 60 in this specific problem context)
    # m = the number of rows
    # n = the number of columns


def main():
    result = is_printable(targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]])
    print(result) # True

    result = is_printable(targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]])
    print(result) # True

    result = is_printable(targetGrid = [[1,2,1],[2,1,2],[1,2,1]])
    print(result) # False

if __name__ == "__main__":
    main()
