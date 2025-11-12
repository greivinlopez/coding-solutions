# ---------------------------------
# 1191. K-Concatenation Maximum Sum
# ---------------------------------

# Problem: https://leetcode.com/problems/k-concatenation-maximum-sum
#
# Given an integer array arr and an integer k, modify the array by repeating it k
# times.
# 
# For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1,
# 2, 1, 2].
# 
# Return the maximum sub-array sum in the modified array. Note that the length of
# the sub-array can be 0 and its sum in that case is 0.
# 
# As the answer can be very large, return the answer modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: arr = [1,2], k = 3
# Output: 9
# 
# Example 2:
# 
# Input: arr = [1,-2,1], k = 5
# Output: 2
# 
# Example 3:
# 
# Input: arr = [-1,-2], k = 7
# Output: 0
# 
# 
# Constraints:
#         1 <= arr.length <= 10⁵
#         1 <= k <= 10⁵
#         -10⁴ <= arr[i] <= 10⁴


# Solution: https://algo.monster/liteproblems/1191
# Credit: AlgoMonster
def k_concatenation_max_sum(arr, k):
    # Initialize variables for tracking sums and maximum values
    total_sum = 0  # Running sum of the array
    max_prefix_sum = 0  # Maximum prefix sum seen so far
    min_prefix_sum = 0  # Minimum prefix sum seen so far
    max_subarray_sum = 0  # Maximum subarray sum (Kadane's algorithm)
    
    # Single pass through the array to calculate all necessary values
    for num in arr:
        total_sum += num
        # Update maximum prefix sum
        max_prefix_sum = max(max_prefix_sum, total_sum)
        # Update minimum prefix sum
        min_prefix_sum = min(min_prefix_sum, total_sum)
        # Update maximum subarray sum using the formula: max_sum = current_sum - min_prefix
        max_subarray_sum = max(max_subarray_sum, total_sum - min_prefix_sum)
    
    # Start with the maximum subarray sum from a single array
    result = max_subarray_sum
    MOD = 10**9 + 7
    
    # If k = 1, return the maximum subarray sum from single array
    if k == 1:
        return result % MOD
    
    # Calculate maximum suffix sum (total_sum - minimum prefix sum)
    max_suffix_sum = total_sum - min_prefix_sum
    
    # For k >= 2, consider connecting suffix of first array with prefix of second array
    result = max(result, max_prefix_sum + max_suffix_sum)
    
    # If total array sum is positive, we can include (k-2) complete arrays in between
    if total_sum > 0:
        result = max(result, (k - 2) * total_sum + max_prefix_sum + max_suffix_sum)
    
    return result % MOD
    # Time: O(n)
    # Space: O(1)


def main():
    result = k_concatenation_max_sum(arr = [1,2], k = 3)
    print(result) # 9

    result = k_concatenation_max_sum(arr = [1,-2,1], k = 5)
    print(result) # 2

    result = k_concatenation_max_sum(arr = [-1,-2], k = 7)
    print(result) # 0

if __name__ == "__main__":
    main()
