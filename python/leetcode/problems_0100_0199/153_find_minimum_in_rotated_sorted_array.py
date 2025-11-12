# -----------------------------------------
# 153. Find Minimum In Rotated Sorted Array
# -----------------------------------------

# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# 
# Suppose an array of length n sorted in ascending order is rotated between 1 
# and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
# 
# 	[4,5,6,7,0,1,2] if it was rotated 4 times.
# 	[0,1,2,4,5,6,7] if it was rotated 7 times.
# 
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results 
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# 
# Given the sorted rotated array nums of unique elements, return the minimum 
# element of this array.
# 
# You must write an algorithm that runs in O(log n) time.
#  
# 
# Example 1:
# 
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# 
# 
# Example 2:
# 
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# 
# 
# Example 3:
# 
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
# 
#  
# Constraints:
# 
# 	n == nums.length
# 	1 <= n <= 5000
# 	-5000 <= nums[i] <= 5000
# 	All the integers of nums are unique.
# 	nums is sorted and rotated between 1 and n times.


# Solution: https://youtu.be/nIVW4P8b1VA
# Credit: Navdeep Singh founder of NeetCode
def find_min(nums):
    # Time: O(log(n))
    # Space: O(1)
    start , end = 0, len(nums) - 1 
    curr_min = float("inf")
    
    while start  <  end :
        mid = start + (end - start ) // 2
        curr_min = min(curr_min,nums[mid])
        
        # right has the min 
        if nums[mid] > nums[end]:
            start = mid + 1
            
        # left has the  min 
        else:
            end = mid - 1 
            
    return min(curr_min,nums[start])

# Solution: https://youtu.be/H2U24n4bcQQ
# Credit: Greg Hogg
# Same Solution

def main():
    result = find_min([3,4,5,1,2])
    print(result) # 1

    result = find_min([4,5,6,7,0,1,2])
    print(result) # 0

    result = find_min([11,13,15,17])
    print(result) # 11

if __name__ == "__main__":
    main()
