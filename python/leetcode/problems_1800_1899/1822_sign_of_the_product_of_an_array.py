# ------------------------------------
# 1822. Sign Of The Product Of An Array
# ------------------------------------

# Problem: https://leetcode.com/problems/sign-of-the-product-of-an-array
#
# Implement a function signFunc(x) that returns:
#         1 if x is positive.
#         -1 if x is negative.
#         0 if x is equal to 0.
# 
# You are given an integer array nums. Let product be the product of all values in
# the array nums.
# 
# Return signFunc(product).
# 
# Example 1:
# 
# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144) =
# 1
# 
# Example 2:
# 
# Input: nums = [1,5,0,2,-3]
# Output: 0
# Explanation: The product of all values in the array is 0, and signFunc(0) = 0
# 
# Example 3:
# 
# Input: nums = [-1,1,-1,1,-1]
# Output: -1
# Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
# 
# 
# Constraints:
#         1 <= nums.length <= 1000
#         -100 <= nums[i] <= 100


# Solution: https://youtu.be/ILDLM86jNow
# Credit: Navdeep Singh founder of NeetCode
def array_sign(nums):
    flag = True
    for i in nums:
        if i == 0:
            return 0
        if i < 0:
            flag = not flag
    
    return 1 if flag else -1


def main():
    result = array_sign([-1,-2,-3,-4,3,2,1])
    print(result) # 1

    result = array_sign([1,5,0,2,-3])
    print(result) # 0

    result = array_sign([-1,1,-1,1,-1])
    print(result) # -1

if __name__ == "__main__":
    main()
