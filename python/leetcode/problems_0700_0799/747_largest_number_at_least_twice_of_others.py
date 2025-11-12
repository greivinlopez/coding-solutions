# --------------------------------------------
# 747. Largest Number At Least Twice of Others
# --------------------------------------------

# Problem: https://leetcode.com/problems/largest-number-at-least-twice-of-others
#
# You are given an integer array nums where the largest integer is unique.
# 
# Determine whether the largest element in the array is at least twice as much as
# every other number in the array. If it is, return the index of the largest
# element, or return -1 otherwise.
# 
# Example 1:
# 
# Input: nums = [3,6,1,0]
# Output: 1
# 
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.
# 
# Example 2:
# 
# Input: nums = [1,2,3,4]
# Output: -1
# 
# Explanation: 4 is less than twice the value of 3, so we return -1.
# 
# 
# Constraints:
#         2 <= nums.length <= 50
#         0 <= nums[i] <= 100
#         The largest element in nums is unique.

from heapq import nlargest

# Solution: https://algo.monster/liteproblems/747
# Credit: AlgoMonster
def dominant_index(nums):
    # Find the two largest elements in the array
    # nlargest returns elements in descending order
    largest, second_largest = nlargest(2, nums)
    
    # Check if the largest element is at least twice as large as the second largest
    # If true, return its index; otherwise return -1
    if largest >= 2 * second_largest:
        return nums.index(largest)
    else:
        return -1
    # Time: O(n)
    # Space: O(1)


def main():
    result = dominant_index(nums = [3,6,1,0])
    print(result) # 1

    result = dominant_index(nums = [1,2,3,4])
    print(result) # -1

if __name__ == "__main__":
    main()
