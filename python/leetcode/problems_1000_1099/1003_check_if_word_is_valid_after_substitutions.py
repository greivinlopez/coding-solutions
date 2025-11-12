# ------------------------------------------------
# 1003. Check If Word Is Valid After Substitutions
# ------------------------------------------------

# Problem: https://leetcode.com/problems/check-if-word-is-valid-after-substitutions
#
# Given a string s, determine if it is valid.
# 
# A string s is valid if, starting with an empty string t = "", you can transform
# t into s after performing the following operation any number of times:
#         
#   * Insert string "abc" into any position in t. More formally, t becomes
#     tₗₑբₜ + "abc" + tᵣᵢ₉ₕₜ, where t == tₗₑբₜ + tᵣᵢ₉ₕₜ. Note that tₗₑբₜ and tᵣᵢ₉ₕₜ
#     may be empty.
# 
# Return true if s is a valid string, otherwise, return false.
# 
# Example 1:
# 
# Input: s = "aabcbc"
# Output: true
# 
# Explanation:
# "" -> "abc" -> "aabcbc"
# Thus, "aabcbc" is valid.
# 
# Example 2:
# 
# Input: s = "abcabcababcc"
# Output: true
# 
# Explanation:
# "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
# Thus, "abcabcababcc" is valid.
# 
# Example 3:
# 
# Input: s = "abccba"
# Output: false
# 
# Explanation: It is impossible to get "abccba" using the operation.
# 
# 
# Constraints:
#         1 <= s.length <= 2 * 10⁴
#         s consists of letters 'a', 'b', and 'c'


# Solution: https://algo.monster/liteproblems/1003
# Credit: AlgoMonster
def is_valid(s):
    # If string length is not divisible by 3, it cannot be valid
    # since we need to remove "abc" sequences which are 3 characters each
    if len(s) % 3 != 0:
        return False
    
    # Use a stack to track characters
    stack = []
    
    # Process each character in the string
    for char in s:
        # Add current character to stack
        stack.append(char)
        
        # Check if the last 3 characters form "abc"
        # If so, remove them from the stack
        if ''.join(stack[-3:]) == 'abc':
            stack[-3:] = []
    
    # String is valid if stack is empty after processing
    # (all "abc" sequences have been successfully removed)
    return len(stack) == 0
    # Time: O(n)
    # Space: O(n)


def main():
    result = is_valid(s = "aabcbc")
    print(result) # True

    result = is_valid(s = "abcabcababcc")
    print(result) # True

    result = is_valid(s = "abccba")
    print(result) # False

if __name__ == "__main__":
    main()
