# ------------------------------------
# 318. Maximum Product of Word Lengths
# ------------------------------------

# Problem: https://leetcode.com/problems/maximum-product-of-word-lengths
#
# Given a string array words, return the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. If no such two
# words exist, return 0.
# 
# Example 1:
# 
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# 
# Explanation: The two words can be "abcw", "xtfn".
# 
# Example 2:
# 
# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# 
# Explanation: The two words can be "ab", "cd".
# 
# Example 3:
# 
# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# 
# Explanation: No such pair of words.
# 
# 
# Constraints:
#         2 <= words.length <= 1000
#         1 <= words[i].length <= 1000
#         words[i] consists only of lowercase English letters.

from itertools import combinations

# Solution: https://leetcode.com/problems/maximum-product-of-word-lengths/solutions/2085316/python-easy-3-approaches-explained
# Credit: https://leetcode.com/u/constantine786/
# Three different solutions from the same source
def max_product(words):
    # Bit Mask Solution
    n = len(words)
    
    bit_masks = [0] * n
    lengths = [0] * n
    
    for i in range(n):             
        for c in words[i]:
            bit_masks[i] |= 1 << (ord(c) - ord('a')) # set the character bit            
        lengths[i] = len(words[i])
                    
    max_val = 0
    for i in range(n):
        for j in range(i + 1, n):
            if not (bit_masks[i] & bit_masks[j]):
                max_val = max(max_val, lengths[i] * lengths[j])
    
    return max_val
    # Time: O(n²)
    # Space: O(n)

def max_product_one_liner(words):
    # One liner
    return max([len(s1) * len(s2) for s1, s2 in combinations(words, 2)  if not (set(s1) & set(s2))], default=0)
    # Time: O(n² * m)
    # Space: O(n²) or O(n * m) depending on the interpretation
    # m = the maximum length of a word in the list.

def max_product_hashset(words):
    # Hashset Solution
    n = len(words)                        
    char_set = [set(words[i]) for i in range(n)] # precompute hashset for each word                                                  
    max_val = 0
    for i in range(n):
        for j in range(i + 1, n):
            if not (char_set[i] & char_set[j]): # if nothing common
                max_val = max(max_val, len(words[i]) * len(words[j]))
    
    return max_val
    # Time: O(n² + m)
    # Space: O(n)
    # m = the total length of all words


def main():
    result = max_product(["abcw","baz","foo","bar","xtfn","abcdef"])
    print(result) # 16

    result = max_product(["a","ab","abc","d","cd","bcd","abcd"])
    print(result) # 4

    result = max_product(["a","aa","aaa","aaaa"])
    print(result) # 0

if __name__ == "__main__":
    main()
