# -------------------------------------------------
# 2033. Minimum Operations to Make a Uni-Value Grid
# -------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid
#
# You are given a 2D integer grid of size m x n and an integer x. In one
# operation, you can add x to or subtract x from any element in the grid.
# 
# A uni-value grid is a grid where all the elements of it are equal.
# 
# Return the minimum number of operations to make the grid uni-value. If it is not
# possible, return -1.
# 
# Example 1:
# 
# Input: grid = [[2,4],[6,8]], x = 2
# Output: 4
# 
# Explanation: We can make every element equal to 4 by doing the following:
# - Add x to 2 once.
# - Subtract x from 6 once.
# - Subtract x from 8 twice.
# A total of 4 operations were used.
# 
# Example 2:
# 
# Input: grid = [[1,5],[2,3]], x = 1
# Output: 5
# 
# Explanation: We can make every element equal to 3.
# 
# Example 3:
# 
# Input: grid = [[1,2],[3,4]], x = 2
# Output: -1
# 
# Explanation: It is impossible to make every element equal.
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 10^5
#         1 <= m * n <= 10^5
#         1 <= x, grid[i][j] <= 10^4


# Solution: https://youtu.be/2LfVNDlx8mY
# Credit: Navdeep Singh founder of NeetCode
def min_operations(grid, x):
    # 1. Check all remainders
    # 2. Flatten and sort the input
    # 3. Prefix sum / suffix sum

    total = 0
    for row in grid:
        for n in row:
            total += n
            if n % x != grid[0][0] % x:
                return -1

    nums = [n for row in grid for n in row]
    nums.sort()

    prefix = 0
    res = float("inf")
    for i in range(len(nums)):
        cost_left = nums[i] * i - prefix
        cost_right = total - prefix - (nums[i] * (len(nums) - i))
        operations = (cost_left + cost_right) // x
        res = min(res, operations)
        prefix += nums[i]

    return res
    # Time: O((R * C) * log(R * C)) where R is the number of rows and C the number of columns
    # Space: O(R * C)


def main():
    result = min_operations(grid = [[2,4],[6,8]], x = 2)
    print(result) # 4

    result = min_operations(grid = [[1,5],[2,3]], x = 1)
    print(result) # 5

    result = min_operations(grid = [[1,2],[3,4]], x = 2)
    print(result) # -1

if __name__ == "__main__":
    main()
