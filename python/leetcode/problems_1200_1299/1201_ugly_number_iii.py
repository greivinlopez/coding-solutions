# ---------------------
# 1201. Ugly Number III
# ---------------------

# Problem: https://leetcode.com/problems/ugly-number-iii
#
# An ugly number is a positive integer that is divisible by a, b, or c.
# 
# Given four integers n, a, b, and c, return the nth ugly number.
# 
# Example 1:
# 
# Input: n = 3, a = 2, b = 3, c = 5
# Output: 4
# 
# Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
# 
# Example 2:
# 
# Input: n = 4, a = 2, b = 3, c = 4
# Output: 6
# 
# Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
# 
# Example 3:
# 
# Input: n = 5, a = 2, b = 11, c = 13
# Output: 10
# 
# Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
# 
# 
# Constraints:
#         1 <= n, a, b, c <= 10⁹
#         1 <= a * b * c <= 10¹⁸
#         It is guaranteed that the result will be in range [1, 2 * 10⁹].

from math import gcd

# Solution: https://algo.monster/liteproblems/1201
# Credit: AlgoMonster
def nth_ugly_number(n, a, b, c):
    # Helper function to calculate Least Common Multiple
    def lcm(x: int, y: int) -> int:
        return x * y // gcd(x, y)
    
    # Calculate LCMs for pairs and triplet
    lcm_ab = lcm(a, b)
    lcm_bc = lcm(b, c)
    lcm_ac = lcm(a, c)
    lcm_abc = lcm(lcm_ab, c)
    
    # Binary search range: minimum is 1, maximum is 2 * 10^9
    left, right = 1, 2 * 10**9
    
    # Binary search to find the nth ugly number
    while left < right:
        mid = (left + right) // 2
        
        # Count how many ugly numbers are <= mid using inclusion-exclusion principle
        # Numbers divisible by a, b, or c
        count = (mid // a + mid // b + mid // c
                - mid // lcm_ab - mid // lcm_bc - mid // lcm_ac  # Remove double counted
                + mid // lcm_abc)  # Add back triple counted
        
        # If we have at least n ugly numbers <= mid, search in left half
        if count >= n:
            right = mid
        else:
            # Otherwise, search in right half
            left = mid + 1
    
    return left
    # Time: O(log m), where m = 2 × 10⁹
    # Space: O(1)


def main():
    result = nth_ugly_number(n = 3, a = 2, b = 3, c = 5)
    print(result) # 4

    result = nth_ugly_number(n = 4, a = 2, b = 3, c = 4)
    print(result) # 6

    result = nth_ugly_number(n = 5, a = 2, b = 11, c = 13)
    print(result) # 10

if __name__ == "__main__":
    main()
