# -------------------------------------------
# 1658. Minimum Operations To Reduce X To Zero
# -------------------------------------------

# Problem: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero
#
# You are given an integer array nums and an integer x. In one operation, you can
# either remove the leftmost or the rightmost element from the array nums and
# subtract its value from x. Note that this modifies the array for future
# operations.
# 
# Return the minimum number of operations to reduce x to exactly 0 if it is
# possible, otherwise, return -1.
# 
# Example 1:
# 
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x
# to zero.
# 
# Example 2:
# 
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# 
# Example 3:
# 
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the
# first two elements (5 operations in total) to reduce x to zero.
# 
# 
# Constraints:
#         1 <= nums.length <= 10^5
#         1 <= nums[i] <= 10^4
#         1 <= x <= 10^9


# Solution: https://youtu.be/xumn16n7njs
# Credit: Navdeep Singh founder of NeetCode
def min_operations(nums, x):
    # determine sum of subarray remaining after reduction
    target_sum = sum(nums) - x
    # check that x could be reduced to zero
    if target_sum < 0:
        return -1

    n = len(nums)
    min_ops = -1

    # sliding window technique used to find candidate subarrays
    left = 0
    right = 0
    curr_sum = 0
    while right < n:
        curr_sum += nums[right] 
        right += 1

        while left < n and curr_sum > target_sum:
            curr_sum -= nums[left]
            left += 1

        if curr_sum == target_sum:
            ops = n - (right - left) # determine no. of operations used in reduction of nums to candidate subarray 
            min_ops = ops if min_ops == -1 else min(min_ops, ops) # determine if candidate is best candidate thus far

    return min_ops # return best candidate


def main():
    result = min_operations(nums = [1,1,4,2,3], x = 5)
    print(result) # 2

    result = min_operations(nums = [5,6,7,8,9], x = 4)
    print(result) # -1

    result = min_operations(nums = [3,2,20,1,1,3], x = 10)
    print(result) # 5

if __name__ == "__main__":
    main()
