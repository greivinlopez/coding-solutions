# -------------------------------------
# 719. Find K-th Smallest Pair Distance
# -------------------------------------

# Problem: https://leetcode.com/problems/find-k-th-smallest-pair-distance
#
# The distance of a pair of integers a and b is defined as the absolute difference
# between a and b.
# 
# Given an integer array nums and an integer k, return the kth smallest distance
# among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
# 
# Example 1:
# 
# Input: nums = [1,3,1], k = 1
# Output: 0
# 
# Explanation: Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# 
# Example 2:
# 
# Input: nums = [1,1,1], k = 2
# Output: 0
# 
# Example 3:
# 
# Input: nums = [1,6,1], k = 3
# Output: 5
# 
# 
# Constraints:
#         n == nums.length
#         2 <= n <= 10^4
#         0 <= nums[i] <= 10^6
#         1 <= k <= n * (n - 1) / 2


# Solution: https://youtu.be/bQ-QcFKwsZc
# Credit: Navdeep Singh founder of NeetCode
def smallest_distance_pair(nums, k):
    nums.sort()

    def helper(dist):
        # Count total num of pairs
        # with diff <= dist
        l = 0
        res = 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > dist:
                l += 1
            res += r - l
        return res

    l, r = 0, nums[-1] - nums[0]
    while l < r:
        m = l + ((r - l) // 2)
        pairs = helper(m)
        if pairs >= k:
            r = m
        else:
            l = m + 1
    return r
    # Time: O(N log N + N log W)    N = number of elements | W = max. distance
    # Space: O(1)


def main():
    result = smallest_distance_pair(nums = [1,3,1], k = 1)
    print(result) # 0

    result = smallest_distance_pair(nums = [1,1,1], k = 2)
    print(result) # 0

    result = smallest_distance_pair(nums = [1,6,1], k = 3)
    print(result) # 5

if __name__ == "__main__":
    main()
