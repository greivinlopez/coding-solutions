# --------------------------------------------
# 915. Partition Array into Disjoint Intervals
# --------------------------------------------

# Problem: https://leetcode.com/problems/partition-array-into-disjoint-intervals
#
# Given an integer array nums, partition it into two (contiguous) subarrays left
# and right so that:
#         
#   * Every element in left is less than or equal to every element in right.
#   * left and right are non-empty.
#   * left has the smallest possible size.
# 
# Return the length of left after such a partitioning.
# 
# Test cases are generated such that partitioning exists.
# 
# Example 1:
# 
# Input: nums = [5,0,3,8,6]
# Output: 3
# 
# Explanation: left = [5,0,3], right = [8,6]
# 
# Example 2:
# 
# Input: nums = [1,1,1,0,6,12]
# Output: 4
# 
# Explanation: left = [1,1,1,0], right = [6,12]
# 
# 
# Constraints:
#         2 <= nums.length <= 10⁵
#         0 <= nums[i] <= 10⁶
#         There is at least one valid answer for the given input.


# Solution: https://algo.monster/liteproblems/915
# Credit: AlgoMonster
def partition_disjoint(nums):
    n = len(nums)
    
    # Build suffix minimum array
    # min_suffix[i] stores the minimum value from index i to the end
    min_suffix = [float('inf')] * (n + 1)
    for i in range(n - 1, -1, -1):
        min_suffix[i] = min(nums[i], min_suffix[i + 1])
    
    # Track maximum value in the left partition
    max_left = 0
    
    # Iterate through possible partition points
    # i represents the size of the left partition (1-indexed)
    for i, value in enumerate(nums, 1):
        # Update maximum in left partition
        max_left = max(max_left, value)
        
        # Check if all elements in left partition <= all elements in right partition
        # This is true when max of left partition <= min of right partition
        if max_left <= min_suffix[i]:
            return i
    # Time: O(n)
    # Space: O(n)


def main():
    result = partition_disjoint(nums = [5,0,3,8,6])
    print(result) # 3

    result = partition_disjoint(nums = [1,1,1,0,6,12])
    print(result) # 4

if __name__ == "__main__":
    main()
