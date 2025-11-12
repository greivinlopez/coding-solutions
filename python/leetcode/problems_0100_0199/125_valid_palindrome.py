# ----------------------
# 125. Valid Palindrome
# ----------------------

# Problem: https://leetcode.com/problems/valid-palindrome/
# 
# A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, it reads 
# the same forward and backward. Alphanumeric characters include letters 
# and numbers.
# 
# Given a string s, return true if it is a palindrome, or false otherwise.

# Solution: https://youtu.be/jJXJ16kPFWg
# Credit: Navdeep Singh founder of NeetCode
def is_palindrome(s):
    # Time: O(n)
    # Space: O(1)
    new = ''
    for a in s:
        if a.isalpha() or a.isdigit():
            new += a.lower()
    return (new == new[::-1])

# Solution: https://youtu.be/Nxzstmv_U0U
# Credit: Greg Hogg
def is_palindrome_alt(s):
    # Time: O(n)
    # Space: O(1)
    n = len(s)
    L = 0
    R = n - 1

    while L < R:
        if not s[L].isalnum():
            L += 1
            continue

        if not s[R].isalnum():
            R -= 1
            continue

        if s[L].lower() != s[R].lower():
            return False

        L += 1
        R -= 1

    return True

def main():
    result = is_palindrome("A man, a plan, a canal: Panama")
    print(result) # True

    result = is_palindrome("race a car")
    print(result) # False

    result = is_palindrome(" ")
    print(result) # True

if __name__ == "__main__":
    main()