# ---------------------------------------------
# 462. Minimum Moves to Equal Array Elements II
# ---------------------------------------------

# Problem: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii
#
# Given an integer array nums of size n, return the minimum number of moves
# required to make all array elements equal.
# 
# In one move, you can increment or decrement an element of the array by 1.
# 
# Test cases are designed so that the answer will fit in a 32-bit integer.
# 
# Example 1:
# 
# Input: nums = [1,2,3]
# Output: 2
# 
# Explanation:
# Only two moves are needed (remember each move increments or decrements one
# element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
# 
# Example 2:
# 
# Input: nums = [1,10,2,9]
# Output: 16
# 
# 
# Constraints:
#         n == nums.length
#         1 <= nums.length <= 10⁵
#         -10⁹ <= nums[i] <= 10⁹


# Solution: https://algo.monster/liteproblems/462
# Credit: AlgoMonster
def min_moves_2(nums):
    # Sort the array to find the median
    nums.sort()
    
    # Find the median element (middle element for odd length, 
    # or either middle element for even length)
    # Using bit shift (>> 1) is equivalent to integer division by 2
    median = nums[len(nums) >> 1]
    
    # Calculate total moves as sum of absolute differences from median
    # Each absolute difference represents the number of moves for that element
    total_moves = sum(abs(num - median) for num in nums)
    
    return total_moves
    # Time: O(n * log(n))
    # Space: O(1)


def main():
    result = min_moves_2(nums = [1,2,3])
    print(result) # 2

    result = min_moves_2(nums = [1,10,2,9])
    print(result) # 16

if __name__ == "__main__":
    main()
