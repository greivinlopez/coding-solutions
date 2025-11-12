# -------------------------
# 856. Score of Parentheses
# -------------------------

# Problem: https://leetcode.com/problems/score-of-parentheses
#
# Given a balanced parentheses string s, return the score of the string.
# 
# The score of a balanced parentheses string is based on the following rule:
# 
#         "()" has score 1.
#         AB has score A + B, where A and B are balanced parentheses strings.
#         (A) has score 2 * A, where A is a balanced parentheses string.
# 
# Example 1:
# 
# Input: s = "()"
# Output: 1
# 
# Example 2:
# 
# Input: s = "(())"
# Output: 2
# 
# Example 3:
# 
# Input: s = "()()"
# Output: 2
# 
# 
# Constraints:
#         2 <= s.length <= 50
#         s consists of only '(' and ')'.
#         s is a balanced parentheses string.


# Solution: https://algo.monster/liteproblems/856
# Credit: AlgoMonster
def score_of_parentheses(s):
    # Initialize total score and current depth level
    total_score = 0
    depth = 0
    
    # Iterate through each character with its index
    for index, char in enumerate(s):
        if char == '(':
            # Opening parenthesis increases nesting depth
            depth += 1
        else:  # char == ')'
            # Closing parenthesis decreases nesting depth
            depth -= 1
            
            # Check if this closing parenthesis forms "()" pattern
            if s[index - 1] == '(':
                # A "()" at depth d contributes 2^d to the score
                # Using bit shift: 1 << depth is equivalent to 2^depth
                total_score += 1 << depth
    
    return total_score
    # Time: O(n)
    # Space: O(1)


def main():
    result = score_of_parentheses(s = "()")
    print(result) # 1

    result = score_of_parentheses(s = "(())")
    print(result) # 2

    result = score_of_parentheses(s = "()()")
    print(result) # 2

if __name__ == "__main__":
    main()
