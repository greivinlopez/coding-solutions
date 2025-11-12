# --------------------
# 780. Reaching Points
# --------------------

# Problem: https://leetcode.com/problems/reaching-points
#
# Given four integers sx, sy, tx, and ty, return true if it is possible to convert
# the point (sx, sy) to the point (tx, ty) through some operations, or false
# otherwise.
# 
# The allowed operation on some point (x, y) is to convert it to either (x, x + y)
# or (x + y, y).
# 
# Example 1:
# 
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: true
# 
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
# 
# Example 2:
# 
# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: false
# 
# Example 3:
# 
# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: true
# 
# 
# Constraints:
#         1 <= sx, sy, tx, ty <= 10⁹


# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def reaching_points(sx, sy, tx, ty):
    # Work backwards from target point by reducing the larger coordinate
    # When tx > ty, the previous step must have been (tx - ty, ty)
    # We use modulo to skip multiple subtraction steps at once
    while tx > sx and ty > sy and tx != ty:
        if tx > ty:
            # Reduce tx by multiples of ty
            tx %= ty
        else:
            # Reduce ty by multiples of tx
            ty %= tx
    
    # Check if we've reached the source point exactly
    if tx == sx and ty == sy:
        return True
    
    # If x-coordinate matches, check if we can reach source by only changing y
    if tx == sx:
        # ty must be reachable from sy by adding tx multiple times
        return ty > sy and (ty - sy) % tx == 0
    
    # If y-coordinate matches, check if we can reach source by only changing x
    if ty == sy:
        # tx must be reachable from sx by adding ty multiple times
        return tx > sx and (tx - sx) % ty == 0
    
    # Cannot reach the source point
    return False
    # Time: O(log(max(tx,ty)))
    # Space: O(1)


def main():
    result = reaching_points(sx = 1, sy = 1, tx = 3, ty = 5)
    print(result) # True

    result = reaching_points(sx = 1, sy = 1, tx = 2, ty = 2)
    print(result) # False

    result = reaching_points(sx = 1, sy = 1, tx = 1, ty = 1)
    print(result) # True

if __name__ == "__main__":
    main()
