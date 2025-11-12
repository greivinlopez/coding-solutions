# ---------------------------------------------------
# 1685. Sum of Absolute Differences in a Sorted Array
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array
#
# You are given an integer array nums sorted in non-decreasing order.
# 
# Build and return an integer array result with the same length as nums such that
# result[i] is equal to the summation of absolute differences between nums[i] and
# all the other elements in the array.
# 
# In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j <
# nums.length and j != i (0-indexed).
# 
# Example 1:
# 
# Input: nums = [2,3,5]
# Output: [4,3,5]
# 
# Explanation: Assuming the arrays are 0-indexed, then
# result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
# result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
# result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
# 
# Example 2:
# 
# Input: nums = [1,4,6,8,10]
# Output: [24,15,13,15,21]
# 
# 
# Constraints:
#         2 <= nums.length <= 10⁵
#         1 <= nums[i] <= nums[i + 1] <= 10⁴


# Solution: https://youtu.be/3nkc-e66JmA
# Credit: Navdeep Singh founder of NeetCode
def get_sum_absolute_differences(nums):
    total_sum = sum(nums)
    left_sum = 0
    res = []

    for i, n in enumerate(nums):
        right_sum = total_sum - n - left_sum
        
        left_size, right_size = i, len(nums) - i - 1
        res.append(
            left_size * n - left_sum +
            right_sum - right_size * n
        )
        
        left_sum += n

    return res
    # Time: O(n)
    # Space: O(1)


def main():
    result = get_sum_absolute_differences([2,3,5])
    print(result) # [4,3,5]

    result = get_sum_absolute_differences([1,4,6,8,10])
    print(result) # [24,15,13,15,21]

if __name__ == "__main__":
    main()
