# ---------------------------------
# 201. Bitwise And Of Numbers Range
# ---------------------------------

# Problem: https://leetcode.com/problems/bitwise-and-of-numbers-range/
# 
# Given two integers left and right that represent the range [left, right], 
# return the bitwise AND of all numbers in this range, inclusive.
# 
#  
# Example 1:
# 
# Input: left = 5, right = 7
# Output: 4
# 
# 
# Example 2:
# 
# Input: left = 0, right = 0
# Output: 0
# 
# 
# Example 3:
# 
# Input: left = 1, right = 2147483647
# Output: 0
# 
# 
# Constraints:
# 
# 	0 <= left <= right <= 231 - 1


# Solution: https://youtu.be/R3T0olAhUq0
# Credit: Navdeep Singh founder of NeetCode
def range_bitwise_and(left, right):
    # check difference at each bit (cannot be more than left - right)
    res = 0

    for i in range(32):
        bit = (left >> i) & 1
        if not bit:
            continue
        
        remain = left % (1 << (i + 1))
        diff = (1 << (i + 1)) - remain
        if right - left < diff:
            res = res | (1 << i)
    return res

def range_bitwise_and_alt(left, right):
    # find the longest matching prefix of set bits between left and right
    i = 0
    while left != right:
        left = left >> 1
        right = right >> 1
        i += 1
    return left << i

# Solution: https://www.youtube.com/shorts/hYcWu5gXGpU
# Credit: Greg Hogg
def range_bitwise_and_alt_2(m, n):
    # Time: O(Bits)
    # Space: O(1)
    shift = 0
    
    while m < n:
        m = m >> 1
        n = n >> 1
        shift += 1

    return m << shift

def main():
    result = range_bitwise_and_alt_2(5, 7)
    print(result) # 4

    result = range_bitwise_and_alt_2(0, 0)
    print(result) # 0

    result = range_bitwise_and_alt_2(1, 2147483647)
    print(result) # 0

if __name__ == "__main__":
    main()
