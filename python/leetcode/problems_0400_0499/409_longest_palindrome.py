# -----------------------
# 409. Longest Palindrome
# -----------------------

# Problem: https://leetcode.com/problems/longest-palindrome/
# 
# Given a string s which consists of lowercase or uppercase letters, return the 
# length of the longest palindrome that can be built with those letters.
# 
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.
# 
#  
# Example 1:
# 
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# Example 2:
# 
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
#  
# 
# Constraints:
# 
#   1 <= s.length <= 2000
#   s consists of lowercase and/or uppercase English letters only.


# Solution: https://youtu.be/_g9jrLuAphs
# Credit: Navdeep Singh founder of NeetCode
def longest_palindrome(s):
    seen = set()
    res = 0
    for c in s:
        if c in seen:
            seen.remove(c)
            res += 2
        else:
            seen.add(c)
    return res + 1 if seen else res


def main():
    result = longest_palindrome("abccccdd")
    print(result) # 7

    result = longest_palindrome("a")
    print(result) # 1

if __name__ == "__main__":
    main()
