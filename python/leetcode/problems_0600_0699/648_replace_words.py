# ------------------
# 648. Replace Words
# ------------------

# Problem: https://leetcode.com/problems/replace-words
#
# In English, we have a concept called root, which can be followed by some other
# word to form another longer word - let's call this word derivative. For example,
# when the root "help" is followed by the word "ful", we can form a derivative
# "helpful".
# 
# Given a dictionary consisting of many roots and a sentence consisting of words
# separated by spaces, replace all the derivatives in the sentence with the root
# forming it. If a derivative can be replaced by more than one root, replace it
# with the root that has the shortest length.
# 
# Return the sentence after the replacement.
# 
# Example 1:
# 
# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by
# the battery"
# Output: "the cat was rat by the bat"
# 
# Example 2:
# 
# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"
# 
# 
# Constraints:
#         1 <= dictionary.length <= 1000
#         1 <= dictionary[i].length <= 100
#         dictionary[i] consists of only lower-case letters.
#         1 <= sentence.length <= 10⁶
#         sentence consists of only lower-case letters and spaces.
#         The number of words in sentence is in the range [1, 1000]
#         The length of each word in sentence is in the range [1, 1000]
#         Every two consecutive words in sentence will be separated by exactly one space.
#         sentence does not have leading or trailing spaces.


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def replace_words(dictionary, sentence):
    word_array = sentence.split()
    dict_set = set(dictionary)

    def shortest_root(word, dict_set):
        # Find the shortest root of the word in the dictionary
        for i in range(len(word)):
            root = word[0:i]
            if root in dict_set:
                return root
        # There is not a corresponding root in the dictionary
        return word

    # Replace each word in sentence with the corresponding shortest root
    for word in range(len(word_array)):
        word_array[word] = shortest_root(word_array[word], dict_set)

    return " ".join(word_array)
    # Time: O(n + m)
    # Space: O(n + m)
    # n = total number of characters in all dictionary words
    # m = total number of characters in the sentence.


def main():
    result = replace_words(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery")
    print(result) # "the cat was rat by the bat"

    result = replace_words(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs")
    print(result) # "a a b c"

if __name__ == "__main__":
    main()
