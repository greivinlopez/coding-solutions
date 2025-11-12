# ---------------------------------------------
# 1318. Minimum Flips to Make a OR b Equal to c
# ---------------------------------------------

# Problem: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c
#
# Given 3 positives numbers a, b and c. Return the minimum flips required in some
# bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# 
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to
# 1 in their binary representation.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/01/06/sample_3_1676.png
# 
# Input: a = 2, b = 6, c = 5
# Output: 3
# 
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
# 
# Example 2:
# 
# Input: a = 4, b = 2, c = 7
# Output: 1
# 
# Example 3:
# 
# Input: a = 1, b = 2, c = 3
# Output: 0
# 
# 
# Constraints:
#         1 <= a <= 10^9
#         1 <= b <= 10^9
#         1 <= c <= 10^9


# Solution: https://algo.monster/liteproblems/1318
# Credit: AlgoMonster
def min_flips(a, b, c):
    flip_count = 0
    
    # Check each bit position (32-bit integers)
    for bit_position in range(32):
        # Extract the i-th bit from each number
        bit_a = (a >> bit_position) & 1
        bit_b = (b >> bit_position) & 1
        bit_c = (c >> bit_position) & 1
        
        # Calculate flips needed for current bit position
        if bit_c == 0:
            # If target bit is 0, both a and b bits must be 0
            # Count how many 1s need to be flipped to 0
            flip_count += bit_a + bit_b
        else:
            # If target bit is 1, at least one of a or b must be 1
            # Only flip if both are 0
            flip_count += int(bit_a == 0 and bit_b == 0)
    
    return flip_count
    # Time: O(log m)
    # Space: O(1)
    # m = the maximum value among the numbers a, b, and c.


def main():
    result = min_flips(a = 2, b = 6, c = 5)
    print(result) # 3

    result = min_flips(a = 4, b = 2, c = 7)
    print(result) # 1

    result = min_flips(a = 1, b = 2, c = 3)
    print(result) # 0

if __name__ == "__main__":
    main()
