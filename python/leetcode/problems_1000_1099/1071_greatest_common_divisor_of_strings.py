# ----------------------------------------
# 1071. Greatest Common Divisor of Strings
# ----------------------------------------

# Problem: https://leetcode.com/problems/greatest-common-divisor-of-strings
#
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ...
# + t + t (i.e., t is concatenated with itself one or more times).
# 
# Given two strings str1 and str2, return the largest string x such that x divides
# both str1 and str2.
# 
# Example 1:
# 
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# 
# Example 2:
# 
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# 
# Example 3:
# 
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
# 
# 
# Constraints:
#         1 <= str1.length, str2.length <= 1000
#         str1 and str2 consist of English uppercase letters.


# Solution: https://youtu.be/i5I_wrbUdzM
# Credit: Navdeep Singh founder of NeetCode
def gcd_of_strings(str1, str2):
    len1, len2 = len(str1), len(str2)

    def isDivisor(l):
        if len1 % l or len2 % l:
            return False
        f1, f2 = len1 // l, len2 // l
        return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

    for l in range(min(len1, len2), 0, -1):
        if isDivisor(l):
            return str1[:l]

    return ""
    # Time: O(min(m, n) * (n + m))


def main():
    result = gcd_of_strings(str1 = "ABCABC", str2 = "ABC")
    print(result) # "ABC"

    result = gcd_of_strings(str1 = "ABABAB", str2 = "ABAB")
    print(result) # "AB"

    result = gcd_of_strings(str1 = "LEET", str2 = "CODE")
    print(result) # ""

if __name__ == "__main__":
    main()
