# ----------------------------------------------
# 1147. Longest Chunked Palindrome Decomposition
# ----------------------------------------------

# Problem: https://leetcode.com/problems/longest-chunked-palindrome-decomposition
#
# You are given a string text. You should split it to k substrings (subtext₁,
# subtext₂, ..., subtextₖ) such that:
#         
#   * subtextᵢ is a non-empty string.
#   * The concatenation of all the substrings is equal to text (i.e., subtext₁
#     + subtext₂ + ... + subtextₖ == text).
#   * subtextᵢ == subtextₖ ₋ ᵢ ₊ ₁ for all valid values of i (i.e., 1 <= i <= k).
# 
# Return the largest possible value of k.
# 
# Example 1:
# 
# Input: text = "ghiabcdefhelloadamhelloabcdefghi"
# Output: 7
# 
# Explanation: We can split the string on
# "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
# 
# Example 2:
# 
# Input: text = "merchant"
# Output: 1
# 
# Explanation: We can split the string on "(merchant)".
# 
# Example 3:
# 
# Input: text = "antaprezatepzapreanta"
# Output: 11
# 
# Explanation: We can split the string on
# "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)".
# 
# 
# Constraints:
#         1 <= text.length <= 1000
#         text consists only of lowercase English characters.


# Solution: https://algo.monster/liteproblems/1147
# Credit: AlgoMonster
def longest_decomposition(text):
    chunk_count = 0
    left_pointer = 0
    right_pointer = len(text) - 1
    
    # Process the string from both ends towards the center
    while left_pointer <= right_pointer:
        substring_length = 1
        match_found = False
        
        # Try to find matching substrings of increasing length
        while left_pointer + substring_length - 1 < right_pointer - substring_length + 1:
            # Extract substring from left side
            left_substring = text[left_pointer:left_pointer + substring_length]
            # Extract substring from right side
            right_substring = text[right_pointer - substring_length + 1:right_pointer + 1]
            
            # Check if the substrings match
            if left_substring == right_substring:
                # Found matching chunks, count them as 2 pieces
                chunk_count += 2
                # Move pointers inward by the length of matched substring
                left_pointer += substring_length
                right_pointer -= substring_length
                match_found = True
                break
            
            # Try longer substring in next iteration
            substring_length += 1
        
        # If no matching substrings found, the remaining middle part counts as 1 chunk
        if not match_found:
            chunk_count += 1
            break
    
    return chunk_count
    # Time: O(n²)
    # Space: O(n)


def main():
    result = longest_decomposition(text = "ghiabcdefhelloadamhelloabcdefghi")
    print(result) # 7

    result = longest_decomposition(text = "merchant")
    print(result) # 1

    result = longest_decomposition(text = "antaprezatepzapreanta")
    print(result) # 11

if __name__ == "__main__":
    main()
