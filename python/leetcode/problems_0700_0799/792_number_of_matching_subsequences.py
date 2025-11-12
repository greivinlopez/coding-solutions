# ------------------------------------
# 792. Number of Matching Subsequences
# ------------------------------------

# Problem: https://leetcode.com/problems/number-of-matching-subsequences
#
# Given a string s and an array of strings words, return the number of words[i]
# that is a subsequence of s.
# 
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative order
# of the remaining characters.
#         
#   * For example, "ace" is a subsequence of "abcde".
# 
# Example 1:
# 
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# 
# Explanation: There are three strings in words that are a subsequence of s: "a",
# "acd", "ace".
# 
# Example 2:
# 
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
# 
# 
# Constraints:
#         1 <= s.length <= 5 * 10⁴
#         1 <= words.length <= 5000
#         1 <= words[i].length <= 50
#         s and words[i] consist of only lowercase English letters.

from collections import defaultdict, deque

# Solution: https://algo.monster/liteproblems/792
# Credit: AlgoMonster
def num_matching_subseq(s, words):
    # Dictionary to store words grouped by their first character
    # Key: character, Value: deque of words starting with that character
    waiting_dict = defaultdict(deque)
    
    # Group all words by their first character
    for word in words:
        waiting_dict[word[0]].append(word)
    
    # Counter for words that are subsequences of s
    matching_count = 0
    
    # Process each character in string s
    for char in s:
        # Process all words currently waiting for this character
        # Use len() to get current queue size to avoid infinite loop
        current_queue_size = len(waiting_dict[char])
        for _ in range(current_queue_size):
            # Get the word from front of queue
            current_word = waiting_dict[char].popleft()
            
            # If this was the last character needed, word is a subsequence
            if len(current_word) == 1:
                matching_count += 1
            else:
                # Move word to queue for its next required character
                # Remove first character and add to appropriate queue
                next_char = current_word[1]
                remaining_word = current_word[1:]
                waiting_dict[next_char].append(remaining_word)
    
    return matching_count
    # Time: O(n + m * l)
    # Space: O(m * l)
    # n = he length of string s
    # m = the total number of words in the words list
    # l = the average length of words

# Solution: https://leetcode.com/problems/number-of-matching-subsequences/solutions/117634/efficient-and-simple-go-through-words-in-parallel-with-explanation
# Credit: Stefan Pochmann -> https://leetcode.com/u/stefanpochmann/
def num_matching_subseq_short(s, words):
    waiting = defaultdict(list, {' ': map(iter, words)})
    for c in ' ' + s:
        for it in waiting.pop(c, ()):
            waiting[next(it, None)].append(it)
    return len(waiting[None])
    # Time: O(n + m)
    # Space: O(m)
    # n = he length of string s
    # m = the total number of words in the words list


def main():
    result = num_matching_subseq(s = "abcde", words = ["a","bb","acd","ace"])
    print(result) # 3

    result = num_matching_subseq(s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"])
    print(result) # 2

if __name__ == "__main__":
    main()
