# --------------------
# 942. DI String Match
# --------------------

# Problem: https://leetcode.com/problems/di-string-match
#
# A permutation perm of n + 1 integers of all the integers in the range [0, n] can
# be represented as a string s of length n where:
#         
#   * s[i] == 'I' if perm[i] < perm[i + 1], and
#   * s[i] == 'D' if perm[i] > perm[i + 1].
# 
# Given a string s, reconstruct the permutation perm and return it. If there are
# multiple valid permutations perm, return any of them.
# 
# Example 1:
# 
# Input: s = "IDID"
# Output: [0,4,1,3,2]
# 
# Example 2:
# 
# Input: s = "III"
# Output: [0,1,2,3]
# 
# Example 3:
# 
# Input: s = "DDI"
# Output: [3,2,0,1]
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s[i] is either 'I' or 'D'.


# Solution: https://algo.monster/liteproblems/942
# Credit: AlgoMonster
def di_string_match(s):
    # Initialize pointers for smallest and largest available numbers
    low_pointer = 0
    high_pointer = len(s)
    
    # Result array to store the permutation
    result = []
    
    # Process each character in the string
    for char in s:
        if char == "I":
            # For increase, use the smallest available number
            result.append(low_pointer)
            low_pointer += 1
        else:  # char == "D"
            # For decrease, use the largest available number
            result.append(high_pointer)
            high_pointer -= 1
    
    # Add the last remaining number (low_pointer and high_pointer converge to same value)
    result.append(low_pointer)
    
    return result
    # Time: O(n)
    # Space: O(n)


def main():
    result = di_string_match(s = "IDID")
    print(result) # [0, 4, 1, 3, 2]

    result = di_string_match(s = "III")
    print(result) # [0, 1, 2, 3]

    result = di_string_match(s = "DDI")
    print(result) # [3, 2, 0, 1]

if __name__ == "__main__":
    main()
