# --------------------------------------------------------------
# 2535. Difference Between Element Sum and Digit Sum of an Array
# --------------------------------------------------------------

# Problem: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array
#
# You are given a positive integer array nums.
#         
#   * The element sum is the sum of all the elements in nums.
#   * The digit sum is the sum of all the digits (not necessarily distinct)
#     that appear in nums.
# 
# Return the absolute difference between the element sum and digit sum of nums.
# 
# Note that the absolute difference between two integers x and y is defined as |x - y|.
# 
# Example 1:
# 
# Input: nums = [1,15,6,3]
# Output: 9
# 
# Explanation:
# The element sum of nums is 1 + 15 + 6 + 3 = 25.
# The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
# The absolute difference between the element sum and digit sum is |25 - 16| = 9.
# 
# Example 2:
# 
# Input: nums = [1,2,3,4]
# Output: 0
# 
# Explanation:
# The element sum of nums is 1 + 2 + 3 + 4 = 10.
# The digit sum of nums is 1 + 2 + 3 + 4 = 10.
# The absolute difference between the element sum and digit sum is |10 - 10| = 0.
# 
# 
# Constraints:
#         1 <= nums.length <= 2000
#         1 <= nums[i] <= 2000


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def difference_of_sum(nums):
    ele_sum = sum(nums)
    
    def digit_sum(nums):
        dig_sum = 0
        
        for i in range(len(nums)):
            num = nums[i]
            while num > 0:
                rem = num%10
                dig_sum += rem
                num = num//10
        
        return dig_sum
    
    dig_sum = digit_sum(nums)
    
    return abs(ele_sum - dig_sum)
    # Time: O(n * m)
    # Space: O(1)
    # n = the length of the input list
    # m = the maximum number of digits in any number in nums


def main():
    result = difference_of_sum(nums = [1,15,6,3])
    print(result) # 9

    result = difference_of_sum(nums = [1,2,3,4])
    print(result) # 0

if __name__ == "__main__":
    main()
