# -------------------------------
# 416. Partition Equal Subset Sum
# -------------------------------

# Problem: https://leetcode.com/problems/partition-equal-subset-sum/
# 
# Given an integer array nums, return true if you can partition the array into 
# two subsets such that the sum of the elements in both subsets is equal or 
# false otherwise.
# 
#  
# Example 1:
# 
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# Example 2:
# 
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
#  
# Constraints:
# 
# 	1 <= nums.length <= 200
# 	1 <= nums[i] <= 100


# Solution: https://youtu.be/snue4L5WrJ4
# Credit: Navdeep Singh founder of NeetCode
def can_partition(nums):
    if sum(nums) % 2:
        return False

    dp = set()
    dp.add(0)
    target = sum(nums) // 2

    for i in range(len(nums) - 1, -1, -1):
        nextDP = set()
        for t in dp:
            if (t + nums[i]) == target:
                return True
            nextDP.add(t + nums[i])
            nextDP.add(t)
        dp = nextDP
    return False
    # Time: O(n) where n is sum(nums)


def main():
    result = can_partition([1,5,11,5])
    print(result) # True

    result = can_partition([1,2,3,5])
    print(result) # False

if __name__ == "__main__":
    main()
