# ------------------------------------------------------------
# 1558. Minimum Numbers of Function Calls to Make Target Array
# ------------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array
#
# You are given an integer array nums. You have an integer array arr of the same
# length with all values set to 0 initially. You also have the following modify
# function:
# 
# https://assets.leetcode.com/uploads/2020/07/10/sample_2_1887.png
# 
# You want to use the modify function to convert arr to nums using the minimum
# number of calls.
# 
# Return the minimum number of function calls to make nums from arr.
# 
# The test cases are generated so that the answer fits in a 32-bit signed integer.
# 
# Example 1:
# 
# Input: nums = [1,5]
# Output: 5
# 
# Explanation: Increment by 1 (second element): [0, 0] to get [0, 1] (1
# operation).
# Double all the elements: [0, 1] -> [0, 2] -> [0, 4] (2 operations).
# Increment by 1 (both elements)  [0, 4] -> [1, 4] -> [1, 5] (2 operations).
# Total of operations: 1 + 2 + 2 = 5.
# 
# Example 2:
# 
# Input: nums = [2,2]
# Output: 3
# 
# Explanation: Increment by 1 (both elements) [0, 0] -> [0, 1] -> [1, 1] (2
# operations).
# Double all the elements: [1, 1] -> [2, 2] (1 operation).
# Total of operations: 2 + 1 = 3.
# 
# Example 3:
# 
# Input: nums = [4,2,5]
# Output: 6
# 
# Explanation: (initial)[0,0,0] -> [1,0,0] -> [1,0,1] -> [2,0,2] -> [2,1,2] ->
# [4,2,4] -> [4,2,5](nums).
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         0 <= nums[i] <= 10⁹


# Solution: https://algo.monster/liteproblems/1558
# Credit: AlgoMonster
def min_operations(nums):
    # Count total number of set bits (1s) in binary representation of all numbers
    # This represents the number of subtraction operations needed
    # Works only with Python 3.10+. Earlier versions use bin(num).count('1')
    total_set_bits = sum(num.bit_count() for num in nums)
    
    # Find the highest bit position among all numbers
    # bit_length() - 1 gives the number of division operations needed
    # max(0, ...) ensures we don't return negative for empty array or all zeros
    max_bit_position = max(0, max(nums).bit_length() - 1) if nums else 0
    
    # Total operations = subtraction operations + division operations
    return total_set_bits + max_bit_position


def main():
    result = min_operations(nums = [1,5])
    print(result) # 5

    result = min_operations(nums = [2,2])
    print(result) # 3

    result = min_operations(nums = [4,2,5])
    print(result) # 6

if __name__ == "__main__":
    main()
