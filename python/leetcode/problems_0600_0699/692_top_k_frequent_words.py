# -------------------------
# 692. Top K Frequent Words
# -------------------------

# Problem: https://leetcode.com/problems/top-k-frequent-words
#
# Given an array of strings words and an integer k, return the k most frequent
# strings.
# 
# Return the answer sorted by the frequency from highest to lowest. Sort the words
# with the same frequency by their lexicographical order.
# 
# Example 1:
# 
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# 
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# 
# Example 2:
# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k
# = 4
# Output: ["the","is","sunny","day"]
# 
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# with the number of occurrence being 4, 3, 2 and 1 respectively.
# 
# 
# Constraints:
#         1 <= words.length <= 500
#         1 <= words[i].length <= 10
#         words[i] consists of lowercase English letters.
#         k is in the range [1, The number of unique words[i]]
# 
# Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?

from collections import Counter

# Solution: https://algo.monster/liteproblems/692
# Credit: AlgoMonster
def top_k_frequent(words, k):
    # Count the frequency of each word in the input list
    word_count = Counter(words)
    
    # Sort words by:
    # 1. Frequency in descending order (higher frequency first)
    # 2. Lexicographical order for words with same frequency
    sorted_words = sorted(word_count, key=lambda word: (-word_count[word], word))
    
    # Return the top k most frequent words
    return sorted_words[:k]
    # Time: O(n * log n)
    # Space: O(n)


def main():
    result = top_k_frequent(words = ["i","love","leetcode","i","love","coding"], k = 2)
    print(result) # ["i","love"]

    result = top_k_frequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4)
    print(result) # ["the","is","sunny","day"]

if __name__ == "__main__":
    main()
