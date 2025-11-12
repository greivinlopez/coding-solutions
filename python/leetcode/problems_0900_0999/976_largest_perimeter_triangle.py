# -------------------------------
# 976. Largest Perimeter Triangle
# -------------------------------

# Problem: https://leetcode.com/problems/largest-perimeter-triangle
#
# Given an integer array nums, return the largest perimeter of a triangle with a
# non-zero area, formed from three of these lengths. If it is impossible to form
# any triangle of a non-zero area, return 0.
# 
# Example 1:
# 
# Input: nums = [2,1,2]
# Output: 5
# 
# Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
# 
# Example 2:
# 
# Input: nums = [1,2,1,10]
# Output: 0
# 
# Explanation:
# You cannot use the side lengths 1, 1, and 2 to form a triangle.
# You cannot use the side lengths 1, 1, and 10 to form a triangle.
# You cannot use the side lengths 1, 2, and 10 to form a triangle.
# As we cannot use any three side lengths to form a triangle of non-zero area, we
# return 0.
# 
# 
# Constraints:
#         3 <= nums.length <= 10⁴
#         1 <= nums[i] <= 10⁶


# Solution: https://algo.monster/liteproblems/976
# Credit: AlgoMonster
def largest_perimeter(nums):
    # Sort the array in ascending order
    nums.sort()
    
    # Iterate from the largest element backwards
    # We need at least 3 elements to form a triangle
    for i in range(len(nums) - 1, 1, -1):
        # Get the three consecutive elements (in sorted order)
        largest_side = nums[i]
        middle_side = nums[i - 1]
        smallest_side = nums[i - 2]
        
        # Check triangle inequality: sum of two smaller sides must be greater than the largest side
        # For a valid triangle: a + b > c (where c is the largest side)
        if smallest_side + middle_side > largest_side:
            # Return the perimeter of the valid triangle
            return smallest_side + middle_side + largest_side
    
    # No valid triangle can be formed
    return 0
    # Time: O(n * log(n))
    # Space: O(1) or O(n) depending on the sorting algorithm implementation.


def main():
    result = largest_perimeter(nums = [2,1,2])
    print(result) # 5

    result = largest_perimeter(nums = [1,2,1,10])
    print(result) # 0

if __name__ == "__main__":
    main()
