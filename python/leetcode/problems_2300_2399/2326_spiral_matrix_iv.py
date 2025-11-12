# -------------------------
# 2326. Spiral Matrix IV 🌀
# -------------------------

# Problem: https://leetcode.com/problems/spiral-matrix-iv
#
# You are given two integers m and n, which represent the dimensions of a matrix.
# 
# You are also given the head of a linked list of integers.
# 
# Generate an m x n matrix that contains the integers in the linked list presented
# in spiral order (clockwise), starting from the top-left of the matrix. If there
# are remaining empty spaces, fill them with -1.
# 
# Return the generated matrix.
# 
# Example 1:
# 
# Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
# Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
# 
# Explanation: The diagram above shows how the values are printed in the matrix.
# Note that the remaining spaces in the matrix are filled with -1.
# 
# Example 2:
# 
# Input: m = 1, n = 4, head = [0,1,2]
# Output: [[0,1,2,-1]]
# 
# Explanation: The diagram above shows how the values are printed from left to
# right in the matrix.
# The last space in the matrix is set to -1.
# 
# 
# Constraints:
#         1 <= m, n <= 10^5
#         1 <= m * n <= 10^5
#         The number of nodes in the list is in the range [1, m * n].
#         0 <= Node.val <= 1000

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import from_list

# Solution: https://youtu.be/sOV1nRhmsMQ
# Credit: Navdeep Singh founder of NeetCode
def spiral_matrix(m, n, head):
    left, right = 0, n
    top, bottom = 0, m
    grid = [[-1] * n for _ in range(m)]

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    r, c, d = 0, 0, 0  # current row, col & direction

    while head:
        dr, dc = directions[d]

        while head and left <= c < right and top <= r < bottom and grid[r][c] == -1:
            grid[r][c] = head.val
            head = head.next
            r, c = r + dr, c + dc

        r, c = r - dr, c - dc
        d = (d + 1) % 4
        dr, dc = directions[d]
        r, c = r + dr, c + dc

    return grid
    # Time: O(m * n) 
    # Space: O(m * n) 


def main():
    result = spiral_matrix(m = 3, n = 5, head = from_list([3,0,2,6,8,1,7,9,4,2,5,5,0]))
    print(result) # [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]

    result = spiral_matrix(m = 1, n = 4, head = from_list([0,1,2]))
    print(result) # [[0,1,2,-1]]

if __name__ == "__main__":
    main()
