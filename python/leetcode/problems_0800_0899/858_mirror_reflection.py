# ----------------------
# 858. Mirror Reflection
# ----------------------

# Problem: https://leetcode.com/problems/mirror-reflection
#
# There is a special square room with mirrors on each of the four walls. Except
# for the southwest corner, there are receptors on each of the remaining corners,
# numbered 0, 1, and 2.
# 
# The square room has walls of length p and a laser ray from the southwest corner
# first meets the east wall at a distance q from the 0ᵗʰ receptor.
# 
# Given the two integers p and q, return the number of the receptor that the ray
# meets first.
# 
# The test cases are guaranteed so that the ray will meet a receptor eventually.
# 
# Example 1:
# 
# Input: p = 2, q = 1
# Output: 2
# 
# Explanation: The ray meets receptor 2 the first time it gets reflected back to
# the left wall.
# 
# Example 2:
# 
# Input: p = 3, q = 1
# Output: 1
# 
# 
# Constraints:
#         1 <= q <= p <= 1000

from math import gcd

# Solution: https://algo.monster/liteproblems/858
# Credit: AlgoMonster
def mirror_reflection(p, q):
    # Find the greatest common divisor of p and q
    # This helps reduce the problem to its simplest form
    g = gcd(p, q)
    
    # Reduce p and q by their GCD and check if they're odd or even
    # We only need the parity (odd/even) of the reduced values
    p_parity = (p // g) % 2  # 1 if odd, 0 if even
    q_parity = (q // g) % 2  # 1 if odd, 0 if even
    
    # Determine which receptor the laser hits based on parity
    # If both reduced p and q are odd, laser hits receptor 1
    if p_parity == 1 and q_parity == 1:
        return 1
    
    # If reduced p is odd and q is even, laser hits receptor 0
    # If reduced p is even, laser hits receptor 2
    return 0 if p_parity == 1 else 2
    # Time: O(log(min(p, q)))
    # Space: O(1)


def main():
    result = mirror_reflection(p = 2, q = 1)
    print(result) # 2

    result = mirror_reflection(p = 3, q = 1)
    print(result) # 1

if __name__ == "__main__":
    main()
