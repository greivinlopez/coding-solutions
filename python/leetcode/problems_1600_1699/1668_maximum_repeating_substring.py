# ---------------------------------
# 1668. Maximum Repeating Substring
# ---------------------------------

# Problem: https://leetcode.com/problems/maximum-repeating-substring
#
# For a string sequence, a string word is k-repeating if word concatenated k times
# is a substring of sequence. The word's maximum k-repeating value is the highest
# value k where word is k-repeating in sequence. If word is not a substring of
# sequence, word's maximum k-repeating value is 0.
# 
# Given strings sequence and word, return the maximum k-repeating value of word in
# sequence.
# 
# Example 1:
# 
# Input: sequence = "ababc", word = "ab"
# Output: 2
# 
# Explanation: "abab" is a substring in "ababc".
# 
# Example 2:
# 
# Input: sequence = "ababc", word = "ba"
# Output: 1
# 
# Explanation: "ba" is a substring in "ababc". "baba" is not a substring in
# "ababc".
# 
# Example 3:
# 
# Input: sequence = "ababc", word = "ac"
# Output: 0
# 
# Explanation: "ac" is not a substring in "ababc".
# 
# 
# Constraints:
#         1 <= sequence.length <= 100
#         1 <= word.length <= 100
#         sequence and word contains only lowercase English letters.


# Solution: https://algo.monster/liteproblems/1668
# Credit: AlgoMonster
def max_repeating(sequence, word):
    # Calculate the maximum possible number of repetitions
    # by dividing the length of sequence by the length of word
    max_possible_k = len(sequence) // len(word)
    
    # Iterate from the maximum possible k down to 0
    # We start from the largest possible value for optimization
    for k in range(max_possible_k, -1, -1):
        # Check if word repeated k times exists as a substring in sequence
        # word * k creates a string with word repeated k times
        if word * k in sequence:
            # Return the first (largest) k where the pattern is found
            return k
    
    # This line is technically unreachable since k=0 (empty string) 
    # will always be found in any string
    return 0
    # Time: O(n * m * k)
    # Space: O(m * k)


def main():
    result = max_repeating(sequence = "ababc", word = "ab")
    print(result) # 2

    result = max_repeating(sequence = "ababc", word = "ba")
    print(result) # 1

    result = max_repeating(sequence = "ababc", word = "ac")
    print(result) # 0

if __name__ == "__main__":
    main()
