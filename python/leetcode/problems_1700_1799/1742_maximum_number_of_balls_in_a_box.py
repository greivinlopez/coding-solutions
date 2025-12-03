# --------------------------------------
# 1742. Maximum Number of Balls in a Box
# --------------------------------------

# Problem: https://leetcode.com/problems/maximum-number-of-balls-in-a-box
#
# You are working in a ball factory where you have n balls numbered from lowLimit
# up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite
# number of boxes numbered from 1 to infinity.
# 
# Your job at this factory is to put each ball in the box with a number equal to
# the sum of digits of the ball's number. For example, the ball number 321 will be
# put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the
# box number 1 + 0 = 1.
# 
# Given two integers lowLimit and highLimit, return the number of balls in the box
# with the most balls.
# 
# Example 1:
# 
# Input: lowLimit = 1, highLimit = 10
# Output: 2
# 
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
# Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
# Box 1 has the most number of balls with 2 balls.
# 
# Example 2:
# 
# Input: lowLimit = 5, highLimit = 15
# Output: 2
# 
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
# Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
# Boxes 5 and 6 have the most number of balls with 2 balls in each.
# 
# Example 3:
# 
# Input: lowLimit = 19, highLimit = 28
# Output: 2
# 
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
# Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
# Box 10 has the most number of balls with 2 balls.
# 
# 
# Constraints:
#         1 <= lowLimit <= highLimit <= 10⁵


# Solution: https://algo.monster/liteproblems/1742
# Credit: AlgoMonster
def count_balls(lowLimit, highLimit):
    # Initialize a counter array to store the count of balls in each box
    # Maximum possible sum of digits for numbers up to 10^5 is 45 (99999)
    # So 50 boxes are sufficient
    box_counts = [0] * 50
    
    # Iterate through each ball number from lowLimit to highLimit (inclusive)
    for ball_number in range(lowLimit, highLimit + 1):
        # Calculate the sum of digits for current ball number
        digit_sum = 0
        temp_number = ball_number
        
        # Extract and sum each digit
        while temp_number > 0:
            digit_sum += temp_number % 10  # Get the last digit
            temp_number //= 10  # Remove the last digit
        
        # Increment the count for the box corresponding to this digit sum
        box_counts[digit_sum] += 1
    
    # Return the maximum count among all boxes
    return max(box_counts)
    # Time: O(n × log₁₀(m))
    # Space: O(1)


def main():
    result = count_balls(lowLimit = 1, highLimit = 10)
    print(result) # 2

    result = count_balls(lowLimit = 5, highLimit = 15)
    print(result) # 2

    result = count_balls(lowLimit = 19, highLimit = 28)
    print(result) # 2

if __name__ == "__main__":
    main()
