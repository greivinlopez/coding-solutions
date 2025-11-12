# ------------------------------------
# 1248. Count Number of Nice Subarrays
# ------------------------------------

# Problem: https://leetcode.com/problems/count-number-of-nice-subarrays
#
# Given an array of integers nums and an integer k. A continuous subarray is
# called nice if there are k odd numbers on it.
# 
# Return the number of nice sub-arrays.
# 
# Example 1:
# 
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# 
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# 
# Example 2:
# 
# Input: nums = [2,4,6], k = 1
# Output: 0
# 
# Explanation: There are no odd numbers in the array.
# 
# Example 3:
# 
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
# 
# 
# Constraints:
#         1 <= nums.length <= 50000
#         1 <= nums[i] <= 10^5
#         1 <= k <= nums.length


# Solution: https://youtu.be/4zNK0rhFfcA
# Credit: Navdeep Singh founder of NeetCode
def number_of_subarrays(nums, k):
    res, odd = 0, 0
    l, m = 0, 0
    for r in range(len(nums)):
        if nums[r] % 2:
            odd += 1

        while odd > k:
            if nums[l] % 2:
                odd -= 1
            l += 1
            m = l

        if odd == k:
            while not nums[m] % 2:
                m += 1
            res += (m - l) + 1

    return res
    # Time: O(n)
    # Space: O(1)

def main():
    result = number_of_subarrays(nums = [1,1,2,1,1], k = 3)
    print(result) # 2

    result = number_of_subarrays(nums = [2,4,6], k = 1)
    print(result) # 0

    result = number_of_subarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2)
    print(result) # 16

if __name__ == "__main__":
    main()
