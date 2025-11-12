# ------------------------------------
# 1232. Check If It Is a Straight Line
# ------------------------------------

# Problem: https://leetcode.com/problems/check-if-it-is-a-straight-line
#
# You are given an integer array coordinates, coordinates[i] = [x, y], where [x,
# y] represents the coordinate of a point. Check if these points make a straight
# line in the XY plane.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/10/15/untitled-diagram-2.jpg
# 
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2019/10/09/untitled-diagram-1.jpg
# 
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
# 
# 
# Constraints:
#         2 <= coordinates.length <= 1000
#         coordinates[i].length == 2
#         -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
#         coordinates contains no duplicate point.


# Solution: https://algo.monster/liteproblems/1232
# Credit: AlgoMonster
def check_straight_line(coordinates):
    # Extract the first two points as reference points for the line
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    
    # Check if each remaining point is collinear with the first two points
    for x, y in coordinates[2:]:
        # Use cross multiplication to check if the point (x, y) lies on the line
        # formed by points (x1, y1) and (x2, y2)
        if (x - x1) * (y2 - y1) != (y - y1) * (x2 - x1):
            return False
    
    # All points are collinear
    return True
    # Time: O(n)
    # Space: O(1)


def main():
    result = check_straight_line(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
    print(result) # True

    result = check_straight_line(coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])
    print(result) # False

if __name__ == "__main__":
    main()
