# ---------------------
# 169. Majority Element
# ---------------------

# Problem: https://leetcode.com/problems/majority-element/
# 
# Given an array nums of size n, return the majority element.
# 
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
# 
#  
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# 
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
# 
#  
# Constraints:
# 
# 	n == nums.length
# 	1 <= n <= 5 * 104
# 	-109 <= nums[i] <= 109
# 
# Follow-up: Could you solve the problem in linear time and in O(1) space?


# Solution: https://youtu.be/7pnhv842keE
# Credit: Navdeep Singh founder of NeetCode
def majority_element(nums):
    # Time: O(n)
    # Space: O(1)
    res, count = 0, 0

    for n in nums:
        if count == 0:
            res = n
        count += (1 if n == res else -1)
        
    return res

# Solution: https://youtu.be/c1B3LZQtZ_s
# Credit: Greg Hogg
# Same Solution

def main():
    result = majority_element([3,2,3])
    print(result) # 3

    result = majority_element([2,2,1,1,1,2,2])
    print(result) # 2

if __name__ == "__main__":
    main()
