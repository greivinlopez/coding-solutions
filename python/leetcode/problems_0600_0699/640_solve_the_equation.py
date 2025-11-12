# -----------------------
# 640. Solve the Equation
# -----------------------

# Problem: https://leetcode.com/problems/solve-the-equation
#
# Solve a given equation and return the value of 'x' in the form of a string
# "x=#value". The equation contains only '+', '-' operation, the variable 'x' and
# its coefficient. You should return "No solution" if there is no solution for the
# equation, or "Infinite solutions" if there are infinite solutions for the
# equation.
# 
# If there is exactly one solution for the equation, we ensure that the value of
# 'x' is an integer.
# 
# Example 1:
# 
# Input: equation = "x+5-3+x=6+x-2"
# Output: "x=2"
# 
# Example 2:
# 
# Input: equation = "x=x"
# Output: "Infinite solutions"
# 
# Example 3:
# 
# Input: equation = "2x=x"
# Output: "x=0"
# 
# 
# Constraints:
#   * 3 <= equation.length <= 1000
#   * equation has exactly one '='.
#   * equation consists of integers with an absolute value in the range [0, 100] 
#     without any leading zeros, and the variable 'x'.
#   * The input is generated that if there is a single solution, it will be an
#     integer.


# Solution: https://algo.monster/liteproblems/640
# Credit: AlgoMonster
def solve_equation(equation):
    def parse_expression(expression):
        x_coefficient = 0
        constant_term = 0
        
        # Add leading '+' if expression doesn't start with a sign
        if expression[0] != '-':
            expression = '+' + expression
        
        i = 0
        n = len(expression)
        
        while i < n:
            # Determine the sign of current term
            sign = 1 if expression[i] == '+' else -1
            i += 1
            
            # Find the end of current term
            j = i
            while j < n and expression[j] not in '+-':
                j += 1
            
            # Extract the current term
            term = expression[i:j]
            
            # Process the term based on whether it contains 'x'
            if term[-1] == 'x':
                # Term is a coefficient of x
                if len(term) > 1:
                    # Extract coefficient before 'x'
                    x_coefficient += sign * int(term[:-1])
                else:
                    # Just 'x' means coefficient is 1
                    x_coefficient += sign * 1
            else:
                # Term is a constant
                constant_term += sign * int(term)
            
            # Move to next term
            i = j
        
        return x_coefficient, constant_term
    
    # Split equation into left and right sides
    left_side, right_side = equation.split('=')
    
    # Parse both sides of the equation
    left_x_coeff, left_const = parse_expression(left_side)
    right_x_coeff, right_const = parse_expression(right_side)
    
    # Rearrange equation to form: (left_x - right_x) * x = right_const - left_const
    final_x_coeff = left_x_coeff - right_x_coeff
    final_const = right_const - left_const
    
    # Check for special cases
    if final_x_coeff == 0:
        # No x terms after simplification
        if final_const == 0:
            # 0 = 0, any x is a solution
            return 'Infinite solutions'
        else:
            # 0 = non-zero, no solution exists
            return 'No solution'
    
    # Normal case: solve for x
    x_value = final_const // final_x_coeff
    return f'x={x_value}'
    # Time: O(n)
    # Space: O(n)


def main():
    result = solve_equation(equation = "x+5-3+x=6+x-2")
    print(result) # "x=2"

    result = solve_equation(equation = "x=x")
    print(result) # "Infinite solutions"

    result = solve_equation(equation = "2x=x")
    print(result) # "x=0"

if __name__ == "__main__":
    main()
