# ----------------------------------
# 1814. Count Nice Pairs in an Array
# ----------------------------------

# Problem: https://leetcode.com/problems/count-nice-pairs-in-an-array
#
# You are given an array nums that consists of non-negative integers. Let us
# define rev(x) as the reverse of the non-negative integer x. For example,
# rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it
# satisfies all of the following conditions:
#
#   0 <= i < j < nums.length
#   nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# 
# Return the number of nice pairs of indices. Since that number can be too large,
# return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: nums = [42,11,1,97]
# Output: 2
# 
# Explanation: The two pairs are:
#  - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
#  - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
# 
# Example 2:
# 
# Input: nums = [13,10,35,24,76]
# Output: 4
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         0 <= nums[i] <= 10⁹

from collections import defaultdict

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def count_nice_pairs(nums):
    def rev(num):
        result = 0
        while num:
            result = result * 10 + num % 10
            num //= 10
        
        return result

    arr = []
    for i in range(len(nums)):
        arr.append(nums[i] - rev(nums[i]))
    
    dic = defaultdict(int)
    ans = 0
    MOD = 10 ** 9 + 7
    for num in arr:
        ans = (ans + dic[num]) % MOD
        dic[num] += 1
    
    return ans
    # Time: O(n * d)
    # Space: O(n)
    # n = length of the input list
    # d = maximum number of digis in any number in the input list


def main():
    result = count_nice_pairs([42,11,1,97])
    print(result) # 2

    result = count_nice_pairs([13,10,35,24,76])
    print(result) # 4

if __name__ == "__main__":
    main()
