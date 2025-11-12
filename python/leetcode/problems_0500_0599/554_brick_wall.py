# ------------------
# 554. Brick Wall 🧱
# ------------------

# Problem: https://leetcode.com/problems/brick-wall/
# 
# There is a rectangular brick wall in front of you with n rows of bricks. 
# The ith row has some number of bricks each of the same height (i.e., one unit) 
# but they can be of different widths. The total width of each row is the same.
# 
# Draw a vertical line from the top to the bottom and cross the least bricks. 
# If your line goes through the edge of a brick, then the brick is not 
# considered as crossed. You cannot draw a line just along one of the two 
# vertical edges of the wall, in which case the line will obviously cross no 
# bricks.
# 
# Given the 2D array wall that contains the information about the wall, return 
# the minimum number of crossed bricks after drawing such a vertical line.
# 
#  
# Example 1:
# 
# Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# Output: 2
# 
# 
# Example 2:
# 
# Input: wall = [[1],[1],[1]]
# Output: 3
# 
#  
# Constraints:
# 
# 	n == wall.length
# 	1 <= n <= 10^4
# 	1 <= wall[i].length <= 10^4
# 	1 <= sum(wall[i].length) <= 2 * 10^4
# 	sum(wall[i]) is the same for each row i.
# 	1 <= wall[i][j] <= 2^31 - 1


# Solution: https://youtu.be/Kkmv2h48ekw
# Credit: Navdeep Singh founder of NeetCode
def least_bricks(wall):
    countGap = { 0 : 0 }    # { Position : Gap count }

    for r in wall:
        total = 0   # Position
        for b in r[:-1]:
            total += b
            countGap[total] = 1 + countGap.get(total, 0)

    return len(wall) - max(countGap.values())    # Total number of rows - Max gap


def main():
    result = least_bricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]])
    print(result) # 2

    result = least_bricks([[1],[1],[1]])
    print(result) # 3

if __name__ == "__main__":
    main()
