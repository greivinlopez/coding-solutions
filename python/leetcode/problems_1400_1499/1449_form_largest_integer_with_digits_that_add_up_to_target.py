# ------------------------------------------------------------
# 1449. Form Largest Integer With Digits That Add up to Target
# ------------------------------------------------------------

# Problem: https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target
#
# Given an array of integers cost and an integer target, return the maximum
# integer you can paint under the following rules:
# 
#         The cost of painting a digit (i + 1) is given by cost[i] (0-indexed).
#         The total cost used must be equal to target.
#         The integer does not have 0 digits.
# 
# Since the answer may be very large, return it as a string. If there is no way to
# paint any integer given the condition, return "0".
# 
# Example 1:
# 
# Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
# Output: "7772"
# 
# Explanation: The cost to paint the digit '7' is 2, and the digit '2' is 3. Then
# cost("7772") = 2*3+ 3*1 = 9. You could also paint "977", but "7772" is the
# largest number.
# Digit    cost
#   1  ->   4
#   2  ->   3
#   3  ->   2
#   4  ->   5
#   5  ->   6
#   6  ->   7
#   7  ->   2
#   8  ->   5
#   9  ->   5
# 
# Example 2:
# 
# Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
# Output: "85"
# 
# Explanation: The cost to paint the digit '8' is 7, and the digit '5' is 5. Then
# cost("85") = 7 + 5 = 12.
# 
# Example 3:
# 
# Input: cost = [2,4,6,2,4,6,4,4,4], target = 5
# Output: "0"
# 
# Explanation: It is impossible to paint any integer with total cost equal to
# target.
# 
# 
# Constraints:
#         cost.length == 9
#         1 <= cost[i], target <= 5000


# Solution: https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/solutions/635267/cjavapython-strict-otarget-by-lee215-mdg0
# Credit: Lee -> https://leetcode.com/u/lee215/
def largest_number(cost, target):
    dp = [0] + [-1] * (target + 5000)
    for t in range(1, target + 1):
        dp[t] = max(dp[t - c] * 10 + i + 1 for i, c in enumerate(cost))
    return str(max(dp[t], 0))
    # Time: O(n² * c)
    # Space: O(n²)


# NOTE: This solution seems to not work as expected
# Solution: https://algo.monster/liteproblems/1449
# Credit: AlgoMonster
def largest_number_alt(cost, target):
    # dp[i][j] = maximum count of digits we can use with digits 1..i and exact cost j
    # Initialize with negative infinity to mark invalid states
    dp = [[-float('inf')] * (target + 1) for _ in range(10)]
    dp[0][0] = 0  # Base case: 0 digits with 0 cost is valid (0 digits used)
    
    # parent[i][j] = the cost from which we transitioned to reach state (i, j)
    # Used for backtracking to construct the answer
    parent = [[0] * (target + 1) for _ in range(10)]
    
    # Fill the DP table
    for digit in range(1, 10):  # Digits 1-9 (index i corresponds to digit i)
        digit_cost = cost[digit - 1]  # Cost of current digit
        
        for current_cost in range(target + 1):
            # Option 1: Don't use current digit, inherit from previous digit
            dont_use = dp[digit - 1][current_cost]
            
            # Option 2: Use current digit (if we have enough budget)
            if current_cost >= digit_cost:
                use_digit = dp[digit][current_cost - digit_cost] + 1
            else:
                use_digit = -float('inf')
            
            # Choose the option that gives more digits
            if use_digit > dont_use:
                dp[digit][current_cost] = use_digit
                parent[digit][current_cost] = current_cost - digit_cost
            else:
                dp[digit][current_cost] = dont_use
                parent[digit][current_cost] = current_cost
    
    # Check if it's possible to achieve the target cost
    if dp[9][target] < 0:
        return "0"
    
    # Backtrack to construct the largest number
    result = []
    current_digit, remaining_cost = 9, target
    
    while current_digit > 0:
        if remaining_cost == parent[current_digit][remaining_cost]:
            # Current digit was not used, move to previous digit
            current_digit -= 1
        else:
            # Current digit was used, add it to result
            result.append(str(current_digit))
            remaining_cost = parent[current_digit][remaining_cost]
    
    return "".join(result)
    # Time: O(target)
    # Space: O(target)
    # Actually O(n * target) where n is the length of the cost array (which is 9 in this 
    # problem since digits are 1-9).


def main():
    result = largest_number(cost = [4,3,2,5,6,7,2,5,5], target = 9)
    print(result) # "7772"

    result = largest_number(cost = [7,6,5,5,5,6,8,7,8], target = 12)
    print(result) # "85"

    result = largest_number(cost = [2,4,6,2,4,6,4,4,4], target = 5)
    print(result) # "0"

if __name__ == "__main__":
    main()
