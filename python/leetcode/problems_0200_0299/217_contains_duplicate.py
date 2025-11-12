# -----------------------
# 217. Contains Duplicate
# -----------------------

# Problem: https://leetcode.com/problems/contains-duplicate/
# 
# Given an integer array nums, return true if any value appears at least twice 
# in the array, and return false if every element is distinct.
# 
#  
# Example 1:
# 
# Input: nums = [1,2,3,1]
# 
# Output: true
# 
# Explanation:
# 
# The element 1 occurs at the indices 0 and 3.
# 
# 
# Example 2:
# 
# Input: nums = [1,2,3,4]
# 
# Output: false
# 
# Explanation:
# 
# All elements are distinct.
# 
# 
# Example 3:
# 
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# 
# Output: true
# 
# 
# Constraints:
# 
# 	1 <= nums.length <= 105
# 	-109 <= nums[i] <= 109


# Solution: https://youtu.be/3OamzN90kPg
# Credit: Navdeep Singh founder of NeetCode
def contains_duplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

# Solution: https://youtu.be/a1_r3cLQ6wg
# Credit: Greg Hogg

# Brute Force Solution
def contains_duplicate_brute(nums):
    n = len(nums)

    for i in range(n):
        for j in range(n):
            if nums[i] == nums[j] and i != j:
                return True
    return False
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)

# Better Brute Force Solution
def contains_duplicate_brute_2(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return True
    return False
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)

# Optimal Solution : Same as Navdeep's
def contains_duplicate_alt(nums):
    s = set()
    for num in nums:
        if num in s:
            return True
        else:
            s.add(num)
    return False
    # Time Complexity: O(n)
    # Space Complexity: O(n)

def main():
    result = contains_duplicate([1,2,3,1])
    print(result) # True

    result = contains_duplicate([1,2,3,4])
    print(result) # False

    result = contains_duplicate([1,1,1,3,3,4,3,2,4,2])
    print(result) # True

if __name__ == "__main__":
    main()
