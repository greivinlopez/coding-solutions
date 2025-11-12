# ----------------------------
# 410. Split Array Largest Sum
# ----------------------------

# Problem: https://leetcode.com/problems/split-array-largest-sum/
# 
# Given an integer array nums and an integer k, split nums into k non-empty 
# subarrays such that the largest sum of any subarray is minimized.
# 
# Return the minimized largest sum of the split.
# 
# A subarray is a contiguous part of the array.
# 
#  
# Example 1:
# 
# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
# 
# 
# Example 2:
# 
# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
# 
# 
# Constraints:
# 
# 	1 <= nums.length <= 1000
# 	0 <= nums[i] <= 106
# 	1 <= k <= min(50, nums.length)


# Solution: https://youtu.be/YUF3_eBdzsk
# Credit: Navdeep Singh founder of NeetCode
def split_array(nums, k):
    def canSplit(largest):
        subarray = 0
        curSum = 0
        for n in nums:
            curSum += n
            if curSum > largest:
                subarray += 1
                curSum = n
        return subarray + 1 <= k

    l, r = max(nums), sum(nums)
    res = r
    while l <= r:
        mid = l + ((r - l) // 2)
        if canSplit(mid):
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res


def main():
    result = split_array(nums = [7,2,5,10,8], k = 2)
    print(result) # 18

    result = split_array(nums = [1,2,3,4,5], k = 2)
    print(result) # 9

if __name__ == "__main__":
    main()
