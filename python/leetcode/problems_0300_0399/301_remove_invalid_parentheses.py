# -------------------------------
# 301. Remove Invalid Parentheses
# -------------------------------

# Problem: https://leetcode.com/problems/remove-invalid-parentheses
#
# Given a string s that contains parentheses and letters, remove the minimum
# number of invalid parentheses to make the input string valid.
# 
# Return a list of unique strings that are valid with the minimum number of
# removals. You may return the answer in any order.
# 
# Example 1:
# 
# Input: s = "()())()"
# Output: ["(())()","()()()"]
# 
# Example 2:
# 
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]
# 
# Example 3:
# 
# Input: s = ")("
# Output: [""]
# 
# 
# Constraints:
#         1 <= s.length <= 25
#         s consists of lowercase English letters and parentheses '(' and ')'.
#         There will be at most 20 parentheses in s.


from functools import cache

# Solution: https://leetcode.com/problems/remove-invalid-parentheses/solutions/696750/python-backtracking-solution-detailed-explanation
# Credit: Antonio Carlos Salzvedel Furtado
def remove_invalid_parentheses(s):

    @cache
    def getInvalidBraces(s):
        braces = []
        for i, c in enumerate(s):
            if c == '(':
                braces.append((i, c))
            elif c == ')':
                if braces and braces[-1][1] == '(':
                    braces.pop()
                else:
                    braces.append((i, c))
        return braces
    
    @cache
    def dfs(s, left, right):
        if left == 0 and right == 0:
            if getInvalidBraces(s) == []:
                res.append(s)
        else:
            for i, c in enumerate(s):
                if c != '(' and c != ')':
                    continue
                if (c == '(' and left == 0) or (c == ')' and right == 0):
                    continue
                dfs(s[:i] + s[i+1:], left - (c == '('), right - (c == ')'))

    res = []      
    invalid = getInvalidBraces(s)
    left = sum([1 for _, c in invalid if c == '('])
    right = len(invalid) - left
    dfs(s, left, right)
    return res
    # Time: O(2ⁿ) 
    # Space: O(n * 2ⁿ)


def main():
    result = remove_invalid_parentheses(s = "()())()")
    print(result) # ["(())()","()()()"]

    result = remove_invalid_parentheses(s = "(a)())()")
    print(result) # ["(a())()","(a)()()"]

    result = remove_invalid_parentheses(s = ")(")
    print(result) # [""]

if __name__ == "__main__":
    main()
