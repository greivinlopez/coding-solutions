# --------------------------------------------------
# 1297. Maximum Number of Occurrences of a Substring
# --------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring
#
# Given a string s, return the maximum number of occurrences of any substring
# under the following rules:
#         
#   * The number of unique characters in the substring must be less than or
#     equal to maxLetters.
#   * The substring size must be between minSize and maxSize inclusive.
# 
# Example 1:
# 
# Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
# Output: 2
# 
# Explanation: Substring "aab" has 2 occurrences in the original string.
# It satisfies the conditions, 2 unique letters and size 3 (between minSize and
# maxSize).
# 
# Example 2:
# 
# Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
# Output: 2
# 
# Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         1 <= maxLetters <= 26
#         1 <= minSize <= maxSize <= min(26, s.length)
#         s consists of only lowercase English letters.

from collections import Counter

# Solution: https://algo.monster/liteproblems/1297
# Credit: AlgoMonster
def max_freq(s, maxLetters, minSize, maxSize):
    # Initialize maximum frequency counter
    max_frequency = 0
    
    # Dictionary to count occurrences of each valid substring
    substring_counter = Counter()
    
    # Iterate through all possible substrings of length minSize
    for start_index in range(len(s) - minSize + 1):
        # Extract substring of length minSize starting at current position
        current_substring = s[start_index : start_index + minSize]
        
        # Count unique characters in the substring
        unique_chars = set(current_substring)
        
        # Check if substring satisfies the unique character constraint
        if len(unique_chars) <= maxLetters:
            # Increment count for this valid substring
            substring_counter[current_substring] += 1
            
            # Update maximum frequency if current count is higher
            max_frequency = max(max_frequency, substring_counter[current_substring])
    
    return max_frequency
    # Time: O(n * m)
    # Space: O(n * m)


def main():
    result = max_freq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4)
    print(result) # 2

    result = max_freq(s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3)
    print(result) # 2

if __name__ == "__main__":
    main()
