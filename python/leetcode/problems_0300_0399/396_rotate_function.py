# --------------------
# 396. Rotate Function
# --------------------

# Problem: https://leetcode.com/problems/rotate-function
#
# You are given an integer array nums of length n.
# 
# Assume arrk to be an array obtained by rotating nums by k positions clock-wise.
# 
# We define the rotation function F on nums as follow:
# 
#         F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
# 
# Return the maximum value of F(0), F(1), ..., F(n-1).
# 
# The test cases are generated so that the answer fits in a 32-bit integer.
# 
# Example 1:
# 
# Input: nums = [4,3,2,6]
# Output: 26
# 
# Explanation:
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
# So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
# 
# Example 2:
# 
# Input: nums = [100]
# Output: 0
# 
# 
# Constraints:
#         n == nums.length
#         1 <= n <= 10⁵
#         -100 <= nums[i] <= 100


# Solution: https://leetcode.com/problems/rotate-function/solutions/857056/python-3-py3-8-math-o-n-explanation
# Credit: https://leetcode.com/u/idontknoooo/
def max_rotate_function(nums):
    s, n = sum(nums), len(nums)
    cur_sum = sum([i*j for i, j in enumerate(nums)])
    ans = cur_sum
    for i in range(n): ans = max(ans, cur_sum := cur_sum + s-nums[n-1-i]*n)
    return ans
    # Time: O(n)
    # Space: O(1)


def main():
    result = max_rotate_function(nums = [4,3,2,6])
    print(result) # 26

    result = max_rotate_function(nums = [100])
    print(result) # 0

if __name__ == "__main__":
    main()
