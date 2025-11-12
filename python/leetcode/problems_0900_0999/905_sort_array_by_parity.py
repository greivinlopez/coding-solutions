# -------------------------
# 905. Sort Array By Parity
# -------------------------

# Problem: https://leetcode.com/problems/sort-array-by-parity
#
# Given an integer array nums, move all the even integers at the beginning of the
# array followed by all the odd integers.
# 
# Return any array that satisfies this condition.
# 
# Example 1:
# 
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# 
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be
# accepted.
# 
# Example 2:
# 
# Input: nums = [0]
# Output: [0]
# 
# 
# Constraints:
#         1 <= nums.length <= 5000
#         0 <= nums[i] <= 5000


# Solution: https://youtu.be/QC4c9fyr8As
# Credit: Navdeep Singh founder of NeetCode
def sort_array_by_parity(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r] % 2 == 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    return nums
    # Time: O(n) 
    # Space: O(1)


def main():
    result = sort_array_by_parity([3,1,2,4])
    print(result) # [2,4,3,1]

    result = sort_array_by_parity([0])
    print(result) # [0]

if __name__ == "__main__":
    main()
