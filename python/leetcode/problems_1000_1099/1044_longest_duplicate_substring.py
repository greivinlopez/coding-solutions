# ---------------------------------
# 1044. Longest Duplicate Substring
# ---------------------------------

# Problem: https://leetcode.com/problems/longest-duplicate-substring
#
# Given a string s, consider all duplicated substrings: (contiguous) substrings of
# s that occur 2 or more times. The occurrences may overlap.
# 
# Return any duplicated substring that has the longest possible length. If s does
# not have a duplicated substring, the answer is "".
# 
# Example 1:
# 
# Input: s = "banana"
# Output: "ana"
# 
# Example 2:
# 
# Input: s = "abcd"
# Output: ""
# 
# 
# Constraints:
#         2 <= s.length <= 3 * 10⁴
#         s consists of lowercase English letters.


# Solution: https://algo.monster/liteproblems/1044
# Credit: AlgoMonster
def longest_dup_substring(s):

    def has_duplicate_of_length(length):
        seen_substrings = set()
        
        # Iterate through all possible substrings of given length
        for start_idx in range(string_length - length + 1):
            # Extract substring of current length starting at start_idx
            current_substring = s[start_idx : start_idx + length]
            
            # Check if we've seen this substring before
            if current_substring in seen_substrings:
                return current_substring
            
            # Add current substring to the set of seen substrings
            seen_substrings.add(current_substring)
        
        return ''
    
    # Initialize variables
    string_length = len(s)
    left_bound = 0
    right_bound = string_length
    longest_duplicate = ''
    
    # Binary search on the length of the duplicate substring
    while left_bound < right_bound:
        # Calculate mid point (ceiling division)
        mid_length = (left_bound + right_bound + 1) >> 1
        
        # Check if duplicate substring of mid_length exists
        found_substring = has_duplicate_of_length(mid_length)
        
        # Update longest_duplicate if a duplicate was found
        longest_duplicate = found_substring or longest_duplicate
        
        if found_substring:
            # If duplicate found, search for longer substrings
            left_bound = mid_length
        else:
            # If no duplicate found, search for shorter substrings
            right_bound = mid_length - 1
    
    return longest_duplicate
    # Time: O(n² * log n)
    # Space: O(n²)


def main():
    result = longest_dup_substring(s = "banana")
    print(result) # "ana"

    result = longest_dup_substring(s = "abcd")
    print(result) # ""

if __name__ == "__main__":
    main()
