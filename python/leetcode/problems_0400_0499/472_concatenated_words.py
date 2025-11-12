# -----------------------
# 472. Concatenated Words
# -----------------------

# Problem: https://leetcode.com/problems/concatenated-words
#
# Given an array of strings words (without duplicates), return all the
# concatenated words in the given list of words.
# 
# A concatenated word is defined as a string that is comprised entirely of at
# least two shorter words (not necessarily distinct) in the given array.
# 
# Example 1:
# 
# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","
# rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# 
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# 
# Example 2:
# 
# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]
# 
# 
# Constraints:
#         1 <= words.length <= 10^4
#         1 <= words[i].length <= 30
#         words[i] consists of only lowercase English letters.
#         All the strings of words are unique.
#         1 <= sum(words[i].length) <= 10^5


# Solution: https://youtu.be/iHp7fjw1R28
# Credit: Navdeep Singh founder of NeetCode
def find_all_concatenated_words_in_a_dict(words):
    wordSet = set(words)
    
    def dfs(word):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            
            if ((prefix in wordSet and suffix in wordSet) or
                (prefix in wordSet and dfs(suffix))):
                return True
        return False

    res = []
    for w in words:
        if dfs(w):
            res.append(w)
    
    return res
    # Time: O(N * L²)   N = number of words | L = maximum length of a word
    # Space: O(L)


def main():
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    result = find_all_concatenated_words_in_a_dict(words)
    print(result) # ['catsdogcats', 'dogcatsdog', 'ratcatdogcat']

    words = ["cat","dog","catdog"]
    result = find_all_concatenated_words_in_a_dict(words)
    print(result) # ['catdog']

if __name__ == "__main__":
    main()
