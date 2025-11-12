# ---------------
# 824. Goat Latin
# ---------------

# Problem: https://leetcode.com/problems/goat-latin
#
# You are given a string sentence that consist of words separated by spaces. Each
# word consists of lowercase and uppercase letters only.
# 
# We would like to convert the sentence to "Goat Latin" (a made-up language
# similar to Pig Latin.) The rules of Goat Latin are as follows:
#         
#   * If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma"
#     to the end of the word.
#       * For example, the word "apple" becomes "applema".
#   * If a word begins with a consonant (i.e., not a vowel), remove the first
#     letter and append it to the end, then add "ma".
#       * For example, the word "goat" becomes "oatgma".
#   * Add one letter 'a' to the end of each word per its word index in the
#     sentence, starting with 1.
#       * For example, the first word gets "a" added to the end, the
#         second word gets "aa" added to the end, and so on.
# 
# Return the final sentence representing the conversion from sentence to Goat
# Latin.
# 
# Example 1:
# 
# Input: sentence = "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
# 
# Example 2:
# 
# Input: sentence = "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa
# hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
# 
# 
# Constraints:
#         1 <= sentence.length <= 150
#         sentence consists of English letters and spaces.
#         sentence has no leading or trailing spaces.
#         All the words in sentence are separated by a single space.


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def to_goat_latin(sentence):
    splitted = sentence.split(" ")
    
    ans = ""
    
    c = 1
    for w in splitted:
        temp = ""
        if w[0] in "aeiouAEIOU":
            temp = w + "ma"
            
        elif w[0] not in "aeiouAEIOU":
            temp = w[1:] + w[0] + "ma"
        
        temp = temp + "a"*c + " "
        c += 1
        ans += temp
    
    return ans[0:-1]
    # Time: O(n²)
    # Space: O(n²)
    # n = the total number of characters in the input sentence.


def main():
    result = to_goat_latin(sentence = "I speak Goat Latin")
    print(result) # "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

    result = to_goat_latin(sentence = "The quick brown fox jumped over the lazy dog")
    print(result) # "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

if __name__ == "__main__":
    main()
