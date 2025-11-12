# ---------------------------------------------
# 1295. Find Numbers with Even Number of Digits
# ---------------------------------------------

# Problem: https://leetcode.com/problems/find-numbers-with-even-number-of-digits
#
# Given an array nums of integers, return how many of them contain an even number
# of digits.
# 
# Example 1:
# 
# Input: nums = [12,345,2,6,7896]
# Output: 2
# 
# Explanation:
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.
# 
# Example 2:
# 
# Input: nums = [555,901,482,1771]
# Output: 1
# 
# Explanation:
# Only 1771 contains an even number of digits.
# 
# 
# Constraints:
#         1 <= nums.length <= 500
#         1 <= nums[i] <= 10⁵


# Solution: https://algo.monster/liteproblems/1295
# Credit: AlgoMonster
def find_numbers(nums):
    # Convert each number to string, check if digit count is even, sum the True values
    return sum(len(str(num)) % 2 == 0 for num in nums)
    # Time: O(n * log m)
    # Space: O(log m)
    # n = the length of the array nums
    # m = the maximum value of the elements in the array.


def main():
    result = find_numbers(nums = [12,345,2,6,7896])
    print(result) # 2

    result = find_numbers(nums = [555,901,482,1771])
    print(result) # 1

if __name__ == "__main__":
    main()
