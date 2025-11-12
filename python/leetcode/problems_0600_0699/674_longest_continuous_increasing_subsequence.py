# ----------------------------------------------
# 674. Longest Continuous Increasing Subsequence
# ----------------------------------------------

# Problem: https://leetcode.com/problems/longest-continuous-increasing-subsequence
#
# Given an unsorted array of integers nums, return the length of the longest
# continuous increasing subsequence (i.e. subarray). The subsequence must be
# strictly increasing.
# 
# A continuous increasing subsequence is defined by two indices l and r (l < r)
# such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each 
# l <= i < r, nums[i] < nums[i + 1].
# 
# Example 1:
# 
# Input: nums = [1,3,5,4,7]
# Output: 3
# 
# Explanation: The longest continuous increasing subsequence is [1,3,5] with
# length 3.
# Even though [1,3,5,7] is an increasing subsequence, it is not continuous as
# elements 5 and 7 are separated by element
# 4.
# 
# Example 2:
# 
# Input: nums = [2,2,2,2,2]
# Output: 1
# 
# Explanation: The longest continuous increasing subsequence is [2] with length 1.
# Note that it must be strictly
# increasing.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁴
#         -10⁹ <= nums[i] <= 10⁹


# Solution: https://algo.monster/liteproblems/674
# Credit: AlgoMonster
def find_length_of_LCIS(nums):
    # Handle edge case of empty array
    if not nums:
        return 0
    
    # Initialize variables
    # max_length: tracks the maximum length of increasing subsequence found
    # current_length: tracks the length of current increasing subsequence
    max_length = 1
    current_length = 1
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Check if current element is greater than previous element
        if nums[i - 1] < nums[i]:
            # Extend the current increasing subsequence
            current_length += 1
            # Update maximum length if current sequence is longer
            max_length = max(max_length, current_length)
        else:
            # Reset current length when sequence breaks
            current_length = 1
    
    return max_length
    # Time: O(n)
    # Space: O(1)


def main():
    result = find_length_of_LCIS([1,3,5,4,7])
    print(result) # 3

    result = find_length_of_LCIS([2,2,2,2,2])
    print(result) # 1

if __name__ == "__main__":
    main()
