# ------------------------------
# 977. Squares Of A Sorted Array
# ------------------------------

# Problem: https://leetcode.com/problems/squares-of-a-sorted-array
#
# Given an integer array nums sorted in non-decreasing order, return an array of
# the squares of each number sorted in non-decreasing order.
# 
# 
# Example 1:
# 
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# 
# Example 2:
# 
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# 
# Constraints:
#         1 <= nums.length <= 104
#         -104 <= nums[i] <= 104
#         nums is sorted in non-decreasing order.
# 
# Follow up: Squaring each element and sorting the new array is very trivial,
# could you find an O(n) solution using a different approach?


# Solution: https://youtu.be/FPCZsG_AkUg
# Credit: Navdeep Singh founder of NeetCode
def sorted_squares(nums):
    n = len(nums)
    res = [0] * n
    l, r = 0, n - 1
    
    while l <= r:
        left, right = abs(nums[l]), abs(nums[r])
        if left > right:
            res[r - l] = left * left
            l += 1
        else:
            res[r - l] = right * right
            r -= 1
    return res

# Solution: https://youtu.be/z0InhrjK3es
# Credit: Greg Hogg
def sorted_squares_brute(nums):
    # Brute Force Solution
    n = len(nums)
    for i in range(n):
        nums[i] = nums[i] ** 2
    
    nums.sort()

    return nums
    # Time: O(n log n)
    # Space: O(1)

def sorted_squares_optimal(nums):
    # Optimal Solution for Bootcamp
    n = len(nums)
    L, R = 0, n-1
    result = [0] * n

    for i in range(n):
        nums[i] = nums[i] ** 2

    j = n-1
    while L <= R:
        if nums[L] > nums[R]:
            result[j] = nums[L]
            L += 1
        else:
            result[j] = nums[R]
            R -= 1

        j -= 1
    
    return result
    # Time: O(n)
    # Space: O(n)

def sorted_squares_yt(nums):
    # Optimal Solution in YT Video
    left = 0
    right = len(nums) - 1
    result = []

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1
        else:
            result.append(nums[right] ** 2)
            right -= 1

    result.reverse()

    return result
    # Time: O(n)
    # Space: O(n)

def main():
    result = sorted_squares(nums = [-4,-1,0,3,10])
    print(result) # [0,1,9,16,100]

    result = sorted_squares(nums = [-7,-3,2,3,11])
    print(result) # [4,9,9,49,121]

if __name__ == "__main__":
    main()
