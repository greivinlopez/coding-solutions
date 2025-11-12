# ---------------------
# 819. Most Common Word
# ---------------------

# Problem: https://leetcode.com/problems/most-common-word
#
# Given a string paragraph and a string array of the banned words banned, return
# the most frequent word that is not banned. It is guaranteed there is at least
# one word that is not banned, and that the answer is unique.
# 
# The words in paragraph are case-insensitive and the answer should be returned in
# lowercase.
# 
# Note that words can not contain punctuation symbols.
# 
# Example 1:
# 
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",
# banned = ["hit"]
# Output: "ball"
# 
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-
# banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
# 
# Example 2:
# 
# Input: paragraph = "a.", banned = []
# Output: "a"
# 
# 
# Constraints:
#   1 <= paragraph.length <= 1000
#   paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
#   0 <= banned.length <= 100
#   1 <= banned[i].length <= 10
#   banned[i] consists of only lowercase English letters.

from collections import Counter
import re

# Solution: https://algo.monster/liteproblems/819
# Credit: AlgoMonster
def most_common_word(paragraph, banned):
    # Create a set of banned words for O(1) lookup
    banned_words = set(banned)
    
    # Extract all words (lowercase letters only) from the paragraph
    # Convert to lowercase and count frequency of each word
    word_counts = Counter(re.findall(r'[a-z]+', paragraph.lower()))
    
    # Iterate through words sorted by frequency (most common first)
    # Return the first word that is not in the banned list
    for word, count in word_counts.most_common():
        if word not in banned_words:
            return word
    # Time: O(n + m)
    # Space: O(n + m)
    # n = the length of the paragraph
    # m = the number of banned words


def main():
    result = most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    print(result) # "ball"

    result = most_common_word("a.", [])
    print(result) # "a"

if __name__ == "__main__":
    main()
