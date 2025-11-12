# ----------------------------------
# 953. Verifying An Alien Dictionary
# ----------------------------------

# Problem: https://leetcode.com/problems/verifying-an-alien-dictionary
#
# In an alien language, surprisingly, they also use English lowercase letters, but
# possibly in a different order. The order of the alphabet is some permutation of
# lowercase letters.
# 
# Given a sequence of words written in the alien language, and the order of the
# alphabet, return true if and only if the given words are sorted
# lexicographically in this alien language.
# 
# Example 1:
# 
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is
# sorted.
# 
# Example 2:
# 
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1],
# hence the sequence is unsorted.
# 
# Example 3:
# 
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is
# shorter (in size.) According to lexicographical rules "apple" > "app", because
# 'l' > '∅', where '∅' is defined as the blank character which is less than any
# other character (More info).
# 
# 
# Constraints:
#         1 <= words.length <= 100
#         1 <= words[i].length <= 20
#         order.length == 26
#         All characters in words[i] and order are English lowercase letters.


# Solution: https://youtu.be/OVgPAJIyX6o
# Credit: Navdeep Singh founder of NeetCode
def is_alien_sorted(words, order):
    # first differing char
    # if word A is prefix of word B, word B must be AFTER word A
    orderInd = { c : i for i, c in enumerate(order)}
    
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        
        for j in range(len(w1)):
            if j == len(w2):
                return False
            
            if w1[j] != w2[j]:
                if orderInd[w2[j]] < orderInd[w1[j]]:
                    return False
                break
    return True


def main():
    result = is_alien_sorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")
    print(result) # True

    result = is_alien_sorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz")
    print(result) # True

    result = is_alien_sorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz")
    print(result) # False

if __name__ == "__main__":
    main()
