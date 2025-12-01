# ---------------------------------
# 1706. Where Will the Ball Fall 🎾
# ---------------------------------

# Problem: https://leetcode.com/problems/where-will-the-ball-fall
#
# You have a 2-D grid of size m x n representing a box, and you have n balls. The
# box is open on the top and bottom sides.
# 
# Each cell in the box has a diagonal board spanning two corners of the cell that
# can redirect a ball to the right or to the left.
#         
#   * A board that redirects the ball to the right spans the top-left corner
#     to the bottom-right corner and is represented in the grid as 1.
#   * A board that redirects the ball to the left spans the top-right corner
#     to the bottom-left corner and is represented in the grid as -1.
# 
# We drop one ball at the top of each column of the box. Each ball can get stuck
# in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped
# pattern between two boards or if a board redirects the ball into either wall of
# the box.
# 
# Return an array answer of size n where answer[i] is the column that the ball
# falls out of at the bottom after dropping the ball from the ith column at the
# top, or -1 if the ball gets stuck in the box.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/09/26/ball.jpg
# 
# Input: grid =
# [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
# Output: [1,-1,-1,-1,-1]
# 
# Explanation: This example is shown in the photo.
# Ball b0 is dropped at column 0 and falls out of the box at column 1.
# Ball b1 is dropped at column 1 and will get stuck in the box between column 2
# and 3 and row 1.
# Ball b2 is dropped at column 2 and will get stuck on the box between column 2
# and 3 and row 0.
# Ball b3 is dropped at column 3 and will get stuck on the box between column 2
# and 3 and row 0.
# Ball b4 is dropped at column 4 and will get stuck on the box between column 2
# and 3 and row 1.
# 
# Example 2:
# 
# Input: grid = [[-1]]
# Output: [-1]
# 
# Explanation: The ball gets stuck against the left wall.
# 
# Example 3:
# 
# Input: grid =
# [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
# Output: [0,1,2,3,4,-1]
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 100
#         grid[i][j] is 1 or -1.


# Solution: https://algo.monster/liteproblems/1706
# Credit: AlgoMonster
def find_ball(grid):
    
    def simulate_ball_drop(row, col):
        # Ball successfully reached the bottom of the grid
        if row == num_rows:
            return col
        
        # Check if ball hits left wall while being directed left
        if col == 0 and grid[row][col] == -1:
            return -1
        
        # Check if ball hits right wall while being directed right
        if col == num_cols - 1 and grid[row][col] == 1:
            return -1
        
        # Check for V-shaped trap: current cell directs right, next cell directs left
        if grid[row][col] == 1 and grid[row][col + 1] == -1:
            return -1
        
        # Check for V-shaped trap: current cell directs left, previous cell directs right
        if grid[row][col] == -1 and grid[row][col - 1] == 1:
            return -1
        
        # Ball continues to next row
        # If current cell is 1, ball moves right; if -1, ball moves left
        if grid[row][col] == 1:
            return simulate_ball_drop(row + 1, col + 1)
        else:
            return simulate_ball_drop(row + 1, col - 1)
    
    # Initialize grid dimensions
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    # Simulate dropping a ball from each column at the top
    result = []
    for starting_col in range(num_cols):
        final_position = simulate_ball_drop(0, starting_col)
        result.append(final_position)
    
    return result
    # Time: O(m * n)
    # Space: O(m)


def main():
    result = find_ball(grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]])
    print(result) # [1, -1, -1, -1, -1]

    result = find_ball(grid = [[-1]])
    print(result) # [-1]

    result = find_ball(grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]])
    print(result) # [0, 1, 2, 3, 4, -1]

if __name__ == "__main__":
    main()
