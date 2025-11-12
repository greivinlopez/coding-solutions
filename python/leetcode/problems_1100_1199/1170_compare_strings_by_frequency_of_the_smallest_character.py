# ------------------------------------------------------------
# 1170. Compare Strings by Frequency of the Smallest Character
# ------------------------------------------------------------

# Problem: https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character
#
# Let the function f(s) be the frequency of the lexicographically smallest
# character in a non-empty string s. For example, if s = "dcce" then f(s) = 2
# because the lexicographically smallest character is 'c', which has a frequency
# of 2.
# 
# You are given an array of strings words and another array of query strings
# queries. For each query queries[i], count the number of words in words such that
# f(queries[i]) < f(W) for each W in words.
# 
# Return an integer array answer, where each answer[i] is the answer to the ith
# query.
# 
# Example 1:
# 
# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# 
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd")
# < f("zaaaz").
# 
# Example 2:
# 
# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# 
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second query
# both f("aaa") and f("aaaa") are both > f("cc").
# 
# 
# Constraints:
#         1 <= queries.length <= 2000
#         1 <= words.length <= 2000
#         1 <= queries[i].length, words[i].length <= 10
#         queries[i][j], words[i][j] consist of lowercase English letters.

from collections import Counter
from string import ascii_lowercase
from bisect import bisect_right

# Solution: https://algo.monster/liteproblems/1170
# Credit: AlgoMonster
def num_smaller_by_frequency(queries, words):
    def calculate_smallest_char_frequency(s):
        # Count frequency of each character in the string
        char_counter = Counter(s)
        
        # Find the first character in alphabetical order that exists in the string
        # and return its frequency
        for char in ascii_lowercase:
            if char_counter[char] > 0:
                return char_counter[char]
        
        return 0  # Should never reach here for non-empty strings
    
    # Get the total number of words
    word_count = len(words)
    
    # Calculate f(w) for each word and sort the results
    # This allows us to use binary search later
    word_frequencies = sorted(calculate_smallest_char_frequency(word) for word in words)
    
    # For each query, find how many words have f(w) > f(query)
    # Using binary search to find the rightmost position where f(query) can be inserted
    # word_count - position gives us the count of elements greater than f(query)
    result = []
    for query in queries:
        query_frequency = calculate_smallest_char_frequency(query)
        position = bisect_right(word_frequencies, query_frequency)
        result.append(word_count - position)
    
    return result
    # Time: O((n + q) * M + n * log(n))
    # Space: O(n)
    # M is the maximum string length


def main():
    result = num_smaller_by_frequency(queries = ["cbd"], words = ["zaaaz"])
    print(result) # [1]

    result = num_smaller_by_frequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"])
    print(result) # [1, 2]

if __name__ == "__main__":
    main()
