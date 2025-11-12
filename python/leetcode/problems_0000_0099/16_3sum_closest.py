# -------------------
# 16. 3Sum Closest 3️⃣
# -------------------

# Problem: https://leetcode.com/problems/3sum-closest
#
# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.
# 
# Return the sum of the three integers.
# 
# You may assume that each input would have exactly one solution.
# 
# Example 1:
# 
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# 
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# Example 2:
# 
# Input: nums = [0,0,0], target = 1
# Output: 0
# 
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
# 
# 
# Constraints:
#         3 <= nums.length <= 500
#         -1000 <= nums[i] <= 1000
#         -10⁴ <= target <= 10⁴

# Solution: https://www.youtube.com/watch?v=PXWT4wzkA6M
# Credit: Navdeep Singh founder of NeetCode 
def three_sum_closest(nums, target):
    closest = float('inf')
    n = len(nums)
    nums.sort()

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i+1, n-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s == target:
                return s

            if abs(s - target) < abs(closest - target):
                closest = s

            if s < target:
                l += 1
            else:
                r -= 1
    return closest
    # Time: O(n²)
    # Space: O(n)     -> worst case scenario
    # Space: O(log n) -> average case
    # Space: O(1)     -> best case scenario

# Solution: https://youtu.be/PXWT4wzkA6M
# Credit: Greg Hogg
# Almost identical
def three_sum_closest_alt(nums, target):
    n = len(nums)
    nums.sort()
    closest_sum = float('inf')

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        lo, hi = i + 1, n - 1
        while lo < hi:
            cur_sum = nums[i] + nums[lo] + nums[hi]

            if abs(cur_sum - target) < abs(closest_sum - target):
                closest_sum = cur_sum

            if cur_sum == target:
                return cur_sum
            elif cur_sum < target:
                lo += 1
            else:
                hi -= 1

    return closest_sum
    # Time: O(n²)
    # Space: O(n)


def main():
    result = three_sum_closest(nums = [-1,2,1,-4], target = 1) # 2
    print(result)
    result = three_sum_closest(nums = [0,0,0], target = 1) # 0
    print(result)

if __name__ == "__main__":
    main()