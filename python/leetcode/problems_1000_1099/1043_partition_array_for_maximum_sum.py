# -------------------------------------
# 1043. Partition Array for Maximum Sum
# -------------------------------------

# Problem: https://leetcode.com/problems/partition-array-for-maximum-sum
#
# Given an integer array arr, partition the array into (contiguous) subarrays of
# length at most k. After partitioning, each subarray has their values changed to
# become the maximum value of that subarray.
# 
# Return the largest sum of the given array after partitioning. Test cases are
# generated so that the answer fits in a 32-bit integer.
# 
# Example 1:
# 
# Input: arr = [1,15,7,9,2,5,10], k = 3
# Output: 84
# 
# Explanation: arr becomes [15,15,15,9,10,10,10]
# 
# Example 2:
# 
# Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# Output: 83
# 
# Example 3:
# 
# Input: arr = [1], k = 1
# Output: 1
# 
# 
# Constraints:
#         1 <= arr.length <= 500
#         0 <= arr[i] <= 10^9
#         1 <= k <= arr.length


# Solution: https://youtu.be/kWhy4ZUBdOY
# Credit: Navdeep Singh founder of NeetCode
def max_sum_after_partitioning(arr, k):
    dp = [0] * k
    dp[0] = arr[0]

    for i in range(1, len(arr)):
        cur_max = 0
        max_at_i = 0
        for j in range(i, i - k, -1):
            if j < 0:
                break
            cur_max = max(cur_max, arr[j])
            window_size = i - j + 1
            cur_sum = cur_max * window_size
            sub_sum = dp[(j - 1) % k] if j > 0 else 0
            max_at_i = max(max_at_i, cur_sum + sub_sum)

        dp[i % k] = max_at_i
    return dp[(len(arr) - 1) % k]


def main():
    result = max_sum_after_partitioning(arr = [1,15,7,9,2,5,10], k = 3)
    print(result) # 84

    result = max_sum_after_partitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4)
    print(result) # 83

    result = max_sum_after_partitioning(arr = [1], k = 1)
    print(result) # 1

if __name__ == "__main__":
    main()
