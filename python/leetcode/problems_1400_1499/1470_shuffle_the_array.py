# -----------------------
# 1470. Shuffle the Array
# -----------------------

# Problem: https://leetcode.com/problems/shuffle-the-array
#
# Given the array nums consisting of 2n elements in the form
# [x1,x2,...,xn,y1,y2,...,yn].
# 
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
# 
# Example 1:
# 
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is
# [2,3,5,4,1,7].
# 
# Example 2:
# 
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
# 
# Example 3:
# 
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]
# 
# 
# Constraints:
#         1 <= n <= 500
#         nums.length == 2n
#         1 <= nums[i] <= 10^3


# Solution: https://youtu.be/IvIKD_EU8BY
# Credit: Navdeep Singh founder of NeetCode
def shuffle(nums, n):
    for i in range(n):
        nums[i] = nums[i] << 10
        nums[i] = nums[i] | nums[i + n]  # store x, y
    
    j = 2 * n - 1
    for i in range(n - 1, -1, -1):
        y = nums[i] & (2**10 - 1)
        x = nums[i] >> 10
        nums[j] = y
        nums[j - 1] = x
        j -= 2
    
    return nums
    # Time: O(n)
    # Space: O(1)


def main():
    result = shuffle(nums = [2,5,1,3,4,7], n = 3)
    print(result) # [2,3,5,4,1,7]

    result = shuffle(nums = [1,2,3,4,4,3,2,1], n = 4)
    print(result) # [1,4,2,3,3,2,4,1]

    result = shuffle(nums = [1,1,2,2], n = 2)
    print(result) # [1,2,1,2]

if __name__ == "__main__":
    main()
