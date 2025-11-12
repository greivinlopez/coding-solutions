# -------------------------------------------------------------
# 1456. Maximum Number Of Vowels In A Substring Of Given Length
# -------------------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
#
# Given a string s and an integer k, return the maximum number of vowel letters in
# any substring of s with length k.
# 
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
# 
# Example 1:
# 
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# 
# Example 2:
# 
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# 
# Example 3:
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
# 
# 
# Constraints:
#         1 <= s.length <= 10^5
#         s consists of lowercase English letters.
#         1 <= k <= s.length


# Solution: https://youtu.be/kEfPSzgL-Ss
# Credit: Navdeep Singh founder of NeetCode
def max_vowels(s, k):
    l, res, total = 0, 0, 0
    vowels = "aeiou"

    for r in range(len(s)):
        if s[r] in vowels:
            total += 1
        if (r - l + 1) > k:
            if s[l] in vowels:
                total -= 1
            l += 1
        res = max(res, total)
    return res


def main():
    result = max_vowels(s = "abciiidef", k = 3)
    print(result) # 3

    result = max_vowels(s = "aeiou", k = 2)
    print(result) # 2

    result = max_vowels(s = "leetcode", k = 3)
    print(result) # 2

if __name__ == "__main__":
    main()
