# ---------------------------------------------------
# 1296. Divide Array in Sets of K Consecutive Numbers
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers
#
# Given an array of integers nums and a positive integer k, check whether it is
# possible to divide this array into sets of k consecutive numbers.
# 
# Return true if it is possible. Otherwise, return false.
# 
# Example 1:
# 
# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# Output: true
# 
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
# 
# Example 2:
# 
# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# 
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and
# [9,10,11].
# 
# Example 3:
# 
# Input: nums = [1,2,3,4], k = 3
# Output: false
# 
# Explanation: Each array should be divided in subarrays of size 3.
# 
# 
# Constraints:
#         1 <= k <= nums.length <= 10⁵
#         1 <= nums[i] <= 10⁹
# 
# Note: This question is the same as 846: 
# https://leetcode.com/problems/hand-of-straights/

from collections import Counter

# Solution: https://algo.monster/liteproblems/1296
# Credit: AlgoMonster
def is_possible_divide(nums, k):
    # Check if total number of elements is divisible by k
    # If not, we cannot form groups of size k
    if len(nums) % k != 0:
        return False
    
    # Count frequency of each number in the array
    frequency_map = Counter(nums)
    
    # Process numbers in ascending order
    for num in sorted(nums):
        # Skip if current number has already been used in previous groups
        if frequency_map[num] > 0:
            # Try to form a consecutive group starting from current number
            for consecutive_num in range(num, num + k):
                # Check if we have enough of the consecutive number
                if frequency_map[consecutive_num] == 0:
                    return False
                # Use one occurrence of this number for the current group
                frequency_map[consecutive_num] -= 1
    
    # All numbers have been successfully grouped
    return True
    # Time: O(n * log(n) + n * k)
    # Space: O(n)


def main():
    result = is_possible_divide(nums = [1,2,3,3,4,4,5,6], k = 4)
    print(result) # True

    result = is_possible_divide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3)
    print(result) # True

    result = is_possible_divide(nums = [1,2,3,4], k = 3)
    print(result) # False

if __name__ == "__main__":
    main()
