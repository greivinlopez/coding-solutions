# ----------------------------------------
# 1657. Determine if Two Strings Are Close
# ----------------------------------------

# Problem: https://leetcode.com/problems/determine-if-two-strings-are-close
#
# Two strings are considered close if you can attain one from the other using the
# following operations:
#         
#   * Operation 1: Swap any two existing characters.
#       * For example, abcde -> aecdb      
#   * Operation 2: Transform every occurrence of one existing character into
#     another existing character, and do the same with the other character.
#       * For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn 
#         into a's)
# 
# You can use the operations on either string as many times as necessary.
# 
# Given two strings, word1 and word2, return true if word1 and word2 are close,
# and false otherwise.
# 
# Example 1:
# 
# Input: word1 = "abc", word2 = "bca"
# Output: true
# 
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
# 
# Example 2:
# 
# Input: word1 = "a", word2 = "aa"
# Output: false
# 
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any
# number of operations.
# 
# Example 3:
# 
# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# 
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"
# 
# 
# Constraints:
#         1 <= word1.length, word2.length <= 10⁵
#         word1 and word2 contain only lowercase English letters.

from collections import Counter

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def close_strings(word1, word2):
    f1 = Counter(word1)
    f2 = Counter(word2)
    char1 = set(word1)
    char2 = set(word2)
    return (char1 == char2) and (sorted(f1.values()) == sorted(f2.values()))
    # Time: O(n * log(n))
    # Space: O(n) 

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def close_strings(word1, word2):
    if len(word1) != len(word2):
        return False
    
    wrd1_frq = Counter(word1)
    wrd2_frq = Counter(word2)
    
    keys_match = set(wrd1_frq.keys()) == set(wrd2_frq.keys())
    
    return sorted(wrd1_frq.values()) == sorted(wrd2_frq.values()) and keys_match
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = close_strings(word1 = "abc", word2 = "bca")
    print(result) # True

    result = close_strings(word1 = "a", word2 = "aa")
    print(result) # False

    result = close_strings(word1 = "cabbba", word2 = "abbccc")
    print(result) # True

if __name__ == "__main__":
    main()
