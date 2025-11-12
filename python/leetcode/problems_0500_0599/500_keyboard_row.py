# -----------------------
# 500. Keyboard Row ⌨️ 💻
# -----------------------

# Problem: https://leetcode.com/problems/keyboard-row
#
# Given an array of strings words, return the words that can be typed using
# letters of the alphabet on only one row of American keyboard like the image
# below.
# 
# Note that the strings are case-insensitive, both lowercased and uppercased of
# the same letter are treated as if they are at the same row.
# 
# In the American keyboard:
#         the first row consists of the characters "qwertyuiop",
#         the second row consists of the characters "asdfghjkl", and
#         the third row consists of the characters "zxcvbnm".
# 
# https://assets.leetcode.com/uploads/2018/10/12/keyboard.png
# 
# Example 1:
# 
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# 
# Explanation:
# Both "a" and "A" are in the 2nd row of the American keyboard due to case
# insensitivity.
# 
# Example 2:
# 
# Input: words = ["omk"]
# Output: []
# 
# Example 3:
# 
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]
# 
# 
# Constraints:
#         1 <= words.length <= 20
#         1 <= words[i].length <= 100
#         words[i] consists of English letters (both lowercase and uppercase).


# Solution: https://algo.monster/liteproblems/500
# Credit: AlgoMonster
def find_words(words):
    # Define sets for each row of the QWERTY keyboard
    first_row = set('qwertyuiop')
    second_row = set('asdfghjkl')
    third_row = set('zxcvbnm')
    
    # List to store words that can be typed using letters from a single row
    result = []
    
    # Check each word in the input list
    for word in words:
        # Convert word to lowercase and create a set of its characters
        word_chars = set(word.lower())
        
        # Check if all characters belong to any single keyboard row
        # The <= operator checks if word_chars is a subset of the row
        if (word_chars <= first_row or 
            word_chars <= second_row or 
            word_chars <= third_row):
            # Add the original word (with original casing) to result
            result.append(word)
    
    return result
    # Time: O(n * m)
    # Space: O(n * m)
    # n = the number of words in the input list
    # m = the average length of each word

# Solution: https://leetcode.com/problems/keyboard-row/solutions/3645744/python-3-2-lines-for-fun
# Credit: Capt Spaulding -> https://leetcode.com/u/Spaulding_/
def find_words_short(words):
    rows = (set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm"))
    return [w for w in words if any(set(w.lower()).issubset(row) for row in rows)]
    # Time: O(n * m)
    # Space: O(n * m)
    # n = the number of words in the input list words
    # m = the maximum length of a word in the input list


def main():
    result = find_words(words = ["Hello","Alaska","Dad","Peace"])
    print(result) # ["Alaska","Dad"]

    result = find_words(words = ["omk"])
    print(result) # []

    result = find_words(words = ["adsdf","sfd"])
    print(result) # ["adsdf","sfd"]

if __name__ == "__main__":
    main()
