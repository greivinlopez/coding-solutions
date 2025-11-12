# -----------------------------------
# 334. Increasing Triplet Subsequence
# -----------------------------------

# Problem: https://leetcode.com/problems/increasing-triplet-subsequence/
# 
# Given an integer array nums, return true if there exists a triple of indices 
# (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such 
# indices exists, return false.
# 
#  
# Example 1:
# 
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# 
# 
# Example 2:
# 
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# 
# 
# Example 3:
# 
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
# 
# 
# Constraints:
# 
# 	1 <= nums.length <= 5 * 105
# 	-2^31 <= nums[i] <= 2^31 - 1
# 
# Follow up: Could you implement a solution that runs in O(n) time complexity 
# and O(1) space complexity?


# Solution: Video not found
# Credit: Navdeep Singh founder of NeetCode
def increasing_triplet(nums):
    first = float('inf')  # Initialize first to positive infinity
    second = float('inf')  # Initialize second to positive infinity
    
    for num in nums:
        if num <= first:
            first = num  # Update first if num is smaller or equal
        elif num <= second:
            second = num  # Update second if num is smaller or equal
        else:
            return True  # We found a triplet: first < second < num
    
    return False  # No triplet exists


def main():
    result = increasing_triplet([1,2,3,4,5])
    print(result) # True

    result = increasing_triplet([5,4,3,2,1])
    print(result) # False

    result = increasing_triplet([2,1,5,0,4,6])
    print(result) # True

if __name__ == "__main__":
    main()
