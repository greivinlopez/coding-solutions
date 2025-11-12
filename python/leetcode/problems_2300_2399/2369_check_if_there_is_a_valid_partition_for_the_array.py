# -------------------------------------------------------
# 2369. Check if There is a Valid Partition For The Array
# -------------------------------------------------------

# Problem: https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array
#
# You are given a 0-indexed integer array nums. You have to partition the array
# into one or more contiguous subarrays.
# 
# We call a partition of the array valid if each of the obtained subarrays
# satisfies one of the following conditions:
#         
#   1. The subarray consists of exactly 2, equal elements. For example, the
#      subarray [2,2] is good.
#   2. The subarray consists of exactly 3, equal elements. For example, the
#      subarray [4,4,4] is good.
#   3. The subarray consists of exactly 3 consecutive increasing elements, that
#      is, the difference between adjacent elements is 1. For example, the subarray
#      [3,4,5] is good, but the subarray [1,3,5] is not.
# 
# Return true if the array has at least one valid partition. Otherwise, return
# false.
# 
# Example 1:
# 
# Input: nums = [4,4,4,5,6]
# Output: true
# 
# Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
# This partition is valid, so we return true.
# 
# Example 2:
# 
# Input: nums = [1,1,1,2]
# Output: false
# 
# Explanation: There is no valid partition for this array.
# 
# 
# Constraints:
#         2 <= nums.length <= 10⁵
#         1 <= nums[i] <= 10⁶


# Solution: https://youtu.be/OxXPiwWFdTI
# Credit: Navdeep Singh founder of NeetCode
def valid_partition_memo(nums):
    # Memoization solution
    dp = {}
    def dfs(i):
        if i == len(nums):
            return True
        if i in dp:
            return dp[i]
        res = False
        if i < len(nums) - 1 and nums[i] == nums[i + 1]:
            res = dfs(i + 2)
        if i < len(nums) - 2:
            if (nums[i] == nums[i + 1] and nums[i + 1] == nums[i + 2]) or (nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]):
                res = res or dfs(i + 3)
        dp[i] = res
        return res
    return dfs(0)
    # Time: O(n) 
    # Space: O(n)

def valid_partition(nums):
    # Bottom Up Dynamic Programming Solution
    two = nums[-1] == nums[-2]
    if len(nums) == 2:
        return two
    three = (nums[-1] == nums[-2] == nums[-3] or
                nums[-3] + 1 == nums[-2] == nums[-1] - 1)
    dp = [three, two, False]
    for i in range(len(nums) - 4, -1, -1):
        cur = (nums[i] == nums[i + 1] and dp[1])
        cur = cur or (
            (nums[i] == nums[i + 1] and nums[i + 1] == nums[i + 2]) or
            (nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2])
        ) and dp[2]
        dp = [cur, dp[0], dp[1]]
    return dp[0]
    # Time: O(n)
    # Space: O(1)


def main():
    result = valid_partition(nums = [4,4,4,5,6])
    print(result) # True

    result = valid_partition(nums = [1,1,1,2])
    print(result) # False

if __name__ == "__main__":
    main()
