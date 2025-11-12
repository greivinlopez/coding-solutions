# ----------------------------
# 804. Unique Morse Code Words
# ----------------------------

# Problem: https://leetcode.com/problems/unique-morse-code-words
#
# International Morse Code defines a standard encoding where each letter is mapped
# to a series of dots and dashes, as follows:
# 
#         'a' maps to ".-",
#         'b' maps to "-...",
#         'c' maps to "-.-.", and so on.
# 
# For convenience, the full table for the 26 letters of the English alphabet is
# given below:
# 
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
# "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."
# ]
# 
# Given an array of strings words where each word can be written as a
# concatenation of the Morse code of each letter.
#         
#   * For example, "cab" can be written as "-.-..--...", which is the concatenation
#     of "-.-.", ".-", and "-...". We will call such a concatenation the
#     transformation of a word.
# 
# Return the number of different transformations among all words we have.
# 
# Example 1:
# 
# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# 
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".
# 
# Example 2:
# 
# Input: words = ["a"]
# Output: 1
# 
# 
# Constraints:
#         1 <= words.length <= 100
#         1 <= words[i].length <= 12
#         words[i] consists of lowercase English letters.


# Solution: https://algo.monster/liteproblems/804
# Credit: AlgoMonster
def unique_morse_representations(words):
    # Morse code mappings for letters a-z
    morse_codes = [
        ".-",    # a
        "-...",  # b
        "-.-.",  # c
        "-..",   # d
        ".",     # e
        "..-.",  # f
        "--.",   # g
        "....",  # h
        "..",    # i
        ".---",  # j
        "-.-",   # k
        ".-..",  # l
        "--",    # m
        "-.",    # n
        "---",   # o
        ".--.",  # p
        "--.-",  # q
        ".-.",   # r
        "...",   # s
        "-",     # t
        "..-",   # u
        "...-",  # v
        ".--",   # w
        "-..-",  # x
        "-.--",  # y
        "--..",  # z
    ]
    
    # Create a set to store unique morse code transformations
    # For each word, convert each character to its morse code equivalent
    # and concatenate them to form the complete morse representation
    unique_transformations = {
        ''.join([morse_codes[ord(char) - ord('a')] for char in word]) 
        for word in words
    }
    
    # Return the count of unique morse code representations
    return len(unique_transformations)
    # Time: O(n * m)
    # Space: O(n * m)
    # n = the number of words in the input list
    # m = the average length of each word


def main():
    result = unique_morse_representations(words = ["gin","zen","gig","msg"])
    print(result) # 2

    result = unique_morse_representations(words = ["a"])
    print(result) # 1

if __name__ == "__main__":
    main()
