# -----------------------------
# 890. Find and Replace Pattern
# -----------------------------

# Problem: https://leetcode.com/problems/find-and-replace-pattern
#
# Given a list of strings words and a string pattern, return a list of words[i]
# that match pattern. You may return the answer in any order.
# 
# A word matches the pattern if there exists a permutation of letters p so that
# after replacing every letter x in the pattern with p(x), we get the desired
# word.
# 
# Recall that a permutation of letters is a bijection from letters to letters:
# every letter maps to another letter, and no two letters map to the same letter.
# 
# Example 1:
# 
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# 
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b
# -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a
# permutation, since a and b map to the same letter.
# 
# Example 2:
# 
# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]
# 
# 
# Constraints:
#         1 <= pattern.length <= 20
#         1 <= words.length <= 50
#         words[i].length == pattern.length
#         pattern and words[i] are lowercase English letters.


# Solution: https://algo.monster/liteproblems/890
# Credit: AlgoMonster
def find_and_replace_pattern(words, pattern):
    def matches_pattern(word, pattern):
        # Initialize mapping arrays for ASCII characters (size 128)
        # These arrays store the last index where each character was seen
        word_last_seen = [0] * 128
        pattern_last_seen = [0] * 128
        
        # Iterate through word and pattern simultaneously with 1-based indexing
        for index, (word_char, pattern_char) in enumerate(zip(word, pattern), start=1):
            # Get ASCII values of current characters
            word_char_ascii = ord(word_char)
            pattern_char_ascii = ord(pattern_char)
            
            # If the last seen positions don't match, the mapping is inconsistent
            if word_last_seen[word_char_ascii] != pattern_last_seen[pattern_char_ascii]:
                return False
            
            # Update last seen position for both characters
            word_last_seen[word_char_ascii] = index
            pattern_last_seen[pattern_char_ascii] = index
        
        return True
    
    # Filter and return words that match the pattern
    return [word for word in words if matches_pattern(word, pattern)]
    # Time: O(n * m)
    # Space: O(1)


def main():
    result = find_and_replace_pattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb")
    print(result) # ["mee","aqq"]

    result = find_and_replace_pattern(words = ["a","b","c"], pattern = "a")
    print(result) # ["a","b","c"]

if __name__ == "__main__":
    main()
