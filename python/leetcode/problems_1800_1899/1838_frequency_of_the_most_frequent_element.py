# --------------------------------------------
# 1838. Frequency Of The Most Frequent Element
# --------------------------------------------

# Problem: https://leetcode.com/problems/frequency-of-the-most-frequent-element
#
# The frequency of an element is the number of times it occurs in an array.
# 
# You are given an integer array nums and an integer k. In one operation, you can
# choose an index of nums and increment the element at that index by 1.
# 
# Return the maximum possible frequency of an element after performing at most k
# operations.
# 
# Example 1:
# 
# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two
# times to make nums = [4,4,4].
# 4 has a frequency of 3.
# 
# Example 2:
# 
# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a
# frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a
# frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a
# frequency of 2.
# 
# Example 3:
# 
# Input: nums = [3,9,6], k = 2
# Output: 1
# 
# 
# Constraints:
#         1 <= nums.length <= 10^5
#         1 <= nums[i] <= 10^5
#         1 <= k <= 10^5


# Solution: https://youtu.be/vgBrQ0NM5vE
# Credit: Navdeep Singh founder of NeetCode
def max_frequency(nums, k):
    nums.sort()

    l, r = 0, 0
    res, total = 0, 0

    while r < len(nums):
        total += nums[r]
        while nums[r] * (r - l + 1) > total + k:
            total -= nums[l]
            l += 1
        res = max(res, r - l + 1)
        r += 1
    
    return res


def main():
    result = max_frequency(nums = [1,2,4], k = 5)
    print(result) # 3

    result = max_frequency(nums = [1,4,8,13], k = 5)
    print(result) # 2

    result = max_frequency(nums = [3,9,6], k = 2)
    print(result) # 1

if __name__ == "__main__":
    main()
