# -------------------------------------------
# 945. Minimum Increment to Make Array Unique
# -------------------------------------------

# Problem: https://leetcode.com/problems/minimum-increment-to-make-array-unique
#
# You are given an integer array nums. In one move, you can pick an index i where
# 0 <= i < nums.length and increment nums[i] by 1.
# 
# Return the minimum number of moves to make every value in nums unique.
# 
# The test cases are generated so that the answer fits in a 32-bit integer.
# 
# Example 1:
# 
# Input: nums = [1,2,2]
# Output: 1
# 
# Explanation: After 1 move, the array could be [1, 2, 3].
# 
# Example 2:
# 
# Input: nums = [3,2,1,2,1,7]
# Output: 6
# 
# Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown that it is impossible for the array to have all unique values
# with 5 or less moves.
# 
# 
# Constraints:
#         1 <= nums.length <= 10^5
#         0 <= nums[i] <= 10^5


# Solution: https://youtu.be/XPPs2Wj2YSk
# Credit: Navdeep Singh founder of NeetCode
def min_increment_for_unique(nums):
    nums.sort()
    res = 0

    for i in range(1, len(nums)):
        if nums[i - 1] >= nums[i]:
            res += nums[i - 1] - nums[i] + 1
            nums[i] = nums[i - 1] + 1

    return res


def main():
    result = min_increment_for_unique([1,2,2])
    print(result) # 1

    result = min_increment_for_unique([3,2,1,2,1,7])
    print(result) # 6

if __name__ == "__main__":
    main()
