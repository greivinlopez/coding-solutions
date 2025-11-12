# ---------------------------------------
# 2444. Count Subarrays With Fixed Bounds
# ---------------------------------------

# Problem: https://leetcode.com/problems/count-subarrays-with-fixed-bounds
#
# You are given an integer array nums and two integers minK and maxK.
# 
# A fixed-bound subarray of nums is a subarray that satisfies the following
# conditions:
# 
#         The minimum value in the subarray is equal to minK.
#         The maximum value in the subarray is equal to maxK.
# 
# Return the number of fixed-bound subarrays.
# 
# A subarray is a contiguous part of an array.
# 
# Example 1:
# 
# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# 
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
# 
# Example 2:
# 
# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# 
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10
# possible subarrays.
# 
# 
# Constraints:
#         2 <= nums.length <= 10⁵
#         1 <= nums[i], minK, maxK <= 10⁶


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def count_subarrays(nums, minK, maxK):
    res = 0
    bad_idx = left_idx = right_idx = -1

    for i, num in enumerate(nums) :
        if not minK <= num <= maxK:
            bad_idx = i

        if num == minK:
            left_idx = i

        if num == maxK:
            right_idx = i

        res += max(0, min(left_idx, right_idx) - bad_idx)

    return res
    # Time: O(n)
    # Space: O(1)


def main():
    result = count_subarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5)
    print(result) # 2

    result = count_subarrays(nums = [1,1,1,1], minK = 1, maxK = 1)
    print(result) # 10

if __name__ == "__main__":
    main()
