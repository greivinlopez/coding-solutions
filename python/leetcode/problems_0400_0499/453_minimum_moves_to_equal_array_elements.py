# ------------------------------------------
# 453. Minimum Moves to Equal Array Elements
# ------------------------------------------

# Problem: https://leetcode.com/problems/minimum-moves-to-equal-array-elements
#
# Given an integer array nums of size n, return the minimum number of moves
# required to make all array elements equal.
# 
# In one move, you can increment n - 1 elements of the array by 1.
# 
# Example 1:
# 
# Input: nums = [1,2,3]
# Output: 3
# 
# Explanation: Only three moves are needed (remember each move increments two
# elements):
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# 
# Example 2:
# 
# Input: nums = [1,1,1]
# Output: 0
# 
# 
# Constraints:
#         n == nums.length
#         1 <= nums.length <= 10⁵
#         -10⁹ <= nums[i] <= 10⁹
#         The answer is guaranteed to fit in a 32-bit integer.


# Solution: https://algo.monster/liteproblems/453
# Credit: AlgoMonster
def min_moves(nums):
    # Find the minimum value in the array
    min_value = min(nums)
    
    # Calculate total sum of all elements
    total_sum = sum(nums)
    
    # The number of moves equals the total difference from minimum
    # This is equivalent to: sum of (each element - min_value)
    return total_sum - min_value * len(nums)
    # Time: O(n)
    # Space: O(1)


def main():
    result = min_moves(nums = [1,2,3])
    print(result) # 3

    result = min_moves(nums = [1,1,1])
    print(result) # 0

if __name__ == "__main__":
    main()
