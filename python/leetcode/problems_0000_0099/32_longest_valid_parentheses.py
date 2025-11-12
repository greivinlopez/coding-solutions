# -----------------------------
# 32. Longest Valid Parentheses
# -----------------------------

# Problem: https://leetcode.com/problems/longest-valid-parentheses
#
# Given a string containing just the characters '(' and ')', return the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# Input: s = "(()"
# Output: 2
# 
# Explanation: The longest valid parentheses substring is "()".
# 
# Example 2:
# 
# Input: s = ")()())"
# Output: 4
# 
# Explanation: The longest valid parentheses substring is "()()".
# 
# Example 3:
# 
# Input: s = ""
# Output: 0
# 
# 
# Constraints:
#         0 <= s.length <= 3 * 10⁴
#         s[i] is '(', or ')'.


# Credit: Jeel Gajera -> https://github.com/JeelGajera
def longest_valid_parentheses(s):
    stack = []
    max_length = 0
    stack.append(-1)

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    return max_length
    # Time: O(n)
    # Space: O(n)


def main():
    result = longest_valid_parentheses("(()")
    print(result) # 2

    result = longest_valid_parentheses(")()())")
    print(result) # 4

    result = longest_valid_parentheses("")
    print(result) # 0

if __name__ == "__main__":
    main()
