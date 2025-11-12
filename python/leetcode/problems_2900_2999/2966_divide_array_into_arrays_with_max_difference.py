# --------------------------------------------------
# 2966. Divide Array Into Arrays With Max Difference
# --------------------------------------------------

# Problem: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference
#
# You are given an integer array nums of size n where n is a multiple of 3 and a
# positive integer k.
# 
# Divide the array nums into n / 3 arrays of size 3 satisfying the following
# condition:
#         
#   * The difference between any two elements in one array is less than or equal to k.
# 
# Return a 2D array containing the arrays. If it is impossible to satisfy the
# conditions, return an empty array. And if there are multiple answers, return any
# of them.
# 
# Example 1:
# 
# Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
# Output: [[1,1,3],[3,4,5],[7,8,9]]
# 
# Explanation:
# The difference between any two elements in each array is less than or equal to
# 2.
# 
# Example 2:
# 
# Input: nums = [2,4,2,2,5,2], k = 2
# Output: []
# 
# Explanation:
# Different ways to divide nums into 2 arrays of size 3 are:
#         [[2,2,2],[2,4,5]] (and its permutations)
#         [[2,2,4],[2,2,5]] (and its permutations)
# Because there are four 2s there will be an array with the elements 2 and 5 no
# matter how we divide it. since 5 - 2 = 3 > k, the condition is not satisfied and
# so there is no valid division.
# 
# Example 3:
# 
# Input: nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14
# Output: [[2,2,2],[4,5,5],[5,5,7],[7,8,8],[9,9,10],[11,12,12]]
# 
# Explanation:
# The difference between any two elements in each array is less than or equal to
# 14.
# 
# 
# Constraints:
#         n == nums.length
#         1 <= n <= 10^5
#         n is a multiple of 3
#         1 <= nums[i] <= 10^5
#         1 <= k <= 10^5


# Solution: https://youtu.be/XleOio1oJeo
# Credit: Navdeep Singh founder of NeetCode
def divide_array(nums, k):
    nums.sort()
    res = []
    for i in range(0, len(nums), 3):
        if nums[i + 2] - nums[i] > k:
            return []
        res.append(nums[i:i + 3])
    return res
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    nums = [1,3,4,8,7,9,3,5,1]
    result = divide_array(nums, 2)
    print(result) # [[1,1,3],[3,4,5],[7,8,9]]

    nums = [2,4,2,2,5,2]
    result = divide_array(nums, 2)
    print(result) # []

    nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11]
    result = divide_array(nums, 14)
    print(result) # [[2,2,2],[4,5,5],[5,5,7],[7,8,8],[9,9,10],[11,12,12]]

if __name__ == "__main__":
    main()
