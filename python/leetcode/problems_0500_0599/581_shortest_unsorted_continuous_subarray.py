# ------------------------------------------
# 581. Shortest Unsorted Continuous Subarray
# ------------------------------------------

# Problem: https://leetcode.com/problems/shortest-unsorted-continuous-subarray
#
# Given an integer array nums, you need to find one continuous subarray such that
# if you only sort this subarray in non-decreasing order, then the whole array
# will be sorted in non-decreasing order.
# 
# Return the shortest such subarray and output its length.
# 
# Example 1:
# 
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# 
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
# 
# Example 2:
# 
# Input: nums = [1,2,3,4]
# Output: 0
# 
# Example 3:
# 
# Input: nums = [1]
# Output: 0
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁴
#         -10⁵ <= nums[i] <= 10⁵
# 
# Follow up: Can you solve it in O(n) time complexity?


# Solution: https://algo.monster/liteproblems/581
# Credit: AlgoMonster
def find_unsorted_subarray(nums):
    # Create a sorted version of the input array
    sorted_nums = sorted(nums)
    
    # Initialize left and right pointers
    left = 0
    right = len(nums) - 1
    
    # Find the leftmost position where the element differs from sorted array
    while left <= right and nums[left] == sorted_nums[left]:
        left += 1
    
    # Find the rightmost position where the element differs from sorted array
    while left <= right and nums[right] == sorted_nums[right]:
        right -= 1
    
    # Calculate the length of the unsorted subarray
    # If left > right, the array is already sorted, so return 0
    # Otherwise, return the length including both endpoints
    return right - left + 1
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = find_unsorted_subarray(nums = [2,6,4,8,10,9,15])
    print(result) # 5

    result = find_unsorted_subarray(nums = [1,2,3,4])
    print(result) # 0

    result = find_unsorted_subarray(nums = [1])
    print(result) # 0

if __name__ == "__main__":
    main()
