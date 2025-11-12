# -----------------------------------------------------------
# 2009. Minimum Number of Operations to Make Array Continuous
# -----------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous
#
# You are given an integer array nums. In one operation, you can replace any
# element in nums with any integer.
# 
# nums is considered continuous if both of the following conditions are fulfilled:
# 
#   * All elements in nums are unique.
#   * The difference between the maximum element and the minimum element in
#     nums equals nums.length - 1.
# 
# For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is
# not continuous.
# 
# Return the minimum number of operations to make nums continuous.
# 
# Example 1:
# 
# Input: nums = [4,2,5,3]
# Output: 0
# 
# Explanation: nums is already continuous.
# 
# Example 2:
# 
# Input: nums = [1,2,3,5,6]
# Output: 1
# 
# Explanation: One possible solution is to change the last element to 4.
# The resulting array is [1,2,3,5,4], which is continuous.
# 
# Example 3:
# 
# Input: nums = [1,10,100,1000]
# Output: 3
# 
# Explanation: One possible solution is to:
# - Change the second element to 2.
# - Change the third element to 3.
# - Change the fourth element to 4.
# The resulting array is [1,2,3,4], which is continuous.
# 
# 
# Constraints:
#         1 <= nums.length <= 10^5
#         1 <= nums[i] <= 10^9


# Solution: https://youtu.be/Dd-yJylrcOY
# Credit: Navdeep Singh founder of NeetCode
def min_operations(nums):
    length = len(nums)
    nums = sorted(set(nums))
    res = length
    r = 0
    for l in range(len(nums)):
        while r < len(nums) and nums[r] < nums[l] + length:
            r += 1
        window = r - l
        res = min(res, length - window)
    return res
    # Time: O(n * log(n)) 
    # Space: O(n)


def main():
    result = min_operations([4,2,5,3])
    print(result) # 0

    result = min_operations([1,2,3,5,6])
    print(result) # 1

    result = min_operations([1,10,100,1000])
    print(result) # 3

if __name__ == "__main__":
    main()
