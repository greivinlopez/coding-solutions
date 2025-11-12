# ----------------------------------------------------------
# 1750. Minimum Length Of String After Deleting Similar Ends
# ----------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends
#
# Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked
# to apply the following algorithm on the string any number of times:
# 
#  1. Pick a non-empty prefix from the string s where all the characters in
# the prefix are equal.
#  2. Pick a non-empty suffix from the string s where all the characters in
# this suffix are equal.
#  3. The prefix and the suffix should not intersect at any index.
#  4. The characters from the prefix and suffix must be the same.
#  5. Delete both the prefix and the suffix.
# 
# Return the minimum length of s after performing the above operation any number
# of times (possibly zero times).
# 
# 
# Example 1:
# 
# Input: s = "ca"
# Output: 2
# Explanation: You can't remove any characters, so the string stays as is.
# 
# Example 2:
# 
# Input: s = "cabaabac"
# Output: 0
# Explanation: An optimal sequence of operations is:
# - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
# - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
# - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
# - Take prefix = "a" and suffix = "a" and remove them, s = "".
# 
# Example 3:
# 
# Input: s = "aabccabba"
# Output: 3
# Explanation: An optimal sequence of operations is:
# - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
# - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
# 
# 
# Constraints:
#         1 <= s.length <= 10^5
#         s only consists of characters 'a', 'b', and 'c'.


# Solution: https://youtu.be/318hrWVr_5U
# Credit: Navdeep Singh founder of NeetCode
def minimum_length(s):
    l, r = 0, len(s) - 1

    while l < r and s[l] == s[r]:
        tmp = s[l]
        while l <= r and s[l] == tmp:
            l += 1
        while l <= r and s[r] == tmp:
            r -= 1
    return (r - l + 1)


def main():
    result = minimum_length("ca")
    print(result) # 2

    result = minimum_length("cabaabac")
    print(result) # 0

    result = minimum_length("aabccabba")
    print(result) # 3

if __name__ == "__main__":
    main()
