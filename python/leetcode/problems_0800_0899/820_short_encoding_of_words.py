# ----------------------------
# 820. Short Encoding of Words
# ----------------------------

# Problem: https://leetcode.com/problems/short-encoding-of-words
#
# A valid encoding of an array of words is any reference string s and array of
# indices indices such that:
#
#         words.length == indices.length
#         The reference string s ends with the '#' character.
#         For each index indices[i], the substring of s starting from indices[i]
#         and up to (but not including) the next '#' character is equal to words[i].
# 
# Given an array of words, return the length of the shortest reference string s
# possible of any valid encoding of words.
# 
# Example 1:
# 
# Input: words = ["time", "me", "bell"]
# Output: 10
# 
# Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
# words[0] = "time", the substring of s starting from indices[0] = 0 to the next
# '#' is underlined in "time#bell#"
# words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#'
# is underlined in "time#bell#"
# words[2] = "bell", the substring of s starting from indices[2] = 5 to the next
# '#' is underlined in "time#bell#"
# 
# Example 2:
# 
# Input: words = ["t"]
# Output: 2
# 
# Explanation: A valid encoding would be s = "t#" and indices = [0].
# 
# 
# Constraints:
#         1 <= words.length <= 2000
#         1 <= words[i].length <= 7
#         words[i] consists of only lowercase letters.

from collections import defaultdict
from functools import reduce

# Solution: https://leetcode.com/problems/short-encoding-of-words/solutions/2172401/python-concise-brute-force-trie-solutions-with-explanation
# Credit: Zayne Siew -> https://leetcode.com/u/zayne-siew/
def minimum_length_encoding(words):
    words = list(set(words))
    trie = (d := lambda: defaultdict(d))()
    nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]  # equivalent to trie[word[-1]][word[-2]]...
    return sum((len(word)+1) for word, node in zip(words, nodes) if len(node) == 0)
    # Time: O(n * k)
    # Space: O(n * k)
    # we have n chains of length k

# Alternative Solution: https://algo.monster/liteproblems/820
# Much more verbose


def main():
    result = minimum_length_encoding(words = ["time", "me", "bell"])
    print(result) # 10

    result = minimum_length_encoding(words = ["t"])
    print(result) # 2

if __name__ == "__main__":
    main()
