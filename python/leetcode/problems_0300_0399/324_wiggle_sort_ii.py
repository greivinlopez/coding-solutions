# -------------------
# 324. Wiggle Sort II
# -------------------

# Problem: https://leetcode.com/problems/wiggle-sort-ii
#
# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] <
# nums[3]....
# 
# You may assume the input array always has a valid answer.
# 
# Example 1:
# 
# Input: nums = [1,5,1,1,6,4]
# Output: [1,6,1,5,1,4]
# 
# Explanation: [1,4,1,5,1,6] is also accepted.
# 
# Example 2:
# 
# Input: nums = [1,3,2,2,3,1]
# Output: [2,3,1,3,1,2]
# 
# 
# Constraints:
#         1 <= nums.length <= 5 * 10⁴
#         0 <= nums[i] <= 5000
#         It is guaranteed that there will be an answer for the given input nums.
# 
# Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?

# Solution: https://leetcode.com/problems/wiggle-sort-ii/solutions/3242335/324-time-99-2-and-space-99-16-solution-with-step-by-step-explanation
# Credit: Marlen Kanatbekov -> https://leetcode.com/u/Marlen09/
def wiggle_sort(nums):
    n = len(nums)
    nums.sort()
    mid = (n - 1) // 2
    nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    nums1 = [1,5,1,1,6,4]
    wiggle_sort(nums1)
    print(nums1) # [1, 6, 1, 5, 1, 4]

    nums2 = [1,3,2,2,3,1]
    wiggle_sort(nums2)
    print(nums2) # [2, 3, 1, 3, 1, 2]

if __name__ == "__main__":
    main()
