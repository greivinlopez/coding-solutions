# ------------------------------
# 1078. Occurrences After Bigram
# ------------------------------

# Problem: https://leetcode.com/problems/occurrences-after-bigram
#
# Given two strings first and second, consider occurrences in some text of the
# form "first second third", where second comes immediately after first, and third
# comes immediately after second.
# 
# Return an array of all the words third for each occurrence of "first second
# third".
# 
# Example 1:
# 
# Input: text = "alice is a good girl she is a good student", first = "a", second
# = "good"
# Output: ["girl","student"]
# 
# Example 2:
# 
# Input: text = "we will we will rock you", first = "we", second = "will"
# Output: ["we","rock"]
# 
# 
# Constraints:
#         1 <= text.length <= 1000
#         text consists of lowercase English letters and spaces.
#         All the words in text are separated by a single space.
#         1 <= first.length, second.length <= 10
#         first and second consist of lowercase English letters.
#         text will not have any leading or trailing spaces.


# Solution: https://algo.monster/liteproblems/1078
# Credit: AlgoMonster
def find_ocurrences(text, first, second):
    # Split the text into individual words
    words = text.split()
    
    # Initialize result list to store third words
    result = []
    
    # Iterate through the words, stopping 2 positions before the end
    # to ensure we have enough words to check a triplet
    for i in range(len(words) - 2):
        # Extract three consecutive words starting at index i
        word_1, word_2, word_3 = words[i:i + 3]
        
        # Check if the first two words match our pattern
        if word_1 == first and word_2 == second:
            # Add the third word to our result
            result.append(word_3)
    
    return result
    # Time: O(n)
    # Space: O(n)


def main():
    result = find_ocurrences(text = "alice is a good girl she is a good student", first = "a", second = "good")
    print(result) # ['girl', 'student']

    result = find_ocurrences(text = "we will we will rock you", first = "we", second = "will")
    print(result) # ['we', 'rock']

if __name__ == "__main__":
    main()
