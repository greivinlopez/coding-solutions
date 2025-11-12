# -------------------------------------------------
# 1283. Find the Smallest Divisor Given a Threshold
# -------------------------------------------------

# Problem: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold
#
# Given an array of integers nums and an integer threshold, we will choose a
# positive integer divisor, divide all the array by it, and sum the division's
# result. Find the smallest divisor such that the result mentioned above is less
# than or equal to threshold.
# 
# Each result of the division is rounded to the nearest integer greater than or
# equal to that element. (For example: 7/3 = 3 and 10/2 = 5).
# 
# The test cases are generated so that there will be an answer.
# 
# Example 1:
# 
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# 
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the
# sum will be 5 (1+1+1+2).
# 
# Example 2:
# 
# Input: nums = [44,22,33,11,1], threshold = 5
# Output: 44
# 
# 
# Constraints:
#         1 <= nums.length <= 5 * 10⁴
#         1 <= nums[i] <= 10⁶
#         nums.length <= threshold <= 10⁶

from bisect import bisect_left

# Solution: https://algo.monster/liteproblems/1283
# Credit: AlgoMonster
def smallest_divisor(nums, threshold):
    def can_meet_threshold(divisor: int) -> bool:
        actual_divisor = divisor + 1
        # Calculate sum of ceiling divisions: ceil(x/d) = (x + d - 1) // d
        total_sum = sum((num + actual_divisor - 1) // actual_divisor for num in nums)
        return total_sum <= threshold
    
    # Binary search for the smallest divisor that meets the threshold
    # bisect_left finds the leftmost position where can_meet_threshold returns True
    # Search range is [0, max(nums)-1], representing divisors [1, max(nums)]
    smallest_index = bisect_left(range(max(nums)), True, key=can_meet_threshold)
    
    # Add 1 to convert from 0-indexed position to actual divisor value
    return smallest_index + 1
    # Time: O(n * log(m))
    # Space: O(1)
    # n = the number of elements in the nums list
    # m = the maximum value in the nums list (i.e., max(nums)).

# Solution: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/solutions/446358/python-binary-search-onlogm-mmaxarr-by-x-20md
# Credit: Rahul Bhati -> https://leetcode.com/u/xplorer/
def smallest_divisor_alt(nums, threshold):
    from math import ceil
    L, R = 1, max(nums) + 1
    def check(m):
        s = 0
        for x in nums:
            s += ceil(x/m)
        return s <= threshold
    
    while L < R:
        m = (L + R) // 2
        if check(m):
            ans = m
            R = m
        else:
            L = m + 1
    
    return ans
    # Time: O(n * log(m))
    # Space: O(1)
    # n = the number of elements in the nums list
    # m = the maximum value in the nums list (i.e., max(nums)).


def main():
    result = smallest_divisor(nums = [1,2,5,9], threshold = 6)
    print(result) # 5

    result = smallest_divisor(nums = [44,22,33,11,1], threshold = 5)
    print(result) # 44

if __name__ == "__main__":
    main()
