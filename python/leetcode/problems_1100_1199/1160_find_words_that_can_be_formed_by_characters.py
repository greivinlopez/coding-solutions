# -------------------------------------------------
# 1160. Find Words That Can Be Formed by Characters
# -------------------------------------------------

# Problem: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters
#
# You are given an array of strings words and a string chars.
# 
# A string is good if it can be formed by characters from chars (each character
# can only be used once for each word in words).
# 
# Return the sum of lengths of all good strings in words.
# 
# Example 1:
# 
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# 
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is
# 3 + 3 = 6.
# 
# Example 2:
# 
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# 
# Explanation: The strings that can be formed are "hello" and "world" so the
# answer is 5 + 5 = 10.
# 
# 
# Constraints:
#         1 <= words.length <= 1000
#         1 <= words[i].length, chars.length <= 100
#         words[i] and chars consist of lowercase English letters.

from collections import Counter, defaultdict

# Solution: https://youtu.be/EQ5jTZdEn8Y
# Credit: Navdeep Singh founder of NeetCode
def count_characters(words, chars):
    count = Counter(chars)
    res = 0

    for w in words:
        cur_word = defaultdict(int)
        good = True
        for c in w:
            cur_word[c] += 1
            if c not in count or cur_word[c] > count[c]:
                good = False
                break
        if good:
            res += len(w)
    
    return res
    # Time: O(n * l)    l = average length of a word
    # Space: O(1)       O(k) where k = 26


def main():
    result = count_characters(words = ["cat","bt","hat","tree"], chars = "atach")
    print(result) # 6

    result = count_characters(words = ["hello","world","leetcode"], chars = "welldonehoneyr")
    print(result) # 10

if __name__ == "__main__":
    main()
