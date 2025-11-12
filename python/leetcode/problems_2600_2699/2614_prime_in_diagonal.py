# -----------------------
# 2614. Prime In Diagonal
# -----------------------

# Problem: https://leetcode.com/problems/prime-in-diagonal
#
# You are given a 0-indexed two-dimensional integer array nums.
# 
# Return the largest prime number that lies on at least one of the diagonals of
# nums. In case, no prime is present on any of the diagonals, return 0.
# 
# Note that:
#   * An integer is prime if it is greater than 1 and has no positive integer
#     divisors other than 1 and itself.
#   * An integer val is on one of the diagonals of nums if there exists an
#     integer i for which nums[i][i] = val or an i for which 
#     nums[i][nums.length - i - 1] = val.
# 
# https://assets.leetcode.com/uploads/2023/03/06/screenshot-2023-03-06-at-45648-pm.png
# 
# In the above diagram, one diagonal is [1,5,9] and another diagonal is [3,5,7].
# 
# Example 1:
# 
# Input: nums = [[1,2,3],[5,6,7],[9,10,11]]
# Output: 11
# 
# Explanation: The numbers 1, 3, 6, 9, and 11 are the only numbers present on at
# least one of the diagonals. Since 11 is the largest prime, we return 11.
# 
# Example 2:
# 
# Input: nums = [[1,2,3],[5,17,7],[9,11,10]]
# Output: 17
# 
# Explanation: The numbers 1, 3, 9, 10, and 17 are all present on at least one of
# the diagonals. 17 is the largest prime, so we return 17.
# 
# 
# Constraints:
#         1 <= nums.length <= 300
#         nums.length == numsi.length
#         1 <= nums[i][j] <= 4 * 10⁶

import math

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def diagonal_prime(nums):
    def isPrime(n):
        if n == 1:
            return False
        i = 2
        while i <= int(math.sqrt(n)):
            if n%i == 0:
                return False
        
            i += 1
        return True
    
    dic = {}
    prime = 0
    
    for i in range(len(nums)):
        first = nums[i][i]
        sec = nums[i][len(nums)-i-1]
        flag1 = False
        if first in dic:
            if dic[first] == True:
                prime = max(prime, first)
                
        elif isPrime(first):
            flag1 = True
            prime = max(prime, first)
            
        dic[first] = flag1
            
        flag2 = False
        if sec in dic:
            if dic[sec] == True:
                prime = max(prime, sec)
                
        elif isPrime(sec):
            flag2 = True
            prime = max(prime, sec)
            
        dic[sec] = flag2
        
    return prime
    # Time: O(n * √m)
    # Space: O(n)
    # n = dimension of the square matrix | length of nums
    # m = maximum value of any element in the matrix.


def main():
    result = diagonal_prime([[1,2,3],[5,6,7],[9,10,11]])
    print(result) # 11

    result = diagonal_prime([[1,2,3],[5,17,7],[9,11,10]])
    print(result) # 17

if __name__ == "__main__":
    main()
