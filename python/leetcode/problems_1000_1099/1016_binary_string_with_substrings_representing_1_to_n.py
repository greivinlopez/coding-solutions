# -------------------------------------------------------
# 1016. Binary String With Substrings Representing 1 To N
# -------------------------------------------------------

# Problem: https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n
#
# Given a binary string s and a positive integer n, return true if the binary
# representation of all the integers in the range [1, n] are substrings of s, or
# false otherwise.
# 
# A substring is a contiguous sequence of characters within a string.
# 
# Example 1:
# 
# Input: s = "0110", n = 3
# Output: true
# 
# Example 2:
# 
# Input: s = "0110", n = 4
# Output: false
# 
# 
# Constraints:
#         1 <= s.length <= 1000
#         s[i] is either '0' or '1'.
#         1 <= n <= 10⁹


# Solution: https://algo.monster/liteproblems/1016
# Credit: AlgoMonster
def query_string(s, n):
    # Early termination: if n > 1000, the string cannot contain all binary representations
    # This is based on the constraint that string length is limited
    if n > 1000:
        return False
    
    # Check if all binary representations from (n//2 + 1) to n exist as substrings in s
    # We only need to check the upper half because:
    # - If all numbers from (n//2 + 1) to n are present as binary substrings
    # - Then all numbers from 1 to n//2 are also present (they appear as prefixes)
    for i in range(n, n // 2, -1):
        # Convert number to binary (remove '0b' prefix)
        binary_representation = bin(i)[2:]
        
        # Check if this binary string exists as a substring in s
        if binary_representation not in s:
            return False
    
    return True
    # Time: O(n * m)
    # Space: O(log(n))


def main():
    result = query_string(s = "0110", n = 3)
    print(result) # True

    result = query_string(s = "0110", n = 4)
    print(result) # False

if __name__ == "__main__":
    main()
