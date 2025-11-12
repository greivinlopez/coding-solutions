# -----------------------------
# 748. Shortest Completing Word
# -----------------------------

# Problem: https://leetcode.com/problems/shortest-completing-word
#
# Given a string licensePlate and an array of strings words, find the shortest
# completing word in words.
# 
# A completing word is a word that contains all the letters in licensePlate.
# Ignore numbers and spaces in licensePlate, and treat letters as case
# insensitive. If a letter appears more than once in licensePlate, then it must
# appear in the word the same number of times or more.
# 
# For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b'
# (ignoring case), and 'c' twice. Possible completing words are "abccdef",
# "caaacab", and "cbca".
# 
# Return the shortest completing word in words. It is guaranteed an answer exists.
# If there are multiple shortest completing words, return the first one that
# occurs in words.
# 
# Example 1:
# 
# Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
# Output: "steps"
# 
# Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and
# 't'.
# "step" contains 't' and 'p', but only contains 1 's'.
# "steps" contains 't', 'p', and both 's' characters.
# "stripe" is missing an 's'.
# "stepple" is missing an 's'.
# Since "steps" is the only word containing all the letters, that is the answer.
# 
# Example 2:
# 
# Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
# Output: "pest"
# 
# Explanation: licensePlate only contains the letter 's'. All the words contain
# 's', but among these "pest", "stew", and "show" are shortest. The answer is
# "pest" because it is the word that appears earliest of the 3.
# 
# 
# Constraints:
#         1 <= licensePlate.length <= 7
#         licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
#         1 <= words.length <= 1000
#         1 <= words[i].length <= 15
#         words[i] consists of lower case English letters.

from collections import Counter

# Solution: https://algo.monster/liteproblems/748
# Credit: AlgoMonster
def shortest_completing_word(licensePlate, words):
    # Count the frequency of each letter in the license plate (case-insensitive)
    license_char_count = Counter(
        char.lower() for char in licensePlate if char.isalpha()
    )
    
    # Initialize the result as None
    result = None
    
    # Iterate through each word in the words list
    for word in words:
        # Skip if we already have a result and current word is longer or equal
        if result and len(word) >= len(result):
            continue
        
        # Count the frequency of characters in the current word
        word_char_count = Counter(word)
        
        # Check if the current word contains all required characters
        # with at least the required frequency
        if all(count <= word_char_count[char] 
                for char, count in license_char_count.items()):
            result = word
    
    return result
    # Time: O(n * m)
    # Space: O(1)

# Similar Solution: Shorter
# Solution: https://leetcode.com/problems/shortest-completing-word/solutions/2421438/python-elegant-short-two-lines-counter
# Credit: Kyrylo-Ktl -> https://leetcode.com/u/Kyrylo-Ktl/
def shortest_completing_word_short(licensePlate, words):
    letters = Counter(ltr.lower() for ltr in licensePlate if ltr.isalpha())
    return min((word for word in words if not letters - Counter(word)), key=len)
    # Time: O(m * max(n,k))
    # Space: O(n + k)
    # n - length of letters in license_plate
    # m - length of words
    # k - length of each word in words


def main():
    result = shortest_completing_word(licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"])
    print(result) # "steps"

    result = shortest_completing_word(licensePlate = "1s3 456", words = ["looks","pest","stew","show"])
    print(result) # "pest"

if __name__ == "__main__":
    main()
