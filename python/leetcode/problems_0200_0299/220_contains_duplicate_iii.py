# ---------------------------
# 220. Contains Duplicate III
# ---------------------------

# Problem: https://leetcode.com/problems/contains-duplicate-iii
#
# You are given an integer array nums and two integers indexDiff and valueDiff.
# 
# Find a pair of indices (i, j) such that:
#         i != j,
#         abs(i - j) <= indexDiff.
#         abs(nums[i] - nums[j]) <= valueDiff, and
# 
# Return true if such pair exists or false otherwise.
# 
# Example 1:
# 
# Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
# Output: true
# 
# Explanation: We can choose (i, j) = (0, 3).
# We satisfy the three conditions:
# i != j --> 0 != 3
# abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
# abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
# 
# Example 2:
# 
# Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
# Output: false
# 
# Explanation: After trying all the possible pairs (i, j), we cannot satisfy the
# three conditions, so we return false.
# 
# 
# Constraints:
#         2 <= nums.length <= 10⁵
#         -10⁹ <= nums[i] <= 10⁹
#         1 <= indexDiff <= nums.length
#         0 <= valueDiff <= 10⁹

from collections import OrderedDict

# Solution: https://leetcode.com/problems/contains-duplicate-iii/solutions/829231/python3-easy-to-understand-o-n-solution-contains-duplicate-iii
# Credit: Robert Zhang -> https://leetcode.com/u/r0bertz/
def contains_nearby_almost_duplicate(nums, k, t):
    d = OrderedDict()
    window = t + 1
    for i, n in enumerate(nums):
        while len(d) > k:
            d.popitem(last=False)
        if (b := n//window) in d:
            return True 
        if b - 1 in d and abs(d[b-1] - n) <= t:
            return True
        if b + 1 in d and abs(d[b+1] - n) <= t:
            return True
        d[b] = nums[i]  
    return False
    # Time: O(n)
    # Space: O(min(n, k))
    # n = the length of nums


def main():
    result = contains_nearby_almost_duplicate([1,2,3,1], 3, 0)
    print(result) # True

    result = contains_nearby_almost_duplicate([1,5,9,1,5,9], 2, 3)
    print(result) # False

if __name__ == "__main__":
    main()
