# --------------------------------------------
# 154. Find Minimum in Rotated Sorted Array II
# --------------------------------------------

# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii
#
# Suppose an array of length n sorted in ascending order is rotated between 1 and
# n times. For example, the array nums = [0,1,4,4,5,6,7] might become:
#
#          [4,5,6,7,0,1,4] if it was rotated 4 times.
#         [0,1,4,4,5,6,7] if it was rotated 7 times.
# 
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in
# the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# 
# Given the sorted rotated array nums that may contain duplicates, return the
# minimum element of this array.
# 
# You must decrease the overall operation steps as much as possible.
# 
# Example 1:
# 
# Input: nums = [1,3,5]
# Output: 1
# 
# Example 2:
# 
# Input: nums = [2,2,2,0,1]
# Output: 0
# 
# Constraints:
#         n == nums.length
#         1 <= n <= 5000
#         -5000 <= nums[i] <= 5000
#         nums is sorted and rotated between 1 and n times.
# 
# Follow up: This problem is similar to Find Minimum in Rotated Sorted Array,
# but nums may contain duplicates. Would this affect the runtime complexity? How
# and why?


# Solution: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/solutions/4881165/100-0ms-8-liner-code-proof-easy-mahiya-se-shava-java-c-py3-js-php-all-in-one
# Credit: saurabh2002rawat -> https://leetcode.com/u/_Torpedo_/
def find_min(nums):
    s , e = 0 , len (nums) - 1 
    while s < e :
        m = s + (e - s ) // 2 
        if nums[m] == nums[s] and nums[m] == nums[e] :
            s += 1
            e -= 1
        elif nums[m] <= nums[e] :  e = m 
        else  :      s = m + 1 
    return nums [s] 
    # Time: O(log(n))
    # Space: O(1)


def main():
    result = find_min(nums = [1,3,5])
    print(result) # 1

    result = find_min(nums = [2,2,2,0,1])
    print(result) # 0

if __name__ == "__main__":
    main()
