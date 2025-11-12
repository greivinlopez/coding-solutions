# ------------
# 679. 24 Game
# ------------

# Problem: https://leetcode.com/problems/24-game
#
# You are given an integer array cards of length 4. You have four cards, each
# containing a number in the range [1, 9]. You should arrange the numbers on these
# cards in a mathematical expression using the operators ['+', '-', '*', '/'] and
# the parentheses '(' and ')' to get the value 24.
# 
# You are restricted with the following rules:
#         
#   * The division operator '/' represents real division, not integer division.
#       * For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
#   * Every operation done is between two numbers. In particular, we cannot use '-' 
#     as a unary operator.
#       * For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is 
#         not allowed.
#   * You cannot concatenate numbers together
#       * For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
# 
# Return true if you can get such expression that evaluates to 24, and false otherwise.
# 
# Example 1:
# 
# Input: cards = [4,1,8,7]
# Output: true
# 
# Explanation: (8-4) * (7-1) = 24
# 
# Example 2:
# 
# Input: cards = [1,2,1,2]
# Output: false
# 
# 
# Constraints:
#         cards.length == 4
#         1 <= cards[i] <= 9


# Solution: https://leetcode.com/problems/24-game/
# Credit: AlgoMonster
def judge_point_24(cards):
 
    def can_reach_target(numbers):
        # Base case: if only one number left, check if it equals 24
        if len(numbers) == 1:
            # Use epsilon comparison for floating point equality
            return abs(numbers[0] - 24) < 1e-6
        
        # Try all pairs of numbers
        for first_idx in range(len(numbers)):
            for second_idx in range(len(numbers)):
                # Skip if same number (can't combine a number with itself)
                if first_idx == second_idx:
                    continue
                
                # Create new list excluding the two selected numbers
                remaining_numbers = [
                    numbers[k] 
                    for k in range(len(numbers)) 
                    if k != first_idx and k != second_idx
                ]
                
                # Try all four operations
                for operation in OPERATIONS:
                    if operation == "+":
                        # Addition: a + b
                        result = numbers[first_idx] + numbers[second_idx]
                    elif operation == "-":
                        # Subtraction: a - b
                        result = numbers[first_idx] - numbers[second_idx]
                    elif operation == "*":
                        # Multiplication: a * b
                        result = numbers[first_idx] * numbers[second_idx]
                    elif operation == "/":
                        # Division: a / b (check for division by zero)
                        if numbers[second_idx] == 0:
                            continue
                        result = numbers[first_idx] / numbers[second_idx]
                    
                    # Recursively check if we can reach 24 with the new set of numbers
                    if can_reach_target(remaining_numbers + [result]):
                        return True
        
        # No valid combination found
        return False
    
    # Define available operations
    OPERATIONS = ("+", "-", "*", "/")
    
    # Convert integers to floats for accurate division
    float_numbers = [float(card) for card in cards]
    
    # Start the recursive search
    return can_reach_target(float_numbers)
    # Time: O(1)
    # Space: O(1)


def main():
    result = judge_point_24(cards = [4,1,8,7])
    print(result) # True

    result = judge_point_24(cards = [1,2,1,2])
    print(result) # False

if __name__ == "__main__":
    main()
