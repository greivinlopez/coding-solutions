# -------------------------------------------
# 1255. Maximum Score Words Formed by Letters
# -------------------------------------------

# Problem: https://leetcode.com/problems/maximum-score-words-formed-by-letters
#
# Given a list of words, list of  single letters (might be repeating) and score of
# every character.
# 
# Return the maximum score of any valid set of words formed by using the given
# letters (words[i] cannot be used two or more times).
# 
# It is not necessary to use all characters in letters and each letter can only be
# used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0],
# score[1], ... , score[25] respectively.
# 
# Example 1:
# 
# Input: words = ["dog","cat","dad","good"], letters =
# ["a","a","c","d","d","d","g","o","o"], score =
# [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# Output: 23
# 
# Explanation:
# Score  a=1, c=9, d=5, g=3, o=2
# Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a
# score of 23.
# Words "dad" and "dog" only get a score of 21.
# 
# Example 2:
# 
# Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"],
# score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
# Output: 27
# 
# Explanation:
# Score  a=4, b=4, c=4, x=5, z=10
# Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with
# a score of 27.
# Word "xxxz" only get a score of 25.
# 
# Example 3:
# 
# Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score =
# [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
# Output: 0
# 
# Explanation:
# Letter "e" can only be used once.
# 
# 
# Constraints:
#         1 <= words.length <= 14
#         1 <= words[i].length <= 15
#         1 <= letters.length <= 100
#         letters[i].length == 1
#         score.length == 26
#         0 <= score[i] <= 10
#         words[i], letters[i] contains only lower case English letters.

from collections import Counter

# Solution: https://youtu.be/1cV8Hq9IAk4
# Credit: Navdeep Singh founder of NeetCode
def max_score_words(words, letters, score):
    
    def can_form_word(w, letter_cnt):
        word_cnt = Counter(w)
        for c in word_cnt:
            if word_cnt[c] > letter_cnt[c]:
                return False
        return True

    def get_score(w):
        res = 0
        for c in w:
            res += score[ord(c) - ord('a')]
        return res

    letter_cnt = Counter(letters)
    
    def backtrack(i):
        if i == len(words):
            return 0
        
        # Case 1: Skip the current word
        res = backtrack(i + 1)
        
        # Case 2: Include the current word (if possible)
        if can_form_word(words[i], letter_cnt):
            for c in words[i]:
                letter_cnt[c] -= 1
            
            res = max(res, get_score(words[i]) + backtrack(i + 1))
            
            # Backtrack: restore the letter count
            for c in words[i]:
                letter_cnt[c] += 1
        
        return res

    return backtrack(0)
    # Time:  O(2^n * w)  w = maximum length of a word 
    # Space: O(n)


def main():
    words = ["dog","cat","dad","good"]
    letters = ["a","a","c","d","d","d","g","o","o"]
    score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    result = max_score_words(words, letters, score)
    print(result) # 23

    words = ["xxxz","ax","bx","cx"]
    letters = ["z","a","b","c","x","x","x"]
    score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
    result = max_score_words(words, letters, score)
    print(result) # 27

    words = ["leetcode"]
    letters = ["l","e","t","c","o","d"]
    score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
    result = max_score_words(words, letters, score)
    print(result) # 0

if __name__ == "__main__":
    main()
