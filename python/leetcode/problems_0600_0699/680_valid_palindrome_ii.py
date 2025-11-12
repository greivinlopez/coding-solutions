# ------------------------
# 680. Valid Palindrome II
# ------------------------

# Problem: https://leetcode.com/problems/valid-palindrome-ii/
# 
# Given a string s, return true if the s can be palindrome after deleting at 
# most one character from it.
# 
#  
# Example 1:
# 
# Input: s = "aba"
# Output: true
# 
# 
# Example 2:
# 
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# 
# 
# Example 3:
# 
# Input: s = "abc"
# Output: false
# 
#  
# Constraints:
# 
# 	1 <= s.length <= 10^5
# 	s consists of lowercase English letters.


# Solution: https://youtu.be/JrxRYBwG6EI
# Credit: Navdeep Singh founder of NeetCode
def valid_palindrome(s):
    i, j = 0, len(s) - 1
    
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return valid_palindrome_util(s, i + 1, j) or valid_palindrome_util(s, i, j - 1)
    return True
    
def valid_palindrome_util(s, i, j):
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    
    return True


def main():
    result = valid_palindrome("aba")
    print(result) # True

    result = valid_palindrome("abca")
    print(result) # True

    result = valid_palindrome("abc")
    print(result) # False

if __name__ == "__main__":
    main()
