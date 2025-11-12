# -------------------------------
# 479. Largest Palindrome Product
# -------------------------------

# Problem: https://leetcode.com/problems/largest-palindrome-product
#
# Given an integer n, return the largest palindromic integer that can be
# represented as the product of two n-digits integers. Since the answer can be
# very large, return it modulo 1337.
# 
# Example 1:
# 
# Input: n = 2
# Output: 987
# 
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
# 
# Example 2:
# 
# Input: n = 1
# Output: 9
# 
# 
# Constraints:
#         1 <= n <= 8


# Solution: https://algo.monster/liteproblems/479
# Credit: AlgoMonster
def largest_palindrome(n):
    # Special case: for n=1, the largest palindrome product is 9 (3*3)
    if n == 1:
        return 9
        
    # Find the maximum n-digit number (e.g., n=2 -> 99)
    max_num = 10**n - 1
    
    # Try to construct palindromes starting from the largest possible
    # We iterate from max_num down to max_num//10 (the minimum n-digit number is 10^(n-1))
    for first_half in range(max_num, max_num // 10, -1):
        # Construct a palindrome by mirroring the first half
        # For example, if first_half = 123, palindrome = 123321
        palindrome = first_half
        temp = first_half
        
        # Mirror the digits to create the second half of the palindrome
        while temp > 0:
            palindrome = palindrome * 10 + temp % 10
            temp //= 10
        
        # Check if this palindrome can be expressed as a product of two n-digit numbers
        # Start from the largest possible divisor
        divisor = max_num
        
        # Only check divisors whose square is >= palindrome
        # The factor (palindrome / divisor) must also be an n-digit number. 
        # Since we check divisors down to max_num // 10, the factors are implicitly checked.
        while divisor * divisor >= palindrome:
            if palindrome % divisor == 0:
                # The other factor is palindrome // divisor.
                # If divisor is an n-digit number, we must ensure palindrome // divisor is also an n-digit number.
                # Since we iterate 'first_half' down to 10**(n-1), the palindrome is at least (10^(n-1)) * (10^(n-1)).
                # Since we check divisor up to max_num, the smallest factor (palindrome // divisor) is checked against 10**(n-1).
                # The condition for the other factor being n-digit is implicitly handled by the loop boundary of `first_half`
                # and the inner loop's structure.
                
                # Found a valid factorization, return result modulo 1337
                return palindrome % 1337
            divisor -= 1
            
    # This should not be reached for valid inputs where a solution exists
    return 9
    # Time: O(10²ⁿ)
    # Space: O(1)
    # n = the number of digits


# My Solution:
# As this problem input is 1..8 perhaps the optimized solution is a precomputed hashtable
def largest_palindrome(n):
    results = {
        1: 9,
        2: 987,
        3: 123,
        4: 597,
        5: 677,
        6: 1218,
        7: 877,
        8: 475
    }
    return results.get(n, 0)


def main():
    result = largest_palindrome(2)
    print(result) # 987

    result = largest_palindrome(1)
    print(result) # 9

if __name__ == "__main__":
    main()
