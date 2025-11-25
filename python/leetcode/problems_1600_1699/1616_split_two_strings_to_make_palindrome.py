# ------------------------------------------
# 1616. Split Two Strings to Make Palindrome
# ------------------------------------------

# Problem: https://leetcode.com/problems/split-two-strings-to-make-palindrome
#
# You are given two strings a and b of the same length. Choose an index and split
# both strings at the same index, splitting a into two strings: aprefix and
# asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix
# and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix +
# asuffix forms a palindrome.
# 
# When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is
# allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc",
# "ab" + "c" , and "abc" + "" are valid splits.
# 
# Return true if it is possible to form a palindrome string, otherwise return
# false.
# 
# Notice that x + y denotes the concatenation of strings x and y.
# 
# Example 1:
# 
# Input: a = "x", b = "y"
# Output: true
# 
# Explaination: If either a or b are palindromes the answer is true since you can
# split in the following way:
# aprefix = "", asuffix = "x"
# bprefix = "", bsuffix = "y"
# Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.
# 
# Example 2:
# 
# Input: a = "xbdef", b = "xecab"
# Output: false
# 
# Example 3:
# 
# Input: a = "ulacfd", b = "jizalu"
# Output: true
# 
# Explaination: Split them at index 3:
# aprefix = "ula", asuffix = "cfd"
# bprefix = "jiz", bsuffix = "alu"
# Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.
# 
# 
# Constraints:
#         1 <= a.length, b.length <= 10⁵
#         a.length == b.length
#         a and b consist of lowercase English letters


# Solution: https://algo.monster/liteproblems/1616
# Credit: AlgoMonster
def check_palindrome_formation(a, b):
    
    def can_form_palindrome_with_split(string1, string2):
        left = 0
        right = len(string2) - 1
        
        # Match characters from outside moving inward
        # string1[left] should equal string2[right] for palindrome
        while left < right and string1[left] == string2[right]:
            left += 1
            right -= 1
        
        # If pointers crossed, we already have a palindrome
        # Otherwise, check if remaining middle part is palindrome in either string
        return (left >= right or 
                is_palindrome(string1, left, right) or 
                is_palindrome(string2, left, right))
    
    def is_palindrome(string, left, right):
        substring = string[left:right + 1]
        return substring == substring[::-1]
    
    # Try both combinations: (prefix_a + suffix_b) and (prefix_b + suffix_a)
    return can_form_palindrome_with_split(a, b) or can_form_palindrome_with_split(b, a)
    # Time: O(n)
    # Space: O(n)


def main():
    result = check_palindrome_formation(a = "x", b = "y")
    print(result) # True

    result = check_palindrome_formation(a = "xbdef", b = "xecab")
    print(result) # False

    result = check_palindrome_formation(a = "ulacfd", b = "jizalu")
    print(result) # True

if __name__ == "__main__":
    main()
