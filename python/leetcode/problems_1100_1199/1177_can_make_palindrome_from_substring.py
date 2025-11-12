# ----------------------------------------
# 1177. Can Make Palindrome from Substring
# ----------------------------------------

# Problem: https://leetcode.com/problems/can-make-palindrome-from-substring
#
# You are given a string s and array queries where queries[i] = [leftᵢ, rightᵢ, kᵢ]. 
# We may rearrange the substring s[lefti...righti] for each query and then
# choose up to kᵢ of them to replace with any lowercase English letter.
# 
# If the substring is possible to be a palindrome string after the operations
# above, the result of the query is true. Otherwise, the result is false.
# 
# Return a boolean array answer where answer[i] is the result of the iᵗʰ query
# queries[i].
# 
# Note that each letter is counted individually for replacement, so if, for
# example s[leftᵢ...rightᵢ] = "aaa", and kᵢ = 2, we can only replace two of the
# letters. Also, note that no query modifies the initial string s.
# 
# Example :
# 
# Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
# Output: [true,false,false,true,true]
# 
# Explanation:
# queries[0]: substring = "d", is palidrome.
# queries[1]: substring = "bc", is not palidrome.
# queries[2]: substring = "abcd", is not palidrome after replacing only 1
# character.
# queries[3]: substring = "abcd", could be changed to "abba" which is palidrome.
# Also this can be changed to "baab" first rearrange it "bacd" then replace "cd"
# with "ab".
# queries[4]: substring = "abcda", could be changed to "abcba" which is palidrome.
# 
# Example 2:
# 
# Input: s = "lyb", queries = [[0,1,0],[2,2,1]]
# Output: [false,true]
# 
# 
# Constraints:
#         1 <= s.length, queries.length <= 10⁵
#         0 <= leftᵢ <= rightᵢ < s.length
#         0 <= kᵢ <= s.length
#         s consists of lowercase English letters.


# Solution: https://algo.monster/liteproblems/1177
# Credit: AlgoMonster
def can_make_pali_queries(s, queries):
    string_length = len(s)
    
    # Build prefix sum array for character frequencies
    # prefix_counts[i][j] represents count of character j in s[0:i]
    prefix_counts = [[0] * 26 for _ in range(string_length + 1)]
    
    # Populate prefix sum array
    for index, char in enumerate(s, start=1):
        # Copy previous counts
        prefix_counts[index] = prefix_counts[index - 1][:]
        # Increment count for current character
        char_position = ord(char) - ord('a')
        prefix_counts[index][char_position] += 1
    
    # Process each query
    result = []
    for left, right, max_changes in queries:
        # Count characters with odd frequency in substring s[left:right+1]
        odd_count = 0
        for char_index in range(26):
            # Get frequency of character in substring using prefix sums
            char_frequency = prefix_counts[right + 1][char_index] - prefix_counts[left][char_index]
            # Check if frequency is odd
            if char_frequency & 1:  # Bitwise AND with 1 checks if odd
                odd_count += 1
        
        # For a palindrome, at most 1 character can have odd frequency
        # We need to pair up odd_count // 2 characters
        # Check if we can fix unpaired characters with available changes
        can_form_palindrome = (odd_count // 2) <= max_changes
        result.append(can_form_palindrome)
    
    return result
    # Time: O(n + m)
    # Space: O(1)


def main():
    result = can_make_pali_queries(s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]])
    print(result) # [True, False, False, True, True]

    result = can_make_pali_queries(s = "lyb", queries = [[0,1,0],[2,2,1]])
    print(result) # [False, True]

if __name__ == "__main__":
    main()
