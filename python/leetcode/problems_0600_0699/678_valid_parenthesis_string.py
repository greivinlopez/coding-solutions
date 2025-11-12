# -----------------------------
# 678. Valid Parenthesis String
# -----------------------------

# Problem: https://leetcode.com/problems/valid-parenthesis-string/
# 
# Given a string s containing only three types of characters: '(', ')' and '*', 
# return true if s is valid.
# 
# The following rules define a valid string:
# 
# 	- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# 	- Any right parenthesis ')' must have a corresponding left parenthesis '('.
# 	- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# 	- '*' could be treated as a single right parenthesis ')' or a single left 
#     parenthesis '(' or an empty string "".
# 
#  
# Example 1:
# 
# Input: s = "()"
# Output: true
# 
# Example 2:
# 
# Input: s = "(*)"
# Output: true
# 
# Example 3:
# 
# Input: s = "(*))"
# Output: true
# 
#  
# Constraints:
# 
# 	1 <= s.length <= 100
# 	s[i] is '(', ')' or '*'.


# Solution: https://youtu.be/QhPdNS143Qg
# Credit: Navdeep Singh founder of NeetCode
def check_valid_string(s):
    # Dynamic Programming: O(n^2)
    dp = {(len(s), 0): True}  # key=(i, leftCount) -> isValid

    def dfs(i, left):
        if i == len(s) or left < 0:
            return left == 0
        if (i, left) in dp:
            return dp[(i, left)]

        if s[i] == "(":
            dp[(i, left)] = dfs(i + 1, left + 1)
        elif s[i] == ")":
            dp[(i, left)] = dfs(i + 1, left - 1)
        else:
            dp[(i, left)] = (
                dfs(i + 1, left + 1) or dfs(i + 1, left - 1) or dfs(i + 1, left)
            )
        return dp[(i, left)]

    return dfs(0, 0)


# Greedy: O(n)
def check_valid_string_greedy(s):
    leftMin, leftMax = 0, 0

    for c in s:
        if c == "(":
            leftMin, leftMax = leftMin + 1, leftMax + 1
        elif c == ")":
            leftMin, leftMax = leftMin - 1, leftMax - 1
        else:
            leftMin, leftMax = leftMin - 1, leftMax + 1
        if leftMax < 0:
            return False
        if leftMin < 0:  # required because -> s = ( * ) (
            leftMin = 0
    return leftMin == 0


def main():
    result = check_valid_string_greedy("()")
    print(result) # True

    result = check_valid_string_greedy("(*)")
    print(result) # True

    result = check_valid_string_greedy("(*))")
    print(result) # True

if __name__ == "__main__":
    main()
