# ------------------------------------------
# 2452. Words Within Two Edits of Dictionary
# ------------------------------------------

# Problem: https://leetcode.com/problems/words-within-two-edits-of-dictionary
#
# You are given two string arrays, queries and dictionary. All words in each array
# comprise of lowercase English letters and have the same length.
# 
# In one edit you can take a word from queries, and change any letter in it to any
# other letter. Find all words from queries that, after a maximum of two edits,
# equal some word from dictionary.
# 
# Return a list of all words from queries, that match with some word from
# dictionary after a maximum of two edits. Return the words in the same order they
# appear in queries.
# 
# Example 1:
# 
# Input: queries = ["word","note","ants","wood"], dictionary =
# ["wood","joke","moat"]
# Output: ["word","note","wood"]
# 
# Explanation:
# - Changing the 'r' in "word" to 'o' allows it to equal the dictionary word
# "wood".
# - Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
# - It would take more than 2 edits for "ants" to equal a dictionary word.
# - "wood" can remain unchanged (0 edits) and match the corresponding dictionary
# word.
# Thus, we return ["word","note","wood"].
# 
# Example 2:
# 
# Input: queries = ["yes"], dictionary = ["not"]
# Output: []
# 
# Explanation:
# Applying any two edits to "yes" cannot make it equal to "not". Thus, we return
# an empty array.
# 
# 
# Constraints:
#         1 <= queries.length, dictionary.length <= 100
#         n == queries[i].length == dictionary[j].length
#         1 <= n <= 100
#         All queries[i] and dictionary[j] are composed of lowercase English letters.


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def two_edit_words(queries, dictionary):
    def checkIfCanEqual(word, query):
        toCorrect = 0
        for j in range(len(word)):
            if word[j] != query[j]:
                toCorrect += 1
        
        return toCorrect
    
    ans = []
    for query in queries:
        if query in dictionary:
            ans.append(query)
        
        else:
            for j in range(len(dictionary)):
                c = checkIfCanEqual(dictionary[j], query)
                if c <= 2:
                    ans.append(query)
                    break
                else:
                    continue
    return ans
    # Time: O(n * m)
    # Space: O(n * m)
    # n = the number of queries
    # m = the number of words in the dictionary


def main():
    result = two_edit_words(queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"])
    print(result) # ["word","note","wood"]

    result = two_edit_words(queries = ["yes"], dictionary = ["not"])
    print(result) # []

if __name__ == "__main__":
    main()
