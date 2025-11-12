# ------------------------------------------------
# 524. Longest Word in Dictionary through Deleting
# ------------------------------------------------

# Problem: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting
#
# Given a string s and a string array dictionary, return the longest string in the
# dictionary that can be formed by deleting some of the given string characters.
# If there is more than one possible result, return the longest word with the
# smallest lexicographical order. If there is no possible result, return the empty
# string.
# 
# Example 1:
# 
# Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# Output: "apple"
# 
# Example 2:
# 
# Input: s = "abpcplea", dictionary = ["a","b","c"]
# Output: "a"
# 
# 
# Constraints:
#         1 <= s.length <= 1000
#         1 <= dictionary.length <= 1000
#         1 <= dictionary[i].length <= 1000
#         s and dictionary[i] consist of lowercase English letters.


# Solution: https://algo.monster/liteproblems/524
# Credit: AlgoMonster
def find_longest_word(s, dictionary):
    def is_subsequence(word, source):
        word_len, source_len = len(word), len(source)
        word_idx = source_idx = 0
        
        # Iterate through both strings
        while word_idx < word_len and source_idx < source_len:
            # If characters match, move word pointer forward
            if word[word_idx] == source[source_idx]:
                word_idx += 1
            # Always move source pointer forward
            source_idx += 1
        
        # Return True if all characters in word were found
        return word_idx == word_len
    
    # Initialize result with empty string
    result = ""
    
    # Check each word in the dictionary
    for word in dictionary:
        # Check if current word is a subsequence of s
        if is_subsequence(word, s):
            # Update result if current word is:
            # 1. Longer than current result, OR
            # 2. Same length but lexicographically smaller
            if len(result) < len(word) or (len(result) == len(word) and result > word):
                result = word
    
    return result
    # Time: O(d * (n + m))
    # Space: O(1)
    # n = length of s
    # m = average word length
    # d = number of words in dictionary


def main():
    result = find_longest_word(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"])
    print(result) # "apple"

    result = find_longest_word(s = "abpcplea", dictionary = ["a","b","c"])
    print(result) # "a"

if __name__ == "__main__":
    main()
