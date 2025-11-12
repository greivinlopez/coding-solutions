# -------------------------------
# 996. Number of Squareful Arrays
# -------------------------------

# Problem: https://leetcode.com/problems/number-of-squareful-arrays
#
# An array is squareful if the sum of every pair of adjacent elements is a perfect
# square.
# 
# Given an integer array nums, return the number of permutations of nums that are
# squareful.
# 
# Two permutations perm1 and perm2 are different if there is some index i such
# that perm1[i] != perm2[i].
# 
# Example 1:
# 
# Input: nums = [1,17,8]
# Output: 2
# 
# Explanation: [1,8,17] and [17,8,1] are the valid permutations.
# 
# Example 2:
# 
# Input: nums = [2,2,2]
# Output: 1
# 
# 
# Constraints:
#         1 <= nums.length <= 12
#         0 <= nums[i] <= 10⁹

from collections import Counter
from math import sqrt, factorial

# Solution: https://algo.monster/liteproblems/996
# Credit: AlgoMonster
def num_squareful_perms(nums):
    n = len(nums)
    
    # dp[mask][last_idx] = number of ways to arrange numbers in 'mask' ending at index 'last_idx'
    # mask: bitmask representing which indices have been used (1 = used, 0 = unused)
    # last_idx: the index of the last number in the current arrangement
    dp = [[0] * n for _ in range(1 << n)]
    
    # Base case: single element arrangements
    # Each number by itself is a valid arrangement of length 1
    for idx in range(n):
        dp[1 << idx][idx] = 1
    
    # Iterate through all possible subsets of indices (represented by bitmask)
    for mask in range(1 << n):
        # Try each possible last element in the current arrangement
        for last_idx in range(n):
            # Check if last_idx is included in the current mask
            if mask >> last_idx & 1:
                # Try to extend from each possible previous element
                for prev_idx in range(n):
                    # Check if prev_idx is in mask and is different from last_idx
                    if (mask >> prev_idx & 1) and prev_idx != last_idx:
                        # Check if the sum of the two adjacent numbers is a perfect square
                        sum_value = nums[last_idx] + nums[prev_idx]
                        sqrt_value = int(sqrt(sum_value))
                        
                        if sqrt_value * sqrt_value == sum_value:
                            # If valid, add the number of ways to reach prev_idx
                            # in the state without last_idx
                            prev_mask = mask ^ (1 << last_idx)
                            dp[mask][last_idx] += dp[prev_mask][prev_idx]
    
    # Sum up all valid complete arrangements (using all numbers)
    full_mask = (1 << n) - 1  # All bits set to 1
    total_arrangements = sum(dp[full_mask][last_idx] for last_idx in range(n))
    
    # Adjust for duplicate numbers by dividing by factorial of their frequencies
    # This removes overcounting due to identical elements being treated as distinct
    frequency_map = Counter(nums)
    for frequency in frequency_map.values():
        total_arrangements //= factorial(frequency)
    
    return total_arrangements
    # Time: O(2ⁿ * n²)
    # Space: O(2ⁿ * n)


def main():
    result = num_squareful_perms([1,17,8])
    print(result) # 2

    result = num_squareful_perms([2,2,2])
    print(result) # 1

if __name__ == "__main__":
    main()
