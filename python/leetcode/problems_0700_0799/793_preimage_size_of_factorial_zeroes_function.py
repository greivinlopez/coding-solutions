# -----------------------------------------------
# 793. Preimage Size of Factorial Zeroes Function
# -----------------------------------------------

# Problem: https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function
#
# Let f(x) be the number of zeroes at the end of x!. Recall that x! = 1 * 2 * 3 *
# ... * x and by convention, 0! = 1.
#         
#   * For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while
#     f(11) = 2 because 11! = 39916800 has two zeroes at the end.
# 
# Given an integer k, return the number of non-negative integers x have the
# property that f(x) = k.
# 
# Example 1:
# 
# Input: k = 0
# Output: 5
# 
# Explanation: 0!, 1!, 2!, 3!, and 4! end with k = 0 zeroes.
# 
# Example 2:
# 
# Input: k = 5
# Output: 0
# 
# Explanation: There is no x such that x! ends in k = 5 zeroes.
# 
# Example 3:
# 
# Input: k = 3
# Output: 5
# 
# Constraints:
#         0 <= k <= 10⁹

from bisect import bisect_right

# NOTE:
# This only work for Python 3.10+

# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def preimage_size_FZF(k):
    count = lambda x: 0 if x == 0 else x//5 + count(x//5)
        
    atLeast_K = lambda x: bisect_right(range(5*x + 5), x, key = count)

    return atLeast_K(k) - atLeast_K(k-1)


def main():
    result = preimage_size_FZF(k = 0)
    print(result) # 5

    result = preimage_size_FZF(k = 5)
    print(result) # 0

    result = preimage_size_FZF(k = 3)
    print(result) # 5

if __name__ == "__main__":
    main()
