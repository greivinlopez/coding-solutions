# --------------------
# 9. Palindrome Number
# --------------------

# Problem: https://leetcode.com/problems/palindrome-number
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
# 
# Example 1:
# 
# Input: x = 121
# Output: true
# 
# Explanation: 121 reads as 121 from left to right and from right to left.
# 
# Example 2:
# 
# Input: x = -121
# Output: false
# 
# Explanation: From left to right, it reads -121. From right to left, it becomes
# 121-. Therefore it is not a palindrome.
# 
# Example 3:
# 
# Input: x = 10
# Output: false
# 
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Constraints:
#         -2³¹ <= x <= 2³¹ - 1
# 
# Follow up: Could you solve it without converting the integer to a string?

# Solution: https://youtu.be/yubRKwixN-U
# Credit: Navdeep Singh founder of NeetCode 
def is_palindrome(x):
    if x < 0: return False
    
    div = 1
    while x >= 10 * div:
        div *= 10
        
    while x:
        right = x % 10
        left = x // div
        
        if left != right: return False
        
        x = (x % div) // 10
        div = div / 100
    return True
    # Time: O(log(x))
    # Space: O(1)

# Reversing the number and compare:
def is_palindrome_alt(x):
    ra = 0
    temp = x
    if x < 0:
        return False
    while (x > 0):
        ra = ra * 10 + x % 10
        x = x // 10
    return temp == ra
    # Time: O(log(x))
    # Space: O(1)

# One liner -> against the follow up
def is_palindrome_short(x):
    return str(x) == str(x)[::-1]


def main():
    result = is_palindrome(121) # True
    print(result)
    result = is_palindrome(-121) # False
    print(result)
    result = is_palindrome(10) # False
    print(result)
    result = is_palindrome(200002) # True
    print(result)

if __name__ == "__main__":
    main()