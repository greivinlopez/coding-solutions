# ----------------------------------------------
# 995. Minimum Number of K Consecutive Bit Flips
# ----------------------------------------------

# Problem: https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips
#
# You are given a binary array nums and an integer k.
# 
# A k-bit flip is choosing a subarray of length k from nums and simultaneously
# changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
# 
# Return the minimum number of k-bit flips required so that there is no 0 in the
# array. If it is not possible, return -1.
# 
# A subarray is a contiguous part of an array.
# 
# Example 1:
# 
# Input: nums = [0,1,0], k = 1
# Output: 2
# 
# Explanation: Flip nums[0], then flip nums[2].
# 
# Example 2:
# 
# Input: nums = [1,1,0], k = 2
# Output: -1
# 
# Explanation: No matter how we flip subarrays of size 2, we cannot make the array
# become [1,1,1].
# 
# Example 3:
# 
# Input: nums = [0,0,0,1,0,1,1,0], k = 3
# Output: 3
# 
# Explanation:
# Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
# Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
# Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]
# 
# 
# Constraints:
#         1 <= nums.length <= 10^5
#         1 <= k <= nums.length


# Solution: https://youtu.be/Fv3M9uO5ovU
# Credit: Navdeep Singh founder of NeetCode
def min_k_bit_flips(nums, k):
    cur_window_flips = 0
    res = 0
    for i in range(len(nums)):
        if i - k >= 0 and nums[i - k] == 2:
            cur_window_flips -= 1

        if (nums[i] + cur_window_flips) % 2 == 0:
            if i + k > len(nums):
                return -1
            res += 1
            cur_window_flips += 1
            nums[i] = 2
    return res
    # Time: O(n) 
    # Space: O(k) where k is the size of the queue


def main():
    result = min_k_bit_flips(nums = [0,1,0], k = 1)
    print(result) # 2

    result = min_k_bit_flips(nums = [1,1,0], k = 2)
    print(result) # -1

    result = min_k_bit_flips(nums = [0,0,0,1,0,1,1,0], k = 3)
    print(result) # 3

if __name__ == "__main__":
    main()
