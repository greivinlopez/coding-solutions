# -----------------------
# 878. Nth Magical Number
# -----------------------

# Problem: https://leetcode.com/problems/nth-magical-number
#
# A positive integer is magical if it is divisible by either a or b.
# 
# Given the three integers n, a, and b, return the nᵗʰ magical number. Since the
# answer may be very large, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: n = 1, a = 2, b = 3
# Output: 2
# 
# Example 2:
# 
# Input: n = 4, a = 2, b = 3
# Output: 6
# 
# 
# Constraints:
#         1 <= n <= 10⁹
#         2 <= a, b <= 4 * 10⁴

import math

# Solution: https://leetcode.com/problems/nth-magical-number/solutions/6608617/inclusion-exclusion-easy-python-soln
# Credit: Vishal Gunawad -> https://leetcode.com/u/vishalgunawad/
# Note: not explination of the solution here
def nth_magical_number(n, a, b):
    mod = 10**9 + 7

    lcm = math.lcm(a, b)
    l = min(a, b)
    r = n * min(a, b)


    while l < r:

        m = l + r >> 1

        aa = m//a
        bb = m//b
        ab = m//lcm

            
        if n <= (aa + bb - ab): # a U b = a + b - ab   inclusion exclusion
            r = m
        else:
            l = m + 1
    
    return l % mod
    # Time: O(log(n * min(a,b)))
    # Space: O(1)

# Alternative Solution: using bisect_left
# Solution: https://algo.monster/liteproblems/878
# Credit: AlgoMonster
# Will only work for Python 3.10+
def nth_magical_number_alt(n, a, b):
    from bisect import bisect_left

    # Define the modulo constant for the result
    MOD = 10**9 + 7
    
    # Calculate the least common multiple of a and b
    # This helps avoid double-counting numbers divisible by both a and b
    lcm_value = (a * b) // math.gcd(a, b)
    
    # Set an upper bound for binary search
    # The nth magical number won't exceed n * min(a, b), but we use a safer upper bound
    upper_bound = (a + b) * n
    
    # Binary search to find the nth magical number
    # The key function counts how many magical numbers are <= x
    # Formula: numbers divisible by a + numbers divisible by b - numbers divisible by both
    result = bisect_left(
        range(upper_bound), 
        x=n, 
        key=lambda x: x // a + x // b - x // lcm_value
    )
    
    # Return the result modulo 10^9 + 7
    return result % MOD
    # Time: O(log(n * max(a,b)))
    # Space: O(1)


def main():
    result = nth_magical_number(n = 1, a = 2, b = 3)
    print(result) # 2

    result = nth_magical_number(n = 4, a = 2, b = 3)
    print(result) # 6

if __name__ == "__main__":
    main()
