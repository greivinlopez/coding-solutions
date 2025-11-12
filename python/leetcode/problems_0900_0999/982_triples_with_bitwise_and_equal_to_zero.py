# -------------------------------------------
# 982. Triples with Bitwise AND Equal To Zero
# -------------------------------------------

# Problem: https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero
#
# Given an integer array nums, return the number of AND triples.
# 
# An AND triple is a triple of indices (i, j, k) such that:
# 
#         0 <= i < nums.length
#         0 <= j < nums.length
#         0 <= k < nums.length
#         nums[i] & nums[j] & nums[k] == 0, where & represents the bitwise-AND operator.
# 
# Example 1:
# 
# Input: nums = [2,1,3]
# Output: 12
# 
# Explanation: We could choose the following i, j, k triples:
# (i=0, j=0, k=1) : 2 & 2 & 1
# (i=0, j=1, k=0) : 2 & 1 & 2
# (i=0, j=1, k=1) : 2 & 1 & 1
# (i=0, j=1, k=2) : 2 & 1 & 3
# (i=0, j=2, k=1) : 2 & 3 & 1
# (i=1, j=0, k=0) : 1 & 2 & 2
# (i=1, j=0, k=1) : 1 & 2 & 1
# (i=1, j=0, k=2) : 1 & 2 & 3
# (i=1, j=1, k=0) : 1 & 1 & 2
# (i=1, j=2, k=0) : 1 & 3 & 2
# (i=2, j=0, k=1) : 3 & 2 & 1
# (i=2, j=1, k=0) : 3 & 1 & 2
# 
# Example 2:
# 
# Input: nums = [0,0,0]
# Output: 27
# 
# 
# Constraints:
#         1 <= nums.length <= 1000
#         0 <= nums[i] < 2¹⁶

from collections import Counter

# Solution: https://algo.monster/liteproblems/982
# Credit: AlgoMonster
def count_triplets(nums):
    # Step 1: Pre-compute frequency of all possible bitwise AND results for pairs
    # For each pair (x, y) from nums, calculate x & y and count occurrences
    pair_and_frequency = Counter(x & y for x in nums for y in nums)
    
    # Step 2: Count valid triplets
    # For each pre-computed pair AND result and its frequency,
    # check against each number z in nums
    # If (x & y) & z == 0, then the triplet (x, y, z) has AND result of 0
    triplet_count = sum(
        frequency 
        for pair_and_result, frequency in pair_and_frequency.items() 
        for z in nums 
        if pair_and_result & z == 0
    )
    
    return triplet_count
    # Time: O(n² + n * m)
    # Space: O(m)
    # n = the length of the array nums
    # m = the maximum value in the array nums


def main():
    result = count_triplets(nums = [2,1,3])
    print(result) # 12

    result = count_triplets(nums = [0,0,0])
    print(result) # 27

if __name__ == "__main__":
    main()
