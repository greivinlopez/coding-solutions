# -----------------------------------------------
# 2419. Longest Subarray With Maximum Bitwise AND
# -----------------------------------------------

# Problem: https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and
#
# You are given an integer array nums of size n.
# 
# Consider a non-empty subarray from nums that has the maximum possible bitwise
# AND.
#         
#   * In other words, let k be the maximum value of the bitwise AND of any
#     subarray of nums. Then, only subarrays with a bitwise AND equal to k should be
#     considered.
# 
# Return the length of the longest such subarray.
# 
# The bitwise AND of an array is the bitwise AND of all the numbers in it.
# 
# A subarray is a contiguous sequence of elements within an array.
# 
# Example 1:
# 
# Input: nums = [1,2,3,3,2,2]
# Output: 2
# 
# Explanation:
# The maximum possible bitwise AND of a subarray is 3.
# The longest subarray with that value is [3,3], so we return 2.
# 
# Example 2:
# 
# Input: nums = [1,2,3,4]
# Output: 1
# 
# Explanation:
# The maximum possible bitwise AND of a subarray is 4.
# The longest subarray with that value is [4], so we return 1.
# 
# 
# Constraints:
#         1 <= nums.length <= 10^5
#         1 <= nums[i] <= 10^6


# Solution: https://youtu.be/N8lRlRWA_1Q
# Credit: Navdeep Singh founder of NeetCode
def longest_subarray(nums):
    size, res = 0, 0
    cur_max = 0
    for n in nums:
        if n > cur_max:
            cur_max = n
            size = 1
            res = 0
        elif n == cur_max:
            size += 1
        else:
            size = 0
        res = max(res, size)
    return res
    # Time = O(n)
    # Space = O(1)


def main():
    result = longest_subarray([1,2,3,3,2,2])
    print(result) # 2

    result = longest_subarray([1,2,3,4])
    print(result) # 1

if __name__ == "__main__":
    main()
