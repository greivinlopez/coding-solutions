# -----------------------------------------------------------
# 1968. Array With Elements Not Equal To Average Of Neighbors
# -----------------------------------------------------------

# Problem: https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors
#
# You are given a 0-indexed array nums of distinct integers. You want to rearrange
# the elements in the array such that every element in the rearranged array is not
# equal to the average of its neighbors.
# 
# More formally, the rearranged array should have the property such that for every
# i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not
# equal to nums[i].
# 
# Return any rearrangement of nums that meets the requirements.
# 
# Example 1:
# 
# Input: nums = [1,2,3,4,5]
# Output: [1,2,4,5,3]
# Explanation:
# When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
# When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
# When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.
# 
# Example 2:
# 
# Input: nums = [6,2,0,9,7]
# Output: [9,7,6,2,0]
# Explanation:
# When i=1, nums[i] = 7, and the average of its neighbors is (9+6) / 2 = 7.5.
# When i=2, nums[i] = 6, and the average of its neighbors is (7+2) / 2 = 4.5.
# When i=3, nums[i] = 2, and the average of its neighbors is (6+0) / 2 = 3.
# Note that the original array [6,2,0,9,7] also satisfies the conditions.
# 
# 
# Constraints:
#         3 <= nums.length <= 10^5
#         0 <= nums[i] <= 10^5


# Solution: https://youtu.be/Wmb3YdVYfqM
# Credit: Navdeep Singh founder of NeetCode

    # Solution 1: Sort and fill
    # Intuition:
    # Ensure the below pattern (no Avg number can form at nums[i]:
    # nums[i-1] < nums[i] > nums[i+1]

    # Input: nums = [6,2,0,9,7]
    # Sorted nums = [0,2,6,7,9]
    # 1st Filled arr = [0,_,2,_,6]
    # 2nd Filled arr = [0,7,2,9,6]

def rearrange_array(nums):
    nums.sort()

    i, j, n = 0, 0, len(nums)
    ans = [0]*n

    while i < n and j < n:
        ans[i] = nums[j]
        i = i + 2
        j = j + 1

    i = 1
    while i < n and j < n:
        ans[i] = nums[j]
        i = i + 2
        j = j + 1

    return ans


def main():
    result = rearrange_array([1,2,3,4,5])
    print(result) # [1, 4, 2, 5, 3]

    result = rearrange_array([6,2,0,9,7])
    print(result) # [0, 7, 2, 9, 6]

if __name__ == "__main__":
    main()
