# --------------------------
# 611. Valid Triangle Number
# --------------------------

# Problem: https://leetcode.com/problems/valid-triangle-number
#
# Given an integer array nums, return the number of triplets chosen from the array
# that can make triangles if we take them as side lengths of a triangle.
# 
# Example 1:
# 
# Input: nums = [2,2,3,4]
# Output: 3
# 
# Explanation: Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# 
# Example 2:
# 
# Input: nums = [4,2,3,4]
# Output: 4
# 
# 
# Constraints:
#         1 <= nums.length <= 1000
#         0 <= nums[i] <= 1000

from bisect import bisect_left

# Solution: https://algo.monster/liteproblems/611
# Credit: AlgoMonster
def triangle_number(nums):
    # Sort the array to enable binary search and ensure a <= b <= c
    nums.sort()
    
    # Initialize counter and get array length
    triangle_count = 0
    array_length = len(nums)
    
    # Iterate through all possible first sides (smallest in the triangle)
    for first_side_idx in range(array_length - 2):
        # Iterate through all possible second sides (middle value)
        for second_side_idx in range(first_side_idx + 1, array_length - 1):
            # Find the largest valid third side using binary search
            # We need: first_side + second_side > third_side
            # So we search for the leftmost position where nums[k] >= first_side + second_side
            sum_of_two_sides = nums[first_side_idx] + nums[second_side_idx]
            insertion_point = bisect_left(nums, sum_of_two_sides, lo=second_side_idx + 1)
            
            # The largest valid index is insertion_point - 1
            largest_valid_idx = insertion_point - 1
            
            # Count all valid triangles with current first and second sides
            # All indices from second_side_idx + 1 to largest_valid_idx form valid triangles
            triangle_count += largest_valid_idx - second_side_idx
    
    return triangle_count
    # Time: O(n² * log(n))
    # Space: O(1) (or O(logN) or O(N) depending on the sort implementation).


def main():
    result = triangle_number(nums = [2,2,3,4])
    print(result) # 3

    result = triangle_number(nums = [4,2,3,4])
    print(result) # 4

if __name__ == "__main__":
    main()
