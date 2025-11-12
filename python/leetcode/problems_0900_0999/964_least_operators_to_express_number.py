# --------------------------------------
# 964. Least Operators to Express Number
# --------------------------------------

# Problem: https://leetcode.com/problems/least-operators-to-express-number
#
# Given a single positive integer x, we will write an expression of the form x
# (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either
# addition, subtraction, multiplication, or division (+, -, *, or /). For example,
# with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.
# 
# When writing such an expression, we adhere to the following conventions:
#         
#   * The division operator (/) returns rational numbers.
#   * There are no parentheses placed anywhere.
#   * We use the usual order of operations: multiplication and division happen
#     before addition and subtraction.
#   * It is not allowed to use the unary negation operator (-). For example,
#     "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not
#     because it uses negation.
# 
# We would like to write an expression with the least number of operators such
# that the expression equals the given target. Return the least number of
# operators used.
# 
# Example 1:
# 
# Input: x = 3, target = 19
# Output: 5
# 
# Explanation: 3 * 3 + 3 * 3 + 3 / 3.
# The expression contains 5 operations.
# 
# Example 2:
# 
# Input: x = 5, target = 501
# Output: 8
# 
# Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.
# The expression contains 8 operations.
# 
# Example 3:
# 
# Input: x = 100, target = 100000000
# Output: 3
# 
# Explanation: 100 * 100 * 100 * 100.
# The expression contains 3 operations.
# 
# 
# Constraints:
#         2 <= x <= 100
#         1 <= target <= 2 * 10⁸


# Solution: https://algo.monster/liteproblems/964
# Credit: AlgoMonster
def least_ops_express_target(x, target):
    from functools import cache
    
    @cache
    def dfs(current_value):
        # Base case: when x is greater than or equal to current_value
        if x >= current_value:
            # Option 1: Use addition with x/x (1) repeated current_value times
            # Each 1 needs one division operator, plus (current_value - 1) additions
            option_add_ones = current_value * 2 - 1
            
            # Option 2: Use x minus some number of 1s
            # One subtraction for x, then (x - current_value) divisions for 1s,
            # plus (x - current_value - 1) subtractions between 1s
            option_subtract_from_x = 2 * (x - current_value)
            
            return min(option_add_ones, option_subtract_from_x)
        
        # Find the smallest power k where x^k >= current_value
        power = 2
        while x ** power < current_value:
            power += 1
        
        # Check if it's better to overshoot and subtract or undershoot and add
        if x ** power - current_value < current_value:
            # If overshooting is closer, we have two options:
            # Option 1: Use x^power and subtract the difference
            option_overshoot = power + dfs(x ** power - current_value)
            
            # Option 2: Use x^(power-1) and add the difference
            option_undershoot = power - 1 + dfs(current_value - x ** (power - 1))
            
            return min(option_overshoot, option_undershoot)
        else:
            # If undershooting is closer or equal, use x^(power-1) and add
            return power - 1 + dfs(current_value - x ** (power - 1))
    
    return dfs(target)
    # Time: O(log²(n))
    # Space: O(log(n))
    # n = target


def main():
    result = least_ops_express_target(x = 3, target = 19)
    print(result) # 5

    result = least_ops_express_target(x = 5, target = 501)
    print(result) # 8

    result = least_ops_express_target(x = 100, target = 100000000)
    print(result) # 3

if __name__ == "__main__":
    main()
