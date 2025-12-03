# ----------------------------
# 1763. Longest Nice Substring
# ----------------------------

# Problem: https://leetcode.com/problems/longest-nice-substring
#
# A string s is nice if, for every letter of the alphabet that s contains, it
# appears both in uppercase and lowercase. For example, "abABB" is nice because
# 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b'
# appears, but 'B' does not.
# 
# Given a string s, return the longest substring of s that is nice. If there are
# multiple, return the substring of the earliest occurrence. If there are none,
# return an empty string.
# 
# Example 1:
# 
# Input: s = "YazaAay"
# Output: "aAa"
# 
# Explanation: "aAa" is a nice string because 'A/a' is the only letter of the
# alphabet in s, and both 'A' and 'a' appear.
# "aAa" is the longest nice substring.
# 
# Example 2:
# 
# Input: s = "Bb"
# Output: "Bb"
# 
# Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole
# string is a substring.
# 
# Example 3:
# 
# Input: s = "c"
# Output: ""
# 
# Explanation: There are no nice substrings.
# 
# 
# Constraints:
#         1 <= s.length <= 100
#         s consists of uppercase and lowercase English letters.


# Solution: https://algo.monster/liteproblems/1763
# Credit: AlgoMonster
def longest_nice_substring(s):
    n = len(s)
    result = ''
    
    # Try all possible starting positions
    for start in range(n):
        char_set = set()
        
        # Extend substring from current starting position
        for end in range(start, n):
            # Add current character to the set
            char_set.add(s[end])
            
            # Check if current substring is nice
            # A substring is nice if every character has both cases present
            is_nice = all(
                char.lower() in char_set and char.upper() in char_set 
                for char in char_set
            )
            
            current_length = end - start + 1
            
            # Update result if we found a longer nice substring
            if is_nice and len(result) < current_length:
                result = s[start:end + 1]
    
    return result
    # Time: O(n²)
    # Space: O(1)


def main():
    result = longest_nice_substring(s = "YazaAay")
    print(result) # "aAa"

    result = longest_nice_substring(s = "Bb")
    print(result) # "Bb"

    result = longest_nice_substring(s = "c")
    print(result) # ""

if __name__ == "__main__":
    main()
