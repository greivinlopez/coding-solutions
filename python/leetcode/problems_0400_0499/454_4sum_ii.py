# ------------
# 454. 4Sum II
# ------------

# Problem: https://leetcode.com/problems/4sum-ii
#
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return
# the number of tuples (i, j, k, l) such that:
# 
#         0 <= i, j, k, l < n
#         nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
# 
# Example 1:
# 
# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# 
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) +
# 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) +
# 0 = 0
# 
# Example 2:
# 
# Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# Output: 1
# 
# 
# Constraints:
#         n == nums1.length
#         n == nums2.length
#         n == nums3.length
#         n == nums4.length
#         1 <= n <= 200
#         -2²⁸ <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2²⁸

from collections import Counter

# Solution: https://algo.monster/liteproblems/454
# Credit: AlgoMonster
def four_sum_count(nums1, nums2, nums3, nums4):
    # Create a hash map to store the frequency of all possible sums from nums1 and nums2
    # Key: sum of a pair (a, b) where a is from nums1 and b is from nums2
    # Value: frequency of this sum
    sum_count = Counter(a + b for a in nums1 for b in nums2)
    
    # For each pair (c, d) from nums3 and nums4, check if -(c + d) exists in the hash map
    # If it exists, add its frequency to the result
    # This works because we need a + b + c + d = 0, which means a + b = -(c + d)
    result = sum(sum_count[-(c + d)] for c in nums3 for d in nums4)
    
    return result
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = four_sum_count(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2])
    print(result) # 2

    result = four_sum_count(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0])
    print(result) # 1

if __name__ == "__main__":
    main()
