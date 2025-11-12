# --------------------------------------
# 2149. Rearrange Array Elements by Sign
# --------------------------------------

# Problem: https://leetcode.com/problems/rearrange-array-elements-by-sign
#
# You are given a 0-indexed integer array nums of even length consisting of an
# equal number of positive and negative integers.
# 
# You should return the array of nums such that the the array follows the given
# conditions:
# 
# 1. Every consecutive pair of integers have opposite signs.
# 2. For all integers with the same sign, the order in which they were
#    present in nums is preserved.
# 3. The rearranged array begins with a positive integer.
# 
# Return the modified array after rearranging the elements to satisfy the
# aforementioned conditions.
# 
# Example 1:
# 
# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
# 
# Explanation:
# The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
# The only possible way to rearrange them such that they satisfy all conditions is
# [3,-2,1,-5,2,-4].
# Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are
# incorrect because they do not satisfy one or more conditions.
# 
# Example 2:
# 
# Input: nums = [-1,1]
# Output: [1,-1]
# 
# Explanation:
# 1 is the only positive integer and -1 the only negative integer in nums.
# So nums is rearranged to [1,-1].
# 
# Constraints:
#         2 <= nums.length <= 2 * 10^5
#         nums.length is even
#         1 <= |nums[i]| <= 10^5
#         nums consists of equal number of positive and negative integers.
# 
# It is not required to do the modifications in-place.


# Solution: https://youtu.be/SoPmcGzz9-E
# Credit: Navdeep Singh founder of NeetCode
def rearrange_array_first(nums):
    pos, neg = [], []
    for n in nums:
        if n > 0:
            pos.append(n)
        else:
            neg.append(n)

    i = 0
    while 2 * i < len(nums):
        nums[2 * i] = pos[i]
        nums[2 * i + 1] = neg[i]
        i += 1
        
    return nums
    # Time: O(n) 
    # Space: O(n)

# Better solution
def rearrange_array(nums):
    i, j = 0, 1
    res = [0] * len(nums)
    for k in range(len(nums)):
        if nums[k] > 0:
            res[i] = nums[k]
            i += 2
        else:
            res[j] = nums[k]
            j += 2
    return res
    # Time: O(n) 
    # Space: O(n)

def main():
    result = rearrange_array([3,1,-2,-5,2,-4])
    print(result) # [3,-2,1,-5,2,-4]

    result = rearrange_array([-1,1])
    print(result) # [1,-1]

if __name__ == "__main__":
    main()
