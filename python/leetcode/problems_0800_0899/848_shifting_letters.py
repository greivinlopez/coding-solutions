# ---------------------
# 848. Shifting Letters
# ---------------------

# Problem: https://leetcode.com/problems/shifting-letters
#
# You are given a string s of lowercase English letters and an integer array
# shifts of the same length.
# 
# Call the shift() of a letter, the next letter in the alphabet, (wrapping around
# so that 'z' becomes 'a').
#         
#   * For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
# 
# Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x
# times.
# 
# Return the final string after all such shifts to s are applied.
# 
# Example 1:
# 
# Input: s = "abc", shifts = [3,5,9]
# Output: "rpl"
# 
# Explanation: We start with "abc".
# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.
# 
# Example 2:
# 
# Input: s = "aaa", shifts = [1,2,3]
# Output: "gfd"
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s consists of lowercase English letters.
#         shifts.length == s.length
#         0 <= shifts[i] <= 10⁹

from string import ascii_lowercase

# Solution: https://algo.monster/liteproblems/848
# Credit: AlgoMonster
def shifting_letters(s, shifts):
    # Get the length of the string
    length = len(s)
    
    # Convert string to list for in-place modification
    char_list = list(s)
    
    # Initialize cumulative shift counter
    cumulative_shift = 0
    
    # Process characters from right to left
    for index in range(length - 1, -1, -1):
        # Add current shift value to cumulative sum
        cumulative_shift += shifts[index]
        
        # Calculate the new character position after shifting
        # Convert character to 0-based index (a=0, b=1, ..., z=25)
        current_char_index = ord(char_list[index]) - ord('a')
        
        # Apply the cumulative shift and wrap around using modulo 26
        new_char_index = (current_char_index + cumulative_shift) % 26
        
        # Replace the character with the shifted one
        char_list[index] = ascii_lowercase[new_char_index]
    
    # Convert the list back to string and return
    return ''.join(char_list)
    # Time: O(n)
    # Space: O(n) for the total space used, or O(1) if we don't count the space needed for the output. 


def main():
    result = shifting_letters(s = "abc", shifts = [3,5,9])
    print(result) # "rpl"

    result = shifting_letters(s = "aaa", shifts = [1,2,3])
    print(result) # "gfd"

if __name__ == "__main__":
    main()
