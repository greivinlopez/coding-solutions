# -------------------------------------------------------------------
# 1888. Minimum Number Of Flips To Make The Binary String Alternating
# -------------------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating
#
# You are given a binary string s. You are allowed to perform two types of
# operations on the string in any sequence:
# 
#   * Type-1: Remove the character at the start of the string s and append it
#     to the end of the string.
# 
#   * Type-2: Pick any character in s and flip its value, i.e., if its value
#     is '0' it becomes '1' and vice-versa.
# 
# Return the minimum number of type-2 operations you need to perform such that s
# becomes alternating.
# 
# The string is called alternating if no two adjacent characters are equal.
#  
#   * For example, the strings "010" and "1010" are alternating, while the
#     string "0100" is not.
# 
# Example 1:
# 
# Input: s = "111000"
# Output: 2
# Explanation: Use the first operation two times to make s = "100011".
# Then, use the second operation on the third and sixth elements to make s =
# "101010".
# 
# Example 2:
# 
# Input: s = "010"
# Output: 0
# Explanation: The string is already alternating.
# 
# Example 3:
# 
# Input: s = "1110"
# Output: 1
# Explanation: Use the second operation on the second element to make s = "1010".
# 
# 
# Constraints:
#         1 <= s.length <= 10^5
#         s[i] is either '0' or '1'.


# Solution: https://youtu.be/MOeuK6gaC2A
# Credit: Navdeep Singh founder of NeetCode
def min_flips(s):
    n = len(s)
    s = s + s
    alt1, alt2 = "", ""

    for i in range(len(s)):
        alt1 += "0" if i % 2 == 0 else "1"
        alt2 += "1" if i % 2 == 0 else "0"

    res = float('inf')
    diff1, diff2 = 0, 0
    l = 0
    for r in range(len(s)):
        if s[r] != alt1[r]:
            diff1 += 1
        if s[r] != alt2[r]:
            diff2 += 1
        if (r - l + 1) > n:
            if s[l] != alt1[l]:
                diff1 -= 1
            if s[l] != alt2[l]:
                diff2 -= 1
            l += 1
        if (r - l + 1) == n:
            res = min(res, diff1, diff2)
    return res


def main():
    result = min_flips("111000")
    print(result) # 2

    result = min_flips("010")
    print(result) # 0

    result = min_flips("1110")
    print(result) # 1

if __name__ == "__main__":
    main()
