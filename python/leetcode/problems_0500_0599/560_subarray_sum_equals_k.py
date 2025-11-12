# -----------------------------
# 560. Subarray Sum Equals K ➕
# -----------------------------

# Problem: https://leetcode.com/problems/subarray-sum-equals-k/
# 
# Given an array of integers nums and an integer k, return the total number of 
# subarrays whose sum equals to k.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
#  
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# 
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# 
#  
# Constraints:
# 
# 	1 <= nums.length <= 2 * 10^4
# 	-1000 <= nums[i] <= 1000
# 	-10^7 <= k <= 10^7


# Solution: https://youtu.be/fFVZt-6sgyo
# Credit: Navdeep Singh founder of NeetCode
def sub_sum_k(nums, k):
    res = cur_sum = 0
    prefix = { 0: 1 }

    for n in nums:
        cur_sum += n
        diff = cur_sum - k
        res += prefix.get(diff, 0)
        prefix[cur_sum] = 1 + prefix.get(cur_sum, 0)
    return res


def main():
    result = sub_sum_k(nums = [1,1,1], k = 2)
    print(result) # 2

    result = sub_sum_k(nums = [1,2,3], k = 3)
    print(result) # 2

if __name__ == "__main__":
    main()
