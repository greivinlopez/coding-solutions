# ----------------------------------
# 2390. Removing Stars From A String
# ----------------------------------

# Problem: https://leetcode.com/problems/removing-stars-from-a-string
#
# You are given a string s, which contains stars *.
# 
# In one operation, you can:
#         Choose a star in s.
#         Remove the closest non-star character to its left, as well as remove the
# star itself.
# 
# Return the string after all stars have been removed.
# 
# Note:
#         The input will be generated such that the operation is always possible.
#         It can be shown that the resulting string will always be unique.
# 
# Example 1:
# 
# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes
# "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes
# "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".
# 
# Example 2:
# 
# Input: s = "erase*****"
# Output: ""
# Explanation: The entire string is removed, so we return an empty string.
# 
# 
# Constraints:
#         1 <= s.length <= 10^5
#         s consists of lowercase English letters and stars *.
#         The operation above can be performed on s.


# Solution: https://youtu.be/pRyFZIaKegA
# Credit: Navdeep Singh founder of NeetCode
def remove_stars(s):
    res = []
    for c in s :
        if res and c == '*':
            res.pop()
        else:
            res.append(c)
    return ''.join(res)


def main():
    result = remove_stars("leet**cod*e")
    print(result) # "lecoe"

    result = remove_stars("erase*****")
    print(result) # ""

if __name__ == "__main__":
    main()
