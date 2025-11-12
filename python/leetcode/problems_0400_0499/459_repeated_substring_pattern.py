# -------------------------------
# 459. Repeated Substring Pattern
# -------------------------------

# Problem: https://leetcode.com/problems/repeated-substring-pattern/
# 
# Given a string s, check if it can be constructed by taking a substring of it 
# and appending multiple copies of the substring together.
# 
#  
# Example 1:
# 
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# 
# 
# Example 2:
# 
# Input: s = "aba"
# Output: false
# 
# 
# Example 3:
# 
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
# 
# 
# Constraints:
# 
# 	1 <= s.length <= 10^4
# 	s consists of lowercase English letters.


# Solution: No video found
# Credit: Navdeep Singh founder of NeetCode
def repeated_substring_pattern(s):
    return s in (s + s)[1:-1]


def main():
    result = repeated_substring_pattern("abab")
    print(result) # True

    result = repeated_substring_pattern("aba")
    print(result) # False

    result = repeated_substring_pattern("abcabcabcabc")
    print(result) # True

if __name__ == "__main__":
    main()
