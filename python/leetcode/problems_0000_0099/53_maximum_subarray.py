# ---------------------
# 53. Maximum Subarray
# ---------------------

# Problem: https://leetcode.com/problems/maximum-subarray/
# 
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Solution: https://youtu.be/5WZl3MMT0Eg
# Credit: Navdeep Singh founder of NeetCode 
def max_sub_array(nums):
    # Time: O(n)
    # Space: O(1)
    res = nums[0]

    total = 0
    for n in nums:
        total += n
        res = max(res, total)
        if total < 0:
            total = 0
    return res

# Solution: https://youtu.be/hLPkqd60-28
# Credit: Greg Hogg
# Almost identical
def max_sub_array_alt(nums):
    # Bottom Up DP (Constant Space)
    # Time: O(n)
    # Space: O(1)
    max_sum = float('-inf')
    curr_sum = 0
    
    for i in range(len(nums)):
        curr_sum += nums[i]
        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0
    
    return max_sum


def main():
    result = max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) # 6
    print(result)
    result = max_sub_array([1]) # 1
    print(result)
    result = max_sub_array([5,4,-1,7,8]) # 23
    print(result)

if __name__ == "__main__":
    main()