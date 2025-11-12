# -------------------------------
# 643. Maximum Average Subarray I
# -------------------------------

# Problem: https://leetcode.com/problems/maximum-average-subarray-i
#
# You are given an integer array nums consisting of n elements, and an integer k.
# 
# Find a contiguous subarray whose length is equal to k that has the maximum
# average value and return this value. Any answer with a calculation error less
# than 10-5 will be accepted.
# 
# Example 1:
# 
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# 
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# 
# Example 2:
# 
# Input: nums = [5], k = 1
# Output: 5.00000
# 
# 
# Constraints:
#         n == nums.length
#         1 <= k <= n <= 10⁵
#         -10⁴ <= nums[i] <= 10⁴


# Solution: https://youtu.be/UdUUnoiLkPg
# Credit: Greg Hogg
def find_max_average(nums, k):
    n = len(nums)
    cur_sum = 0

    for i in range(k):
        cur_sum += nums[i]

    max_avg = cur_sum / k

    for i in range(k, n):
        cur_sum += nums[i]
        cur_sum -= nums[i - k]

        avg = cur_sum / k
        max_avg = max(max_avg, avg)

    return max_avg
    # Time: O(n)
    # Space: O(1)


def main():
    result = find_max_average(nums = [1,12,-5,-6,50,3], k = 4)
    print(result) # 12.75

    result = find_max_average(nums = [5], k = 1)
    print(result) # 5.0

if __name__ == "__main__":
    main()
