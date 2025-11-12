# ---------------------------------
# 2601. Prime Subtraction Operation
# ---------------------------------

# Problem: https://leetcode.com/problems/prime-subtraction-operation
#
# You are given a 0-indexed integer array nums of length n.
# 
# You can perform the following operation as many times as you want:
#         
#   * Pick an index i that you haven’t picked before, and pick a prime p
#     strictly less than nums[i], then subtract p from nums[i].
# 
# Return true if you can make nums a strictly increasing array using the above
# operation and false otherwise.
# 
# A strictly increasing array is an array whose each element is strictly greater
# than its preceding element.
# 
# Example 1:
# 
# Input: nums = [4,9,6,10]
# Output: true
# 
# Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3
# from nums[0], so that nums becomes [1,9,6,10].
# In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes
# equal to [1,2,6,10].
# After the second operation, nums is sorted in strictly increasing order, so the
# answer is true.
# 
# Example 2:
# 
# Input: nums = [6,8,11,12]
# Output: true
# 
# Explanation: Initially nums is sorted in strictly increasing order, so we don't
# need to make any operations.
# 
# Example 3:
# 
# Input: nums = [5,8,3]
# Output: false
# 
# Explanation: It can be proven that there is no way to perform operations to make
# nums sorted in strictly increasing order, so the answer is false.
# 
# 
# Constraints:
#         1 <= nums.length <= 1000
#         1 <= nums[i] <= 1000
#         nums.length == n

from math import sqrt

# Solution: https://youtu.be/G9cp9y45qEs
# Credit: Navdeep Singh founder of NeetCode
def prime_sub_operation(nums):
    def is_prime(n):
        for f in range(2, int(sqrt(n)) + 1):
            if n % f == 0:
                return False
        return True

    prev = 0
    for n in nums:
        upper_bound = n - prev
        largest_p = 0
        for i in reversed(range(2, upper_bound)):
            if is_prime(i):
                largest_p = i
                break

        if n - largest_p <= prev:
            return False
        prev = n - largest_p

    return True
    # Time: O(n * √m)
    # Space: O(1)
    # n = number of elements in nums
    # m = maximum value of upper_bound

def prime_sub_operation_alt(nums):
    # Optimized version
    def is_prime(n):
        for f in range(2, int(n**0.5) + 1):
            if n % f == 0:
                return False
        return True

    primes = [0, 0]
    for i in range(2, max(nums) + 1):
        if is_prime(i):
            primes.append(i)
        else:
            primes.append(primes[i - 1])

    prev = 0
    for n in nums:
        upper_bound = n - prev
        largest_p = primes[upper_bound - 1]
        if n - largest_p <= prev:
            return False
        prev = n - largest_p
        
    return True
    # Time: O(n + m * √m)
    # Space: O(m)
    # n = number of elements in nums
    # m = maximum value in nums


def main():
    result = prime_sub_operation(nums = [4,9,6,10])
    print(result) # True

    result = prime_sub_operation(nums = [6,8,11,12])
    print(result) # True

    result = prime_sub_operation(nums = [5,8,3])
    print(result) # False

if __name__ == "__main__":
    main()
