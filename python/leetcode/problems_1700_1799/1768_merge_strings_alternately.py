# -------------------------------
# 1768. Merge Strings Alternately
# -------------------------------

# Problem: https://leetcode.com/problems/merge-strings-alternately
#
# You are given two strings word1 and word2. Merge the strings by adding letters
# in alternating order, starting with word1. If a string is longer than the other,
# append the additional letters onto the end of the merged string.
# 
# Return the merged string.
# 
# Example 1:
# 
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# 
# Example 2:
# 
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s
# 
# Example 3:
# 
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d
# 
# 
# Constraints:
#         1 <= word1.length, word2.length <= 100
#         word1 and word2 consist of lowercase English letters.


# Solution: https://youtu.be/LECWOvTo-Sc
# Credit: Navdeep Singh founder of NeetCode
def merge_alternately(word1, word2):
    i = j = 0
    res = []

    while i < len(word1) and j < len(word2):
        res.append(word1[i])
        res.append(word2[j])
        i += 1
        j += 1
    res.append(word1[i:])
    res.append(word2[j:])
    return ''.join(res)


# Solution: https://youtu.be/qq-AqEPKsI8
# Credit: Greg Hogg
def merge_alternately_brute(word1, word2):
    # Brute Force Solution
    characters = ""
    cur_word = 1
    a, b = 0, 0

    while a < len(word1) and b < len(word2):
        if cur_word == 1:
            characters += word1[a]
            a += 1
            cur_word = 2
        else:
            characters += word2[b]
            b += 1
            cur_word = 1
    
    while a < len(word1):
        characters += word1[a]
        a += 1
    
    while b < len(word2):
        characters += word2[b]
        b += 1
    
    return characters
    # Let A be the length of Word1
    # Let B be the length of Word2
    # Let T = A + B
    
    # Time: O(T^2)
    # Space: O(T)


def merge_alternately_alt2(word1, word2):
    # Optimal Solution
    A, B = len(word1), len(word2)
    a, b = 0, 0
    s = []

    word = 1
    while a < A and b < B:
        if word == 1:
            s.append(word1[a])
            a += 1
            word = 2
        else:
            s.append(word2[b])
            b += 1
            word = 1
    
    while a < A:
        s.append(word1[a])
        a += 1
    
    while b < B:
        s.append(word2[b])
        b += 1
    
    return ''.join(s)
    # Let A be the length of Word1
    # Let B be the length of Word2
    # Let T = A + B
    
    # Time: O(T)
    # Space: O(T)

def main():
    result = merge_alternately(word1 = "abc", word2 = "pqr")
    print(result) # "apbqcr"

    result = merge_alternately(word1 = "ab", word2 = "pqrs")
    print(result) # "apbqrs"

    result = merge_alternately(word1 = "abcd", word2 = "pq")
    print(result) # "apbqcd"

if __name__ == "__main__":
    main()
