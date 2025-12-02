# ------------------------------------------------------------------
# 1737. Change Minimum Characters to Satisfy One of Three Conditions
# ------------------------------------------------------------------

# Problem: https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions
#
# You are given two strings a and b that consist of lowercase letters. In one
# operation, you can change any character in a or b to any lowercase letter.
# 
# Your goal is to satisfy one of the following three conditions:
#         
#   * Every letter in a is strictly less than every letter in b in the alphabet.
#   * Every letter in b is strictly less than every letter in a in the alphabet.
#   * Both a and b consist of only one distinct letter.
# 
# Return the minimum number of operations needed to achieve your goal.
# 
# Example 1:
# 
# Input: a = "aba", b = "caa"
# Output: 2
# 
# Explanation: Consider the best way to make each condition true:
# 1) Change b to "ccc" in 2 operations, then every letter in a is less than every
# letter in b.
# 2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is
# less than every letter in a.
# 3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one
# distinct letter.
# The best way was done in 2 operations (either condition 1 or condition 3).
# 
# Example 2:
# 
# Input: a = "dabadd", b = "cda"
# Output: 3
# 
# Explanation: The best way is to make condition 1 true by changing b to "eee".
# 
# 
# Constraints:
#         1 <= a.length, b.length <= 10⁵
#         a and b consist only of lowercase letters.


# Solution: https://algo.monster/liteproblems/1737
# Credit: AlgoMonster
def min_characters(a, b):
   
    def calculate_operations_for_separation(freq_first, freq_second):
        nonlocal min_operations
        
        # Try each character position as separator (1 corresponds to 'b', 25 to 'z')
        for separator_idx in range(1, 26):
            # Operations needed: 
            # - Change all chars >= separator in first string to something smaller
            # - Change all chars < separator in second string to something larger
            operations_needed = sum(freq_first[separator_idx:]) + sum(freq_second[:separator_idx])
            min_operations = min(min_operations, operations_needed)
    
    # Get string lengths
    len_a, len_b = len(a), len(b)
    
    # Initialize frequency arrays for both strings (26 letters)
    freq_a = [0] * 26
    freq_b = [0] * 26
    
    # Count character frequencies in string a
    for char in a:
        freq_a[ord(char) - ord('a')] += 1
        
    # Count character frequencies in string b
    for char in b:
        freq_b[ord(char) - ord('a')] += 1
    
    # Initialize minimum operations to worst case (changing all characters)
    min_operations = len_a + len_b
    
    # Condition 3: Check cost to make both strings consist of same single character
    # For each possible target character, calculate operations needed
    for count_a, count_b in zip(freq_a, freq_b):
        # Operations = total chars - chars already matching target character
        operations_for_same_char = len_a + len_b - count_a - count_b
        min_operations = min(min_operations, operations_for_same_char)
    
    # Condition 1: Make all chars in a < all chars in b
    calculate_operations_for_separation(freq_a, freq_b)
    
    # Condition 2: Make all chars in b < all chars in a
    calculate_operations_for_separation(freq_b, freq_a)
    
    return min_operations
    # Time: O(m + n)
    # Space: O(1)


def main():
    result = min_characters(a = "aba", b = "caa")
    print(result) # 2

    result = min_characters(a = "dabadd", b = "cda")
    print(result) # 3

if __name__ == "__main__":
    main()
