# -------------------------------
# 1679. Max Number of K-Sum Pairs
# -------------------------------

# Problem: https://leetcode.com/problems/max-number-of-k-sum-pairs
#
# You are given an integer array nums and an integer k.
# 
# In one operation, you can pick two numbers from the array whose sum equals k and
# remove them from the array.
# 
# Return the maximum number of operations you can perform on the array.
# 
# Example 1:
# 
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# 
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# 
# Example 2:
# 
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# 
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         1 <= nums[i] <= 10⁹
#         1 <= k <= 10⁹


# Solution: https://algo.monster/liteproblems/1679
# Credit: AlgoMonster
def max_operations(nums, k):
    # Sort the array to enable two-pointer approach
    nums.sort()
    
    # Initialize two pointers at the start and end of the array
    left = 0
    right = len(nums) - 1
    
    # Counter for the number of valid operations
    operation_count = 0
    
    # Use two-pointer technique to find pairs that sum to k
    while left < right:
        # Calculate the sum of elements at current pointers
        current_sum = nums[left] + nums[right]
        
        if current_sum == k:
            # Found a valid pair, increment count and move both pointers inward
            operation_count += 1
            left += 1
            right -= 1
        elif current_sum > k:
            # Sum is too large, move right pointer left to decrease sum
            right -= 1
        else:
            # Sum is too small, move left pointer right to increase sum
            left += 1
    
    return operation_count
    # Time: O(n * log n)
    # Space: O(log n)


def main():
    result = max_operations(nums = [1,2,3,4], k = 5)
    print(result) # 2

    result = max_operations(nums = [3,1,3,4,3], k = 6)
    print(result) # 1

if __name__ == "__main__":
    main()
