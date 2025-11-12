# --------------------------------------------
# 1684. Count the Number of Consistent Strings
# --------------------------------------------

# Problem: https://leetcode.com/problems/count-the-number-of-consistent-strings
#
# You are given a string allowed consisting of distinct characters and an array of
# strings words. A string is consistent if all characters in the string appear in
# the string allowed.
# 
# Return the number of consistent strings in the array words.
# 
# Example 1:
# 
# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# 
# Explanation: Strings "aaab" and "baa" are consistent since they only contain
# characters 'a' and 'b'.
# 
# Example 2:
# 
# Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# 
# Explanation: All strings are consistent.
# 
# Example 3:
# 
# Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# Output: 4
# 
# Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
# 
# 
# Constraints:
#         1 <= words.length <= 10^4
#         1 <= allowed.length <= 26
#         1 <= words[i].length <= 10
#         The characters in allowed are distinct.
#         words[i] and allowed contain only lowercase English letters.


# Solution: https://youtu.be/CFa2TgIHMN0
# Credit: Navdeep Singh founder of NeetCode
def count_consistent_strings(allowed, words):
    allowed = set(allowed)
    
    res = len(words)
    for w in words:
        for c in w:
            if c not in allowed:
                res -= 1
                break
    
    return res
    # Time: O(l + n * m),  l = len of allowed, n = number of words, m = max len of a word
    # Space: O(l)

# Alternative solution
def count_consistent_strings_alt(allowed, words):
    bit_mask = 0
    for c in allowed:
        bit = 1 << (ord(c) - ord('a'))
        bit_mask = bit_mask | bit

    res = len(words)
    for w in words:
        for c in w:
            bit = 1 << (ord(c) - ord('a'))
            if bit & bit_mask == 0:
                res -= 1
                break

    return res
    # Time: O(l + n * m),  l = len of allowed, n = number of words, m = max len of a word
    # Space: O(1)


def main():
    result = count_consistent_strings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"])
    print(result) # 2

    result = count_consistent_strings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"])
    print(result) # 7

    result = count_consistent_strings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"])
    print(result) # 4

if __name__ == "__main__":
    main()
