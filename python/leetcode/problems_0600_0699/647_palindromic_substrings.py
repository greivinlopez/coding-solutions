# ---------------------------
# 647. Palindromic Substrings
# ---------------------------

# Problem: https://leetcode.com/problems/palindromic-substrings/
# 
# Given a string s, return the number of palindromic substrings in it.
# 
# A string is a palindrome when it reads the same backward as forward.
# 
# A substring is a contiguous sequence of characters within the string.
# 
#  
# Example 1:
# 
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# Example 2:
# 
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# Constraints:
# 
# 	1 <= s.length <= 1000
# 	s consists of lowercase English letters.


# Solution: https://youtu.be/4RACzI5-du8
# Credit: Navdeep Singh founder of NeetCode
def count_substrings(s):
    def count_pali(s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

    res = 0

    for i in range(len(s)):
        res += count_pali(s, i, i)
        res += count_pali(s, i, i + 1)
    return res
    # Time: O(n^2)
    # Space: O(n^2)


def main():
    result = count_substrings("abc")
    print(result) # 3

    result = count_substrings("aaa")
    print(result) # 6

if __name__ == "__main__":
    main()
