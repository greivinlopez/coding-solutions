# ------------------
# 3174. Clear Digits
# ------------------

# Problem: https://leetcode.com/problems/clear-digits
#
# You are given a string s.
# 
# Your task is to remove all digits by doing this operation repeatedly:
#         
#   * Delete the first digit and the closest non-digit character to its left.
# 
# Return the resulting string after removing all digits.
# 
# Note that the operation cannot be performed on a digit that does not have any
# non-digit character to its left.
# 
# Example 1:
# 
# Input: s = "abc"
# Output: "abc"
# 
# Explanation:
# There is no digit in the string.
# 
# Example 2:
# 
# Input: s = "cb34"
# Output: ""
# 
# Explanation:
# First, we apply the operation on s[2], and s becomes "c4".
# Then we apply the operation on s[1], and s becomes "".
# 
# 
# Constraints:
#         1 <= s.length <= 100
#         s consists only of lowercase English letters and digits.
#         The input is generated such that it is possible to delete all digits.


# Solution: https://youtu.be/f_u_9ixrktQ
# Credit: Navdeep Singh founder of NeetCode
def clear_digits(s):
    res = []

    def is_digit(c):
        return "0" <= c <= "9"

    for i in range(len(s)):
        if is_digit(s[i]):
            if res:  # Ensure the list is not empty before popping
                res.pop()
        else:
            res.append(s[i])

    return "".join(res)
    # Time: O(n) 
    # Space: O(n)


def main():
    result = clear_digits("abc")
    print(result) # "abc"

    result = clear_digits("cb34")
    print(result) # ""

if __name__ == "__main__":
    main()
