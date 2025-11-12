# ---------------------------------
# 238. Product Of Array Except Self
# ---------------------------------

# Problem: https://leetcode.com/problems/product-of-array-except-self/
# 
# Given an integer array nums, return an array answer such that answer[i] is 
# equal to the product of all the elements of nums except nums[i].
# 
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
# integer.
# 
# You must write an algorithm that runs in O(n) time and without using the 
# division operation.
# 
#  
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
# 
#  
# Constraints:
# 
# 	2 <= nums.length <= 105
# 	-30 <= nums[i] <= 30
# 	The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
# 
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


# Solution: https://youtu.be/bNvIQI2wAjk
# Credit: Navdeep Singh founder of NeetCode
def product_except_self(nums):
    res = [1] * (len(nums))

    for i in range(1, len(nums)):
        res[i] = res[i-1] * nums[i-1]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

# Solution: https://youtu.be/bNvIQI2wAjk
# Credit: Greg Hogg

# Brute Force Solution
def product_except_self_brute(nums):
    n = len(nums)
    ans = [0] * n

    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        ans[i] = prod
    
    return ans
    # Time: O(n^2)
    # Space: O(n)


# Optimal Solution
def product_except_self_optimal(nums):
    l_mult = 1
    r_mult = 1
    n = len(nums)
    l_arr = [0] * n
    r_arr = [0] * n
    
    for i in range(n): 
        j = -i -1
        l_arr[i] = l_mult
        r_arr[j] = r_mult
        l_mult *= nums[i]
        r_mult *= nums[j]

    return [l*r for l, r in zip(l_arr, r_arr)]
    # Time Complexity: O(n)
    # Space Complexity: O(n)


# Optimal Solution for Bootcamp
def product_except_self_boot(nums):
    n = len(nums)
    answer = [0] * n

    L = 1
    left_product = [0] * n

    for i in range(n):
        left_product[i] = L
        L *= nums[i]


    R = 1
    right_product = [0] * n

    for i in range(n-1, -1, -1):
        right_product[i] = R
        R *= nums[i]
    

    for i in range(n):
        answer[i] = left_product[i] * right_product[i]
    
    return answer   
    # Time Complexity: O(n)
    # Space Complexity: O(n)

def main():
    result = product_except_self([1,2,3,4])
    print(result) # [24,12,8,6]

    result = product_except_self([-1,1,0,-3,3])
    print(result) # [0,0,9,0,0]

if __name__ == "__main__":
    main()
