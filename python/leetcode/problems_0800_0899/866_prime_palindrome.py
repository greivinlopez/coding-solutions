# ---------------------
# 866. Prime Palindrome
# ---------------------

# Problem: https://leetcode.com/problems/prime-palindrome
#
# Given an integer n, return the smallest prime palindrome greater than or equal
# to n.
# 
# An integer is prime if it has exactly two divisors: 1 and itself. Note that 1 is
# not a prime number.
#         
#   * For example, 2, 3, 5, 7, 11, and 13 are all primes.
# 
# An integer is a palindrome if it reads the same from left to right as it does
# from right to left.
#         
#   * For example, 101 and 12321 are palindromes.
# 
# The test cases are generated so that the answer always exists and is in the
# range [2, 2 * 108].
# 
# Example 1:
# 
# Input: n = 6
# Output: 7
# 
# Example 2:
# 
# Input: n = 8
# Output: 11
# 
# Example 3:
# 
# Input: n = 13
# Output: 101
# 
# 
# Constraints:
#         1 <= n <= 10⁸


# Solution: https://algo.monster/liteproblems/866
# Credit: AlgoMonster
def prime_palindrome(n):
    # Helper function to check if a number is prime.
    def is_prime(x):
        if x < 2:
            return False
        divisor = 2
        # Check divisors up to the square root of x.
        while divisor * divisor <= x:
            if x % divisor == 0:
                return False
            divisor += 1
        return True

    # Helper function to reverse an integer number.
    def reverse(x):
        result = 0
        while x:
            result = result * 10 + x % 10  # Add the last digit of x to result.
            x //= 10  # Remove the last digit of x.
        return result

    # Loop until we find the palindrome prime.
    while True:
        # Check if the number is both a palindrome and prime.
        if reverse(n) == n and is_prime(n):
            return n
        # Skip all numbers between 10^7 and 10^8, as there are no 8-digit palindrome primes.
        if 10**7 < n < 10**8:
            n = 10**8
        n += 1  # Go to the next number.
    # Time: O(n * √n)
    # Space: O(1)


def main():
    result = prime_palindrome(6)
    print(result) # 7

    result = prime_palindrome(8)
    print(result) # 11

    result = prime_palindrome(13)
    print(result) # 101

if __name__ == "__main__":
    main()
