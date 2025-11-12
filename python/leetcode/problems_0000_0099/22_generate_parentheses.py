# ------------------------
# 22. Generate Parentheses
# ------------------------

# Problem: https://leetcode.com/problems/generate-parentheses
#
# Given n pairs of parentheses, write a function to generate all combinations of
# well-formed parentheses.
# 
# Example 1:
# 
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# 
# Example 2:
# 
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
#         1 <= n <= 8

# Solution: https://youtu.be/s9fokUqJ76A
# Credit: Navdeep Singh founder of NeetCode 
def generate_parenthesis(n):
    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res
    # Time: O(4ⁿ)
    # Space: O(n)

# Alternative Solution: https://youtu.be/oC4saZRNwfI
# Credit: Greg Hogg
# Almost identical
def generate_parenthesis_alt(n):
    ans, sol = [], []

    def backtrack(openn, close):
        if len(sol) == 2 * n:
            ans.append("".join(sol))
            return
        if openn < n:
            sol.append("(")
            backtrack(openn + 1, close)
            sol.pop()

        if openn > close:
            sol.append(")")
            backtrack(openn, close + 1)
            sol.pop()

    backtrack(0, 0)
    return ans
    # Time: O(4ⁿ)
    # Space: O(n)


def main():
    result = generate_parenthesis(3) # ["((()))","(()())","(())()","()(())","()()()"]
    print(result)
    result = generate_parenthesis(1) # ["()"]
    print(result)

if __name__ == "__main__":
    main()