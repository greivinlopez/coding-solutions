# -----------------------------------
# 1451. Rearrange Words in a Sentence
# -----------------------------------

# Problem: https://leetcode.com/problems/rearrange-words-in-a-sentence
#
# Given a sentence text (A sentence is a string of space-separated words) in the
# following format:
#         
#   * First letter is in upper case.
#   * Each word in text are separated by a single space.
# 
# Your task is to rearrange the words in text such that all words are rearranged
# in an increasing order of their lengths. If two words have the same length,
# arrange them in their original order.
# 
# Return the new text following the format shown above.
# 
# Example 1:
# 
# Input: text = "Leetcode is cool"
# Output: "Is cool leetcode"
# 
# Explanation: There are 3 words, "Leetcode" of length 8, "is" of length 2 and
# "cool" of length 4.
# Output is ordered by length and the new first word starts with capital letter.
# 
# Example 2:
# 
# Input: text = "Keep calm and code on"
# Output: "On and keep calm code"
# 
# Explanation: Output is ordered as follows:
# "On" 2 letters.
# "and" 3 letters.
# "keep" 4 letters in case of tie order by position in original text.
# "calm" 4 letters.
# "code" 4 letters.
# 
# Example 3:
# 
# Input: text = "To be or not to be"
# Output: "To be or to be not"
# 
# 
# Constraints:
#   * text begins with a capital letter and then contains lowercase letters
#     and single space between words.
#   * 1 <= text.length <= 10^5


# Solution: https://algo.monster/liteproblems/1451
# Credit: AlgoMonster
def arrange_words(text):
    # Split the text into individual words
    words = text.split()
    
    # Convert the first word to lowercase to ensure uniform sorting
    # (since the original first word is capitalized)
    words[0] = words[0].lower()
    
    # Sort words by their length, maintaining relative order for words of same length
    # Python's sort is stable, so original order is preserved for equal-length words
    words.sort(key=len)
    
    # Capitalize the first word of the rearranged sentence
    words[0] = words[0].capitalize()
    
    # Join the words back into a single string with spaces
    return " ".join(words)
    # Time: O(n * log n)
    # Space: O(n)


def main():
    result = arrange_words(text = "Leetcode is cool")
    print(result) # "Is cool leetcode"

    result = arrange_words(text = "Keep calm and code on")
    print(result) # "On and keep calm code"

    result = arrange_words(text = "To be or not to be")
    print(result) # "To be or to be not"

if __name__ == "__main__":
    main()
