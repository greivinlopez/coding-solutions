# -----------------------------------------
# 1911. Maximum Alternating Subsequence Sum
# -----------------------------------------

# Problem: https://leetcode.com/problems/maximum-alternating-subsequence-sum
#
# The alternating sum of a 0-indexed array is defined as the sum of the elements
# at even indices minus the sum of the elements at odd indices.
#         
#   * For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
# 
# Given an array nums, return the maximum alternating sum of any subsequence of
# nums (after reindexing the elements of the subsequence).
# 
# A subsequence of an array is a new array generated from the original array by
# deleting some elements (possibly none) without changing the remaining elements'
# relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the
# underlined elements), while [2,4,2] is not.
# 
# Example 1:
# 
# Input: nums = [4,2,5,3]
# Output: 7
# 
# Explanation: It is optimal to choose the subsequence [4,2,5] with alternating
# sum (4 + 5) - 2 = 7.
# 
# Example 2:
# 
# Input: nums = [5,6,7,8]
# Output: 8
# 
# Explanation: It is optimal to choose the subsequence [8] with alternating sum 8.
# 
# Example 3:
# 
# Input: nums = [6,2,1,2,4,5]
# Output: 10
# 
# Explanation: It is optimal to choose the subsequence [6,1,5] with alternating
# sum (6 + 5) - 1 = 10.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         1 <= nums[i] <= 10⁵


# Solution: https://youtu.be/4v42XOuU1XA
# Credit: Navdeep Singh founder of NeetCode
def max_alternating_sum(nums):
    sumEven, sumOdd = 0, 0
    
    for i in range(len(nums) - 1, -1, -1):
        tmpEven = max(sumOdd + nums[i], sumEven)
        tmpOdd = max(sumEven - nums[i], sumOdd)
        sumEven, sumOdd = tmpEven, tmpOdd

    return sumEven
    # Time: O(n)
    # Space: O(1)


def main():
    result = max_alternating_sum([4,2,5,3])
    print(result) # 7

    result = max_alternating_sum([5,6,7,8])
    print(result) # 8

    result = max_alternating_sum([6,2,1,2,4,5])
    print(result) # 10

if __name__ == "__main__":
    main()
