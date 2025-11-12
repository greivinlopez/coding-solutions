# ---------------------
# 137. Single Number II
# ---------------------

# Problem: https://leetcode.com/problems/single-number-ii
#
# Given an integer array nums where every element appears three times except for
# one, which appears exactly once. Find the single element and return it.
# 
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
# 
# Example 1:
# 
# Input: nums = [2,2,3,2]
# Output: 3
# 
# Example 2:
# 
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
# 
# 
# Constraints:
#         1 <= nums.length <= 3 * 10⁴
#         -2³¹ <= nums[i] <= 2³¹ - 1
#         Each element in nums appears exactly three times except for one element
# which appears once.


# Solution: https://leetcode.com/problems/single-number-ii/solutions/7058148/by-using-bitwise-not-operator
# Credit: Sandesh Yesane
def single_number(nums):
    single = double = 0
    for n in nums:
        single = (single ^ n) & ~double
        double = (double ^ n) & ~single
    return single
    # Time: O(n)
    # Space: O(1)


def main():
    result = single_number([2,2,3,2])
    print(result) # 3

    result = single_number([0,1,0,1,0,1,99])
    print(result) # 99

if __name__ == "__main__":
    main()
