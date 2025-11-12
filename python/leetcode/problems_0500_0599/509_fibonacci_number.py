# ---------------------
# 509. Fibonacci Number
# ---------------------

# Problem: https://leetcode.com/problems/fibonacci-number/
# 
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the 
# Fibonacci sequence, such that each number is the sum of the two preceding 
# ones, starting from 0 and 1. That is,
# 
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# 
# Given n, calculate F(n).
# 
#  
# Example 1:
# 
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# 
# 
# Example 2:
# 
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# 
# 
# Example 3:
# 
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#  
# 
# Constraints:
# 
#   -10^7 <= num <= 10^7

# Solution: https://youtu.be/dDokMfPpfu4
# Credit: Navdeep Singh founder of NeetCode
class Solution:
    Memo = {}

    def fib(self, n: int):
        if n in self.Memo:
            return self.Memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        self.Memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.Memo[n]

# Solution: https://youtu.be/FggXDrgeI20
# Credit: Greg Hogg

# Top Down Recursive
def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    # Time: O(2^n)
    # Space: O(n)


# Top Down Memoized
def fib_memo(n):
    memo = {0:0, 1:1}

    def f(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x-1) + f(x-2)
            return memo[x]
    
    return f(n)
    # Time: O(n)
    # Space: O(n)

# Bottom Up Tabulation
def fib_bottom(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]

    return dp[n]
    # Time: O(n)
    # Space: O(n)


# Bottom Up Constant Space
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev = 0
    cur = 1

    for i in range(2, n+1):
        prev, cur = cur, prev+cur
    
    return cur
    # Time: O(n)
    # Space: O(1)


def main():
    result = fib(2)
    print(result) # 1

    result = fib(3)
    print(result) # 2

    result = fib(4)
    print(result) # 3

    result = fib(30)
    print(result) # 832040

if __name__ == "__main__":
    main()
