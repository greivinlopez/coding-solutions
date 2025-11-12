# ---------------------
# 191. Number Of 1 Bits
# ---------------------

# Problem: https://leetcode.com/problems/number-of-1-bits/
# 
# Given a positive integer n, write a function that returns the number of set 
# bits in its binary representation (also known as the Hamming weight). 
#  
# Example 1:
# 
# Input: n = 11
# Output: 3
# 
# Explanation:
# The input binary string 1011 has a total of three set bits.
# 
# Example 2:
# 
# Input: n = 128
# Output: 1
# 
# Explanation:
# The input binary string 10000000 has a total of one set bit.
# 
# Example 3:
# 
# Input: n = 2147483645
# Output: 30
# 
# Explanation:
# 
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
# 
# 
# Constraints:
# 
# 	1 <= n <= 2^31 - 1
# 
# 
# Follow up: If this function is called many times, how would you optimize it?


# Solution: https://youtu.be/5Km3utixwZs
# Credit: Navdeep Singh founder of NeetCode
def hamming_weight(n):
    res = 0
    while n:
        n &= n - 1
        res += 1
    return res
    # Time: O(log(n))
    # Space: O(1)


# Solution: https://youtu.be/1JfdvPk-iHg
# Credit: Greg Hogg
# Almost the same solution


# Credit: Jeel Gajera -> https://github.com/JeelGajera
def hamming_weight_alt(n):
    s = str(bin(n))
    bits = list(s)
    return bits.count('1')
    # Time: O(log(n))
    # Space: O(log(n))


def main():
    result = hamming_weight(11)
    print(result) # 3

    result = hamming_weight(128)
    print(result) # 1

    result = hamming_weight(2147483645)
    print(result) # 30

if __name__ == "__main__":
    main()
