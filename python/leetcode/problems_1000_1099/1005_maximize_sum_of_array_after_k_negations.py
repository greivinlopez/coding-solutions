# --------------------------------------------
# 1005. Maximize Sum Of Array After K Negations
# --------------------------------------------

# Problem: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations
#
# Given an integer array nums and an integer k, modify the array in the following
# way:
#         
#   * choose an index i and replace nums[i] with -nums[i].
# 
# You should apply this process exactly k times. You may choose the same index i
# multiple times.
# 
# Return the largest possible sum of the array after modifying it in this way.
# 
# Example 1:
#
# Input: nums = [4,2,3], k = 1
# Output: 5
# 
# Explanation: Choose index 1 and nums becomes [4,-2,3].
# 
# Example 2:
# 
# Input: nums = [3,-1,0,2], k = 3
# Output: 6
# 
# Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
# 
# Example 3:
# 
# Input: nums = [2,-3,-1,5,-4], k = 2
# Output: 13
# 
# Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁴
#         -100 <= nums[i] <= 100
#         1 <= k <= 10⁴

from collections import Counter

# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def largest_sum_after_k_negations(nums, k):
    # Count frequency of each number in the array
    frequency_map = Counter(nums)
    
    # Process negative numbers from smallest to largest (-100 to -1)
    # Converting negatives to positives maximizes the sum
    for value in range(-100, 0):
        if frequency_map[value]:
            # Calculate how many times we can negate this value
            # Limited by either its frequency or remaining k
            negations_to_apply = min(frequency_map[value], k)
            
            # Update frequencies: reduce count of negative, increase count of positive
            frequency_map[value] -= negations_to_apply
            frequency_map[-value] += negations_to_apply
            
            # Decrease remaining negations
            k -= negations_to_apply
            
            # If we've used all negations, stop processing
            if k == 0:
                break
    
    # Handle remaining negations if k is odd and there's no zero in the array
    # If k is odd after negating all negatives, we must negate one more number
    # The optimal choice is the smallest positive number
    if k & 1 and frequency_map[0] == 0:
        # Find the smallest positive number to negate
        for value in range(1, 101):
            if frequency_map[value]:
                # Negate one instance of the smallest positive number
                frequency_map[value] -= 1
                frequency_map[-value] += 1
                break
    
    # Calculate the final sum by multiplying each value by its frequency
    return sum(value * frequency for value, frequency in frequency_map.items())
    # Time: O(n + m)
    # Space: O(m)
    # n = the length of the array nums
    # m = the size of the data range.


def main():
    result = largest_sum_after_k_negations(nums = [4,2,3], k = 1)
    print(result) # 5

    result = largest_sum_after_k_negations(nums = [3,-1,0,2], k = 3)
    print(result) # 6

    result = largest_sum_after_k_negations(nums = [2,-3,-1,5,-4], k = 2)
    print(result) # 13

if __name__ == "__main__":
    main()
