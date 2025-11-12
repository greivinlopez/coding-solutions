# --------------------------------------------------------------------
# 3306. Count of Substrings Containing Every Vowel and K Consonants II
# --------------------------------------------------------------------

# Problem: https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii
#
# You are given a string word and a non-negative integer k.
# 
# Return the total number of substrings of word that contain every vowel ('a',
# 'e', 'i', 'o', and 'u') at least once and exactly k consonants.
# 
# Example 1:
# 
# Input: word = "aeioqq", k = 1
# Output: 0
# 
# Explanation:
# There is no substring with every vowel.
# 
# Example 2:
# 
# Input: word = "aeiou", k = 0
# Output: 1
# 
# Explanation:
# The only substring with every vowel and zero consonants is word[0..4], which is
# "aeiou".
# 
# Example 3:
# 
# Input: word = "ieaouqqieaouqq", k = 1
# Output: 3
# 
# Explanation:
# The substrings with every vowel and one consonant are:
#         word[0..5], which is "ieaouq".
#         word[6..11], which is "qieaou".
#         word[7..12], which is "ieaouq".
# 
# 
# Constraints:
#         5 <= word.length <= 2 * 10^5
#         word consists only of lowercase English letters.
#         0 <= k <= word.length - 5

from collections import defaultdict

# Solution: https://youtu.be/2wANakxRZNo
# Credit: Navdeep Singh founder of NeetCode
def count_of_substrings(word, k):
    def at_least_k(k_val):
        vowel = defaultdict(int)
        non_vowel = 0
        res = 0
        l = 0
        for r in range(len(word)):
            if word[r] in "aeiou":
                vowel[word[r]] += 1
            else:
                non_vowel += 1
            
            while len(vowel) == 5 and non_vowel >= k_val:
                res += (len(word) - r)
                if word[l] in "aeiou":
                    vowel[word[l]] -= 1
                    if vowel[word[l]] == 0:
                        vowel.pop(word[l])
                else:
                    non_vowel -= 1
                l += 1
        return res

    return at_least_k(k) - at_least_k(k + 1)
    # Time: O(n) 
    # Space: O(1)


def main():
    result = count_of_substrings(word = "aeioqq", k = 1)
    print(result) # 0

    result = count_of_substrings(word = "aeiou", k = 0)
    print(result) # 1

    result = count_of_substrings(word = "ieaouqqieaouqq", k = 1)
    print(result) # 3

if __name__ == "__main__":
    main()
