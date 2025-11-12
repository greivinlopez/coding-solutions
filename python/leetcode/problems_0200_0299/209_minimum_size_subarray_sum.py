# ------------------------------
# 209. Minimum Size Subarray Sum
# ------------------------------

# Problem: https://leetcode.com/problems/minimum-size-subarray-sum/
# 
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# 
# Example 1:
# 
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# 
# 
# Example 2:
# 
# Input: target = 4, nums = [1,4,4]
# Output: 1
# 
# 
# Example 3:
# 
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
# 
#  
# Constraints:
# 
# 	1 <= target <= 109
# 	1 <= nums.length <= 105
# 	1 <= nums[i] <= 104
#  
# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).


# Solution: https://youtu.be/aYqYMIqZx5s
# Credit: Navdeep Singh founder of NeetCode
def min_sub_array_len(target, nums):
    # Time: O(n)
    # Space: O(1)
    res = float('inf')
    l, total = 0, 0

    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(res, r - l + 1)
            total -= nums[l]
            l += 1
    return res if res != float('inf') else 0

# Solution: https://youtu.be/RG17VCQOFpg
# Credit: Greg Hogg
# Same Solution

def main():
    result = min_sub_array_len(target = 7, nums = [2,3,1,2,4,3])
    print(result) # 2

    result = min_sub_array_len(target = 4, nums = [1,4,4])
    print(result) # 1

    result = min_sub_array_len(target = 11, nums = [1,1,1,1,1,1,1,1])
    print(result) # 0

if __name__ == "__main__":
    main()
