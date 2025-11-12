# -------------------------------------
# 2348. Number Of Zero Filled Subarrays
# -------------------------------------

# Problem: https://leetcode.com/problems/number-of-zero-filled-subarrays
#
# Given an integer array nums, return the number of subarrays filled with 0.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
# Example 1:
# 
# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation:
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0.
# Therefore, we return 6.
# 
# Example 2:
# 
# Input: nums = [0,0,0,2,0,0]
# Output: 9
# Explanation:
# There are 5 occurrences of [0] as a subarray.
# There are 3 occurrences of [0,0] as a subarray.
# There is 1 occurrence of [0,0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 3 filled with 0.
# Therefore, we return 9.
# 
# Example 3:
# 
# Input: nums = [2,10,2019]
# Output: 0
# Explanation: There is no subarray filled with 0. Therefore, we return 0.
# 
# 
# Constraints:
#         1 <= nums.length <= 10^5
#         -10^9 <= nums[i] <= 10^9


# Solution: https://youtu.be/G-EWVGCcL_w
# Credit: Navdeep Singh founder of NeetCode
def zero_filled_subarray(nums):
    # check if there are any Zeros in the list
    res = nums.count(0)
    if res == 0:
        return 0
            
    r = 0
    l = len(nums)
    while r < l:
        Temp_Subarray=[]
        while r < l and nums[r] == 0:
            Temp_Subarray.append(nums[r])
            r += 1
        if len(Temp_Subarray) > 1:
            Temp_Count =  len(Temp_Subarray) * ( len(Temp_Subarray) - 1 ) / 2 
            res += int(Temp_Count)

        r += 1
    return res


def main():
    result = zero_filled_subarray([1,3,0,0,2,0,0,4])
    print(result) # 6

    result = zero_filled_subarray([0,0,0,2,0,0])
    print(result) # 9

    result = zero_filled_subarray([2,10,2019])
    print(result) # 0

if __name__ == "__main__":
    main()
