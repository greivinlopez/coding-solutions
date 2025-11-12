# ---------------------
# 20. Valid Parentheses
# ---------------------

# Problem: https://leetcode.com/problems/valid-parentheses
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# 
# An input string is valid if:
# 
#         Open brackets must be closed by the same type of brackets.
#         Open brackets must be closed in the correct order.
#         Every close bracket has a corresponding open bracket of the same type.
# 
# Example 1:
# 
# Input: s = "()"
# Output: true
# 
# Example 2:
# 
# Input: s = "()[]{}"
# Output: true
# 
# Example 3:
# 
# Input: s = "(]"
# Output: false
# 
# Example 4:
# 
# Input: s = "([])"
# Output: true
# 
# Example 5:
# 
# Input: s = "([)]"
# Output: false
# 
# 
# Constraints:
#         1 <= s.length <= 10⁴
#         s consists of parentheses only '()[]{}'.

# Solution: https://youtu.be/WTzjTskDFMg
# Credit: Navdeep Singh founder of NeetCode 
def is_valid(s):
    bracketMap = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c not in bracketMap:
            stack.append(c)
            continue
        if not stack or stack[-1] != bracketMap[c]:
            return False
        stack.pop()

    return not stack
    # Time: O(n)
    # Space: O(n)

# Solution: https://youtu.be/7-_V-ufnF4c
# Credit: Greg Hogg
# Almost identical
def is_valid_alt(s):
    hashmap = {")": "(", "}": "{", "]": "["}
    stk = []

    for c in s:
        if c not in hashmap:
            stk.append(c)
        else:
            if not stk:
                return False
            else:
                popped = stk.pop()
                if popped != hashmap[c]:
                    return False

    return not stk
    # Time: O(n)
    # Space: O(n)


def main():
    result = is_valid("()") # True
    print(result)
    result = is_valid("()[]{}") # True
    print(result)
    result = is_valid("(]") # False
    print(result)
    result = is_valid("([])") # True
    print(result)
    result = is_valid("([)]") # False
    print(result)

if __name__ == "__main__":
    main()