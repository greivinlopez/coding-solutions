# ----------------------------------
# 918. Maximum Sum Circular Subarray
# ----------------------------------

# Problem: https://leetcode.com/problems/maximum-sum-circular-subarray/
# 
# Given a circular integer array nums of length n, return the maximum possible 
# sum of a non-empty subarray of nums.
# 
# A circular array means the end of the array connects to the beginning of the 
# array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the 
# previous element of nums[i] is nums[(i - 1 + n) % n].
# 
# A subarray may only include each element of the fixed buffer nums at most 
# once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there 
# does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
# 
#  
# Example 1:
# 
# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.
# 
# Example 2:
# 
# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
# 
# Example 3:
# 
# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.
#  
# 
# Constraints:
# 
#   n == nums.length
#   1 <= n <= 3 * 10^4
#   -3 * 10^4 <= nums[i] <= 3 * 10^4


# Solution: https://youtu.be/fxT9KjakYPM
# Credit: Navdeep Singh founder of NeetCode
def max_subarray_sum_circular(nums):
    globMax, globMin = nums[0], nums[0]
    curMax, curMin = 0, 0
    total = 0
    
    for i, n in enumerate(nums):
        curMax = max(curMax + n, n)
        curMin = min(curMin + n, n)
        total += n
        globMax = max(curMax, globMax)
        globMin = min(curMin, globMin)

    return max(globMax, total - globMin) if globMax > 0 else globMax


def main():
    result = max_subarray_sum_circular([1,-2,3,-2])
    print(result) # 3

    result = max_subarray_sum_circular([5,-3,5])
    print(result) # 10

    result = max_subarray_sum_circular([-3,-2,-3])
    print(result) # -2

if __name__ == "__main__":
    main()
