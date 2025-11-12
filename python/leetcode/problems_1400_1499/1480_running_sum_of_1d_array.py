# ---------------------------------------------------------------------
# 1489. Find Critical And Pseudo Critical Edges In Minimum Spanning Tree
# ---------------------------------------------------------------------

# Problem: https://leetcode.com/problems/running-sum-of-1d-array/
#
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# 
# Return the running sum of nums.
# 
#  
# Example 1:
# 
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# 
# Example 2:
# 
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# 
# Example 3:
# 
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
#  
# 
# Constraints:
# 
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6


# Solution: No video found
# Credit: Greg Hogg
def running_sum(nums):
    s = 0
    n = len(nums)
    prefix_sum = [0] * n
    
    for i in range(n):
        s += nums[i]
        prefix_sum[i] = s
    
    return prefix_sum
    # Time: O(n)
    # Space: O(n)

def main():
    result = running_sum([1,2,3,4])
    print(result) # [1,3,6,10]

    result = running_sum([1,1,1,1,1])
    print(result) # [1,2,3,4,5]

    result = running_sum([3,1,2,10,1])
    print(result) # [3,4,6,16,17]

if __name__ == "__main__":
    main()
