# ----------------------------------------
# 718. Maximum Length of Repeated Subarray
# ----------------------------------------

# Problem: https://leetcode.com/problems/maximum-length-of-repeated-subarray
#
# Given two integer arrays nums1 and nums2, return the maximum length of a
# subarray that appears in both arrays.
# 
# Example 1:
# 
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# 
# Explanation: The repeated subarray with maximum length is [3,2,1].
# 
# Example 2:
# 
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
# 
# Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
# 
# 
# Constraints:
#         1 <= nums1.length, nums2.length <= 1000
#         0 <= nums1[i], nums2[i] <= 100


# Solution: https://algo.monster/liteproblems/718
# Credit: AlgoMonster
def find_length(nums1, nums2):
    # Get the lengths of both arrays
    len1, len2 = len(nums1), len(nums2)
    
    # Initialize DP table with dimensions (len1+1) x (len2+1)
    # dp[i][j] stores length of common subarray ending at nums1[i-1] and nums2[j-1]
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    # Track the maximum length found
    max_length = 0
    
    # Iterate through all positions in both arrays
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            # If elements match, extend the common subarray from previous diagonal
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
            # If elements don't match, common subarray length is 0 (implicit due to initialization)
    
    return max_length
    # Time: O(m * n)
    # Space: O(m * n)


def main():
    result = find_length(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7])
    print(result) # 3

    result = find_length(nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0])
    print(result) # 5

if __name__ == "__main__":
    main()
