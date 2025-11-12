# ----------------------------------
# 1021. Remove Outermost Parentheses
# ----------------------------------

# Problem: https://leetcode.com/problems/remove-outermost-parentheses
#
# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A
# and B are valid parentheses strings, and + represents string concatenation.
#         
#   * For example, "", "()", "(())()", and "(()(()))" are all valid
#     parentheses strings.
# 
# A valid parentheses string s is primitive if it is nonempty, and there does not
# exist a way to split it into s = A + B, with A and B nonempty valid parentheses
# strings.
# 
# Given a valid parentheses string s, consider its primitive decomposition: s = P1
# + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
# 
# Return s after removing the outermost parentheses of every primitive string in
# the primitive decomposition of s.
# 
# Example 1:
# 
# Input: s = "(()())(())"
# Output: "()()()"
# 
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" +
# "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# 
# Example 2:
# 
# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# 
# Explanation:
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())"
# + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())"
# = "()()()()(())".
# 
# Example 3:
# 
# Input: s = "()()"
# Output: ""
# 
# Explanation:
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s[i] is either '(' or ')'.
#         s is a valid parentheses string.


# Solution: https://algo.monster/liteproblems/1021
# Credit: AlgoMonster
def remove_outer_parentheses(s):
    result = []
    depth = 0  # Track the depth/level of nested parentheses
    
    for char in s:
        if char == '(':
            # Increment depth when encountering opening parenthesis
            depth += 1
            # Only add to result if it's not an outermost opening parenthesis
            # (depth > 1 means we're inside at least one pair already)
            if depth > 1:
                result.append(char)
        else:  # char == ')'
            # Decrement depth when encountering closing parenthesis
            depth -= 1
            # Only add to result if it's not an outermost closing parenthesis
            # (depth > 0 means we're still inside at least one pair)
            if depth > 0:
                result.append(char)
    
    return ''.join(result)
    # Time: O(n)
    # Space: O(n)


def main():
    result = remove_outer_parentheses(s = "(()())(())")
    print(result) # "()()()"

    result = remove_outer_parentheses(s = "(()())(())(()(()))")
    print(result) # "()()()()(())"

    result = remove_outer_parentheses(s = "()()")
    print(result) # ""

if __name__ == "__main__":
    main()
