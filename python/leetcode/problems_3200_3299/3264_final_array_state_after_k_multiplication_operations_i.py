# -----------------------------------------------------------
# 3264. Final Array State After K Multiplication Operations I
# -----------------------------------------------------------

# Problem: https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i
#
# You are given an integer array nums, an integer k, and an integer multiplier.
# 
# You need to perform k operations on nums. In each operation:
#         
#   * Find the minimum value x in nums. If there are multiple occurrences of
#     the minimum value, select the one that appears first.
#   * Replace the selected minimum value x with x * multiplier.
# 
# Return an integer array denoting the final state of nums after performing all k
# operations.
# 
# Example 1:
# 
# Input: nums = [2,1,3,5,6], k = 5, multiplier = 2
# Output: [8,4,6,5,6]
# 
# Explanation:
#       +-------------------+--------------------+
#       | Operation         | Result             |
#       +-------------------+--------------------+
#       | After operation 1 | [2, 2, 3, 5, 6]    |
#       | After operation 2 | [4, 2, 3, 5, 6]    |
#       | After operation 3 | [4, 4, 3, 5, 6]    |
#       | After operation 4 | [4, 4, 6, 5, 6]    |
#       | After operation 5 | [8, 4, 6, 5, 6]    |
#       +-------------------+--------------------+

# Example 2:
# 
# Input: nums = [1,2], k = 3, multiplier = 4
# Output: [16,8]
# 
# Explanation:
#       +-------------------+-----------+
#       | Operation         | Result    |
#       +-------------------+-----------+
#       | After operation 1 | [4, 2]    |
#       | After operation 2 | [4, 8]    |
#       | After operation 3 | [16, 8]   |
#       +-------------------+-----------+
# 
# Constraints:
#         1 <= nums.length <= 100
#         1 <= nums[i] <= 100
#         1 <= k <= 10
#         1 <= multiplier <= 5

import heapq

# Solution: https://youtu.be/AaoytRXBXGs
# Credit: Navdeep Singh founder of NeetCode
def get_final_state(nums, k, multiplier):
    res = nums[::]

    min_heap = [(n, i) for i, n in enumerate(nums)]
    heapq.heapify(min_heap)

    for _ in range(k):
        n, i = heapq.heappop(min_heap)
        res[i] *= multiplier
        heapq.heappush(min_heap, (res[i], i))
    
    return res
    # Time: O(k * log(n))

def main():
    result = get_final_state(nums = [2,1,3,5,6], k = 5, multiplier = 2)
    print(result) # [8,4,6,5,6]

    result = get_final_state(nums = [1,2], k = 3, multiplier = 4)
    print(result) # [16,8]

if __name__ == "__main__":
    main()
