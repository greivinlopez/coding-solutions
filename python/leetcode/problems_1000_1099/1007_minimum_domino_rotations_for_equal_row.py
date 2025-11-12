# --------------------------------------------
# 1007. Minimum Domino Rotations For Equal Row
# --------------------------------------------

# Problem: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row
#
# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves
# of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on
# each half of the tile.)
# 
# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
# 
# Return the minimum number of rotations so that all the values in tops are the
# same, or all the values in bottoms are the same.
# 
# If it cannot be done, return -1.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/05/14/domino.png
# 
# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# 
# Explanation:
# The first figure represents the dominoes as given by tops and bottoms: before we
# do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top
# row equal to 2, as indicated by the second figure.
# 
# Example 2:
# 
# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# 
# Explanation:
# In this case, it is not possible to rotate the dominoes to make one row of
# values equal.
# 
# 
# Constraints:
#         2 <= tops.length <= 2 * 10⁴
#         bottoms.length == tops.length
#         1 <= tops[i], bottoms[i] <= 6


# Solution: https://youtu.be/VD9NACqBCw4
# Credit: Navdeep Singh founder of NeetCode
def min_domino_rotations(tops, bottoms):
    for target in [tops[0], bottoms[0]]:
        missing_t = 0
        missing_b = 0
        for i, pair in enumerate(zip(tops, bottoms)):
            top, bottom = pair
            if not (top == target or bottom == target):
                break
            if top != target:
                missing_t += 1
            if bottom != target:
                missing_b += 1
            if i == len(tops) - 1:
                return min(missing_t, missing_b)
    return -1
    # Time: O(n)
    # Space: O(1)


def main():
    result = min_domino_rotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2])
    print(result) # 2

    result = min_domino_rotations(tops = [3,5,1,2,3], bottoms = [3,6,3,3,4])
    print(result) # -1

if __name__ == "__main__":
    main()
