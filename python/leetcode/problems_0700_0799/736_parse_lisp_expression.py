# --------------------------
# 736. Parse Lisp Expression
# --------------------------

# Problem: https://leetcode.com/problems/parse-lisp-expression
#
# You are given a string expression representing a Lisp-like expression to return
# the integer value of.
# 
# The syntax for these expressions is given as follows.
#         
#   * An expression is either an integer, let expression, add expression, mult
#     expression, or an assigned variable. Expressions always evaluate to a single
#     integer.
#   * (An integer could be positive or negative.)
#   * A let expression takes the form "(let v1 e1 v2 e2 ... vn en expr)",
#     where let is always the string "let", then there are one or more pairs of
#     alternating variables and expressions, meaning that the first variable v1 is
#     assigned the value of the expression e1, the second variable v2 is assigned the
#     value of the expression e2, and so on sequentially; and then the value of this
#     let expression is the value of the expression expr.
#   * An add expression takes the form "(add e1 e2)" where add is always the
#     string "add", there are always two expressions e1, e2 and the result is the
#     addition of the evaluation of e1 and the evaluation of e2.
#   * A mult expression takes the form "(mult e1 e2)" where mult is always the
#     string "mult", there are always two expressions e1, e2 and the result is the
#     multiplication of the evaluation of e1 and the evaluation of e2.
#   * For this question, we will use a smaller subset of variable names. A
#     variable starts with a lowercase letter, then zero or more lowercase letters or
#     digits. Additionally, for your convenience, the names "add", "let", and "mult"
#     are protected and will never be used as variable names.
#   * Finally, there is the concept of scope. When an expression of a variable
#     name is evaluated, within the context of that evaluation, the innermost scope
#     (in terms of parentheses) is checked first for the value of that variable, and
#     then outer scopes are checked sequentially. It is guaranteed that every
#     expression is legal. Please see the examples for more details on the scope.
# 
# Example 1:
# 
# Input: expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
# Output: 14
# 
# Explanation: In the expression (add x y), when checking for the value of the
# variable x,
# we check from the innermost scope to the outermost in the context of the
# variable we are trying to evaluate.
# Since x = 3 is found first, the value of x is 3.
# 
# Example 2:
# 
# Input: expression = "(let x 3 x 2 x)"
# Output: 2
# 
# Explanation: Assignment in let statements is processed sequentially.
# 
# Example 3:
# 
# Input: expression = "(let x 1 y 2 x (add x y) (add x y))"
# Output: 5
# 
# Explanation: The first (add x y) evaluates as 3, and is assigned to x.
# The second (add x y) evaluates as 3+2 = 5.
# 
# 
# Constraints:
#         1 <= expression.length <= 2000
#         There are no leading or trailing spaces in expression.
#         All tokens are separated by a single space in expression.
#         The answer and all intermediate calculations of that answer are
#         guaranteed to fit in a 32-bit integer.
#         The expression is guaranteed to be legal and evaluate to an integer.

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/736
# Credit: AlgoMonster
def evaluate(expression):
    
    def parse_variable():
        nonlocal index
        start = index
        # Continue until we hit a space or closing parenthesis
        while index < length and expression[index] not in " )":
            index += 1
        return expression[start:index]
    
    def parse_integer():
        nonlocal index
        sign = 1
        value = 0
        
        # Handle negative numbers
        if expression[index] == "-":
            sign = -1
            index += 1
        
        # Build the integer digit by digit
        while index < length and expression[index].isdigit():
            value = value * 10 + int(expression[index])
            index += 1
        
        return sign * value
    
    def evaluate_expression():
        nonlocal index
        
        # Base cases: not an expression (either variable or integer)
        if expression[index] != "(":
            if expression[index].islower():
                # It's a variable, return its current value from scope
                var_name = parse_variable()
                return scope[var_name][-1]
            else:
                # It's an integer literal
                return parse_integer()
        
        # Skip opening parenthesis
        index += 1
        
        # Handle 'let' expression
        if expression[index] == "l":
            # Skip "let " (4 characters)
            index += 4
            variables_assigned = []
            
            while True:
                var_name = parse_variable()
                
                # Check if this is the final expression (no assignment)
                if expression[index] == ")":
                    # Return the value of the variable
                    result = scope[var_name][-1]
                    break
                
                # This variable gets assigned a value
                variables_assigned.append(var_name)
                index += 1  # Skip space
                
                # Evaluate the value to assign
                scope[var_name].append(evaluate_expression())
                index += 1  # Skip space
                
                # Check if next token is not a variable (final expression)
                if not expression[index].islower():
                    result = evaluate_expression()
                    break
            
            # Clean up scope - remove temporary variable bindings
            for var in variables_assigned:
                scope[var].pop()
        
        # Handle 'add' or 'mult' expression
        else:
            is_addition = expression[index] == "a"
            # Skip "add " (4 chars) or "mult " (5 chars)
            index += 4 if is_addition else 5
            
            # Evaluate first operand
            operand1 = evaluate_expression()
            index += 1  # Skip space
            
            # Evaluate second operand
            operand2 = evaluate_expression()
            
            # Perform the operation
            result = operand1 + operand2 if is_addition else operand1 * operand2
        
        # Skip closing parenthesis
        index += 1
        return result
    
    # Initialize parsing state
    index = 0
    length = len(expression)
    # Use defaultdict to maintain variable scope stack
    scope = defaultdict(list)
    
    # Start evaluation
    return evaluate_expression()
    # Time: O(n)
    # Space: O(n)


def main():
    result = evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))")
    print(result) # 14

    result = evaluate("(let x 3 x 2 x)")
    print(result) # 2

    result = evaluate("(let x 1 y 2 x (add x y) (add x y))")
    print(result) # 5

if __name__ == "__main__":
    main()
