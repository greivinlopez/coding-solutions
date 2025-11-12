# ----------------------------------------------
# 659. Split Array into Consecutive Subsequences
# ----------------------------------------------

# Problem: https://leetcode.com/problems/split-array-into-consecutive-subsequences
#
# You are given an integer array nums that is sorted in non-decreasing order.
# 
# Determine if it is possible to split nums into one or more subsequences such
# that both of the following conditions are true:
#         
#   * Each subsequence is a consecutive increasing sequence (i.e. each integer
#     is exactly one more than the previous integer).
#   * All subsequences have a length of 3 or more.
# 
# Return true if you can split nums according to the above conditions, or false
# otherwise.
# 
# A subsequence of an array is a new array that is formed from the original array
# by deleting some (can be none) of the elements without disturbing the relative
# positions of the remaining elements. (i.e., [1,3,5] is a subsequence of
# [1,2,3,4,5] while [1,3,2] is not).
# 
# Example 1:
# 
# Input: nums = [1,2,3,3,4,5]
# Output: true
# 
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,5] --> 1, 2, 3
# [1,2,3,3,4,5] --> 3, 4, 5
# 
# Example 2:
# 
# Input: nums = [1,2,3,3,4,4,5,5]
# Output: true
# 
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
# [1,2,3,3,4,4,5,5] --> 3, 4, 5
# 
# Example 3:
# 
# Input: nums = [1,2,3,4,4,5]
# Output: false
# 
# Explanation: It is impossible to split nums into consecutive increasing
# subsequences of length 3 or more.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁴
#         -1000 <= nums[i] <= 1000
#         nums is sorted in non-decreasing order.

from collections import defaultdict
from heapq import heappush, heappop

# Solution: https://algo.monster/liteproblems/659
# Credit: AlgoMonster
def is_possible(nums):
    # Dictionary to store min-heaps of subsequence lengths ending at each number
    # Key: ending number of subsequence
    # Value: min-heap of lengths of subsequences ending at this number
    subsequence_lengths = defaultdict(list)
    
    # Process each number in the input array
    for current_num in nums:
        # Check if there's any subsequence ending at (current_num - 1)
        # that we can extend with current_num
        if subsequence_lengths[current_num - 1]:
            # Get the shortest subsequence ending at (current_num - 1)
            shortest_length = heappop(subsequence_lengths[current_num - 1])
            # Extend it by 1 and add to subsequences ending at current_num
            heappush(subsequence_lengths[current_num], shortest_length + 1)
        else:
            # No subsequence to extend, start a new subsequence of length 1
            heappush(subsequence_lengths[current_num], 1)
    
    # Check if all subsequences have length > 2 (at least 3 elements)
    for heap in subsequence_lengths.values():
        # If heap is empty, skip it
        if not heap:
            continue
        # If the shortest subsequence (heap[0]) has length <= 2, return False
        if heap[0] <= 2:
            return False
    
    return True
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = is_possible(nums = [1,2,3,3,4,5])
    print(result) # True

    result = is_possible(nums = [1,2,3,3,4,4,5,5])
    print(result) # True

    result = is_possible(nums = [1,2,3,4,4,5])
    print(result) # False

if __name__ == "__main__":
    main()
