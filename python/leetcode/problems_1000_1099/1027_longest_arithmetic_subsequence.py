# ------------------------------------
# 1027. Longest Arithmetic Subsequence
# ------------------------------------

# Problem: https://leetcode.com/problems/longest-arithmetic-subsequence
#
# Given an array nums of integers, return the length of the longest arithmetic
# subsequence in nums.
# 
# Note that:
#         
#   * A subsequence is an array that can be derived from another array by
#     deleting some or no elements without changing the order of the remaining
#     elements.
#   * A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same
#     value (for 0 <= i < seq.length - 1).
# 
# Example 1:
# 
# Input: nums = [3,6,9,12]
# Output: 4
# 
# Explanation:  The whole array is an arithmetic sequence with steps of length =
# 3.
# 
# Example 2:
# 
# Input: nums = [9,4,7,2,10]
# Output: 3
# 
# Explanation:  The longest arithmetic subsequence is [4,7,10].
# 
# Example 3:
# 
# Input: nums = [20,1,15,3,10,5,8]
# Output: 4
# 
# Explanation:  The longest arithmetic subsequence is [20,15,10,5].
# 
# 
# Constraints:
#         2 <= nums.length <= 1000
#         0 <= nums[i] <= 500


# Solution: https://algo.monster/liteproblems/1027
# Credit: AlgoMonster
def longest_arith_seq_length(nums):
    n = len(nums)
    
    # dp[i][diff] represents the length of the longest arithmetic subsequence
    # ending at index i with common difference 'diff'
    # Since difference can range from -500 to 500 (based on constraints),
    # we offset by 500 to avoid negative indices (0 to 1000)
    dp = [[1] * 1001 for _ in range(n)]
    
    max_length = 0
    
    # For each position i, check all previous positions
    for i in range(1, n):
        for prev_idx in range(i):
            # Calculate the difference between current and previous element
            # Add 500 offset to handle negative differences as array indices
            diff_with_offset = nums[i] - nums[prev_idx] + 500
            
            # Extend the arithmetic subsequence ending at prev_idx
            # with the same difference to include nums[i]
            dp[i][diff_with_offset] = max(
                dp[i][diff_with_offset], 
                dp[prev_idx][diff_with_offset] + 1
            )
            
            # Update the maximum length found so far
            max_length = max(max_length, dp[i][diff_with_offset])
    
    return max_length
    # Time: O(n²)
    # Space: O(n * d)
    # d = the range of possible differences.


def main():
    result = longest_arith_seq_length(nums = [3,6,9,12])
    print(result) # 4

    result = longest_arith_seq_length(nums = [9,4,7,2,10])
    print(result) # 3

    result = longest_arith_seq_length(nums = [20,1,15,3,10,5,8])
    print(result) # 4

if __name__ == "__main__":
    main()
