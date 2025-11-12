# ---------------------------------------------------------
# 1190. Reverse Substrings Between Each Pair of Parentheses
# ---------------------------------------------------------

# Problem: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses
#
# You are given a string s that consists of lower case English letters and brackets.
# 
# Reverse the strings in each pair of matching parentheses, starting from the
# innermost one.
# 
# Your result should not contain any brackets.
# 
# Example 1:
# 
# Input: s = "(abcd)"
# Output: "dcba"
# 
# Example 2:
# 
# Input: s = "(u(love)i)"
# Output: "iloveu"
# 
# Explanation: The substring "love" is reversed first, then the whole string is
# reversed.
# 
# Example 3:
# 
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# 
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the
# whole string.
# 
# 
# Constraints:
#         1 <= s.length <= 2000
#         s only contains lower case English characters and parentheses.
#         It is guaranteed that all parentheses are balanced.


# Solution: https://youtu.be/n_pCJmg-RyU
# Credit: Navdeep Singh founder of NeetCode
def reverse_parentheses(s):
    pair = {}
    stack = []
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            j = stack.pop()
            pair[i] = j
            pair[j] = i

    i, direction = 0, 1
    res = []
    while i < len(s):
        if s[i] == "(" or s[i] == ")":
            i = pair[i]
            direction = -direction
        else:
            res.append(s[i])
        i += direction

    return "".join(res)
    # Time: O(n)
    # Space: O(n)


def main():
    result = reverse_parentheses("(abcd)")
    print(result) # "dcba"

    result = reverse_parentheses("(u(love)i)")
    print(result) # "iloveu"

    result = reverse_parentheses("(ed(et(oc))el)")
    print(result) # "leetcode"

if __name__ == "__main__":
    main()
