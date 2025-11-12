# ------------------------
# 770. Basic Calculator IV
# ------------------------

# Problem: https://leetcode.com/problems/basic-calculator-iv
#
# Given an expression such as expression = "e + 8 - a + 5" and an evaluation map
# such as {"e": 1} (given in terms of evalvars = ["e"] and evalints = [1]), return
# a list of tokens representing the simplified expression, such as ["-1*a","14"]
#         
#   * An expression alternates chunks and symbols, with a space separating
#     each chunk and symbol.
#   * A chunk is either an expression in parentheses, a variable, or a non-
#     negative integer.
#   * A variable is a string of lowercase letters (not including digits.) Note
#     that variables can be multiple letters, and note that variables never have a
#     leading coefficient or unary operator like "2x" or "-x".
# 
# Expressions are evaluated in the usual order: brackets first, then
# multiplication, then addition and subtraction.
#         
#   * For example, expression = "1 + 2 * 3" has an answer of ["7"].
# 
# The format of the output is as follows:
#         
#   * For each term of free variables with a non-zero coefficient, we write
#     the free variables within a term in sorted order lexicographically.
#       * For example, we would never write a term like "b*a*c", only "a*b*c".
#   * Terms have degrees equal to the number of free variables being
#     multiplied, counting multiplicity. We write the largest degree terms of our
#     answer first, breaking ties by lexicographic order ignoring the leading
#     coefficient of the term.
#       * For example, "a*a*b*c" has degree 4.
#   * The leading coefficient of the term is placed directly to the left with
#     an asterisk separating it from the variables (if they exist.) A leading
#     coefficient of 1 is still printed.
#   * An example of a well-formatted answer is ["-2*a*a*a", "3*a*a*b",
#    "3*b*b", "4*a", "5*c", "-6"].
#   * Terms (including constant terms) with coefficient 0 are not included.
#       * For example, an expression of "0" has an output of [].
# 
# Note: You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-231, 231 - 1].
# 
# Example 1:
# 
# Input: expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
# Output: ["-1*a","14"]
# 
# Example 2:
# 
# Input: expression = "e - 8 + temperature - pressure", evalvars = ["e",
# "temperature"], evalints = [1, 12]
# Output: ["-1*pressure","5"]
# 
# Example 3:
# 
# Input: expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
# Output: ["1*e*e","-64"]
# 
# 
# Constraints:
#         1 <= expression.length <= 250
#         expression consists of lowercase English letters, digits, '+', '-', '*',
# '(', ')', ' '.
#         expression does not contain any leading or trailing spaces.
#         All the tokens in expression are separated by a single space.
#         0 <= evalvars.length <= 100
#         1 <= evalvars[i].length <= 20
#         evalvars[i] consists of lowercase English letters.
#         evalints.length == evalvars.length
#         -100 <= evalints[i] <= 100

import re

# Solution: https://leetcode.com/problems/basic-calculator-iv/solutions/5532691/the-easiest-readable-solution-based-on-basic-calculator-iii
# Credit: Hieu Minh Nguyen -> https://leetcode.com/u/therealhieu/
class Expression:
    def __init__(self, value = None):
        self.value = value if value else {}

    def __sub__(self, other):
        res = dict(self.value)

        for var, coef in other.value.items():
            res[var] = res.get(var, 0) - coef

        return Expression(value=res)

    def __add__(self, other):
        res = dict(self.value)

        for var, coef in other.value.items():
            res[var] = res.get(var, 0) + coef

        return Expression(value=res)

    def __mul__(self, other):
        res = {}
        for var1, coef1 in self.value.items():
            for var2, coef2 in other.value.items():
                new_var = tuple(sorted(var1 + var2))
                res[new_var] = res.get(new_var, 0) + coef1 * coef2
        return Expression(value=res)

    def __neg__(self):
        return Expression() - self

def basic_calculator_IV(expression, evalvars, evalints):
    varmap = dict(zip(evalvars, evalints))

    def tokenize(expression):
        return re.findall(r'[a-z]+|[0-9]+|[\+\-\*\(\)]', expression)

    def process_tokens(tokens) -> Expression:
        stack = []
        xpr = Expression()
        last_op = '+'
        ops = {'+', '-', '*'}

        def apply_op(op: str, expr: Expression) -> None:
            if op == '+':
                stack.append(expr)
            elif op == '-':
                stack.append(-expr)
            elif op == '*':
                stack.append(stack.pop() * expr)

        for token in tokens:
            if token.isdigit():
                xpr = Expression(value={(): int(token)})
            elif token.isalpha():
                if token in varmap:
                    xpr = Expression(value={(): varmap[token]})
                else:
                    xpr = Expression(value={(token,): 1})
            elif token in ops:
                apply_op(last_op, xpr)
                xpr = Expression()
                last_op = token
            elif token == '(':
                stack.append(last_op)
                last_op = '+'
            elif token == ')':
                apply_op(last_op, xpr)
                xpr = Expression()

                while isinstance(stack[-1], Expression):
                    xpr += stack.pop()

                last_op = stack.pop()

        apply_op(last_op, xpr)
        return sum(stack, Expression())

    def format_result(result):
        formatted = []

        for var, coef in sorted(
            result.value.items(),
            key=lambda x: (-len(x[0]), x[0])):
            if coef:
                formatted.append(f'{coef}' + ('*' + '*'.join(var) if var else ''))

        return formatted

    tokens = tokenize(expression)
    result = process_tokens(tokens)

    return format_result(result)


def main():
    result = basic_calculator_IV("e + 8 - a + 5", ["e"], [1])
    print(result) # ["-1*a","14"]

    result = basic_calculator_IV(expression = "e - 8 + temperature - pressure", evalvars = ["e", "temperature"], evalints = [1, 12])
    print(result) # ["-1*pressure","5"]

    result = basic_calculator_IV(expression = "(e + 8) * (e - 8)", evalvars = [], evalints = [])
    print(result) # ["1*e*e","-64"]

if __name__ == "__main__":
    main()
