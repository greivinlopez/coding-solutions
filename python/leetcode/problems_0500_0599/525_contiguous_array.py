# ---------------------
# 525. Contiguous Array
# ---------------------

# Problem: https://leetcode.com/problems/contiguous-array/
# 
# Given a binary array nums, return the maximum length of a contiguous subarray 
# with an equal number of 0 and 1.
# 
#  
# Example 1:
# 
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number 
# of 0 and 1.
# 
# 
# Example 2:
# 
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal 
# number of 0 and 1.
# 
# 
# Example 3:
# 
# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number 
# of 0 and 1.
# 
# 
# Constraints:
# 
# 	1 <= nums.length <= 10^5
# 	nums[i] is either 0 or 1.


# Solution: https://youtu.be/agB1LyObUNE
# Credit: Navdeep Singh founder of NeetCode
def find_max_length(nums):
    zero, one = 0, 0
    res = 0

    diff_index = {}

    for i, n in enumerate(nums):
        if n == 0:
            zero += 1
        else:
            one += 1
        if one - zero not in diff_index:
            diff_index[one - zero] = i
        
        if one == zero:
            res = one + zero
        else:
            idx = diff_index[one - zero]
            res = max(res, i - idx)
    return res


def main():
    result = find_max_length([0,1])
    print(result) # 2

    result = find_max_length([0,1,0])
    print(result) # 2

    result = find_max_length([0,1,1,1,1,1,0,0,0])
    print(result) # 6

if __name__ == "__main__":
    main()
