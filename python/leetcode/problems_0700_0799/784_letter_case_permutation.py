# ----------------------------
# 784. Letter Case Permutation
# ----------------------------

# Problem: https://leetcode.com/problems/letter-case-permutation
#
# Given a string s, you can transform every letter individually to be lowercase or
# uppercase to create another string.
# 
# Return a list of all possible strings we could create. Return the output in any
# order.
# 
# Example 1:
# 
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# 
# Example 2:
# 
# Input: s = "3z4"
# Output: ["3z4","3Z4"]
# 
# 
# Constraints:
#       1 <= s.length <= 12
#       s consists of lowercase English letters, uppercase English letters, and digits.


# Solution: https://algo.monster/liteproblems/784
# Credit: AlgoMonster
def letter_case_permutation(s):
    def backtrack(index):
        # Base case: if we've processed all characters, add the current permutation to results
        if index >= len(char_list):
            result.append("".join(char_list))
            return
        
        # Recursive case 1: keep the current character as is
        backtrack(index + 1)
        
        # Recursive case 2: if the current character is a letter, toggle its case
        if char_list[index].isalpha():
            # Toggle case using XOR with 32 (difference between uppercase and lowercase ASCII values)
            char_list[index] = chr(ord(char_list[index]) ^ 32)
            backtrack(index + 1)
            # Backtrack: restore the original character for other branches
            char_list[index] = chr(ord(char_list[index]) ^ 32)
    
    # Convert string to list for in-place modifications
    char_list = list(s)
    # Store all letter case permutations
    result = []
    # Start the backtracking process from index 0
    backtrack(0)
    
    return result
    # Time: O(n * 2ⁿ)
    # Space: O(n * 2ⁿ)


def main():
    result = letter_case_permutation(s = "a1b2")
    print(result) # ["a1b2","a1B2","A1b2","A1B2"]

    result = letter_case_permutation(s = "3z4")
    print(result) # ["3z4","3Z4"]

if __name__ == "__main__":
    main()
