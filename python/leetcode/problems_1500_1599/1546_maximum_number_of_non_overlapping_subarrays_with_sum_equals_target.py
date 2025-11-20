# ------------------------------------------------------------------------
# 1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
# ------------------------------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target
#
# Given an array nums and an integer target, return the maximum number of non-
# empty non-overlapping subarrays such that the sum of values in each subarray is
# equal to target.
# 
# Example 1:
# 
# Input: nums = [1,1,1,1,1], target = 2
# Output: 2
# 
# Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals
# to target(2).
# 
# Example 2:
# 
# Input: nums = [-1,3,5,1,4,2,-9], target = 6
# Output: 2
# 
# Explanation: There are 3 subarrays with sum equal to 6.
# ([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         -10⁴ <= nums[i] <= 10⁴
#         0 <= target <= 10⁶


# Solution: https://algo.monster/liteproblems/1546
# Credit: AlgoMonster
def max_non_overlapping(nums, target):
    result = 0  # Count of non-overlapping subarrays found
    index = 0
    length = len(nums)
    
    # Iterate through the array to find non-overlapping subarrays
    while index < length:
        current_sum = 0
        # Set to store prefix sums seen so far in current window
        # Initialize with 0 to handle cases where subarray starts from current position
        seen_prefix_sums = {0}
        
        # Try to find a subarray starting from current position
        while index < length:
            current_sum += nums[index]
            
            # Check if there exists a prefix sum such that
            # current_sum - prefix_sum = target
            # This means we found a subarray with sum equal to target
            if current_sum - target in seen_prefix_sums:
                result += 1
                break  # Move to next non-overlapping position
            
            index += 1
            seen_prefix_sums.add(current_sum)
        
        # Move to the next position after the found subarray
        index += 1
    
    return result
    # Time: O(n)
    # Space: O(n)


def main():
    result = max_non_overlapping(nums = [1,1,1,1,1], target = 2)
    print(result) # True

    result = max_non_overlapping(nums = [-1,3,5,1,4,2,-9], target = 6)
    print(result) # True

if __name__ == "__main__":
    main()
