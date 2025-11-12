# -------------------------------------------------------------------------
# 1467. Probability of a Two Boxes Having The Same Number of Distinct Balls
# -------------------------------------------------------------------------

# Problem: https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls
#
# Given 2n balls of k distinct colors. You will be given an integer array balls of
# size k where balls[i] is the number of balls of color i.
# 
# All the balls will be shuffled uniformly at random, then we will distribute the
# first n balls to the first box and the remaining n balls to the other box
# (Please read the explanation of the second example carefully).
# 
# Please note that the two boxes are considered different. For example, if we have
# two balls of colors a and b, and two boxes [] and (), then the distribution [a]
# (b) is considered different than the distribution [b] (a) (Please read the
# explanation of the first example carefully).
# 
# Return the probability that the two boxes have the same number of distinct
# balls. Answers within 10-5 of the actual value will be accepted as correct.
# 
# Example 1:
# 
# Input: balls = [1,1]
# Output: 1.00000
# 
# Explanation: Only 2 ways to divide the balls equally:
# - A ball of color 1 to box 1 and a ball of color 2 to box 2
# - A ball of color 2 to box 1 and a ball of color 1 to box 2
# In both ways, the number of distinct colors in each box is equal. The
# probability is 2/2 = 1
# 
# Example 2:
# 
# Input: balls = [2,1,1]
# Output: 0.66667
# 
# Explanation: We have the set of balls [1, 1, 2, 3]
# This set of balls will be shuffled randomly and we may have one of the 12
# distinct shuffles with equal probability (i.e. 1/12):
# [1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2], [1,3 / 2,1],
# [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
# After that, we add the first two balls to the first box and the second two balls
# to the second box.
# We can see that 8 of these 12 possible random distributions have the same number
# of distinct colors of balls in each box.
# Probability is 8/12 = 0.66667
# 
# Example 3:
# 
# Input: balls = [1,2,1,2]
# Output: 0.60000
# 
# Explanation: The set of balls is [1, 2, 2, 3, 4, 4]. It is hard to display all
# the 180 possible random shuffles of this set but it is easy to check that 108 of
# them will have the same number of distinct colors in each box.
# Probability = 108 / 180 = 0.6
# 
# 
# Constraints:
#         1 <= balls.length <= 8
#         1 <= balls[i] <= 6
#         sum(balls) is even.


# Solution: https://algo.monster/liteproblems/1467
# Credit: AlgoMonster
def get_probability(balls):
    from functools import cache
    from math import comb
    
    @cache
    def dfs(color_index: int, remaining_balls: int, color_difference: int) -> float:
        # Base case: all colors have been processed
        if color_index >= num_colors:
            # Valid distribution if first box has exactly n balls and 
            # both boxes have same number of distinct colors
            return 1 if remaining_balls == 0 and color_difference == 0 else 0
        
        # Pruning: impossible to have exactly n balls in first box
        if remaining_balls < 0:
            return 0
        
        total_ways = 0
        
        # Try all possible distributions of current color's balls
        for balls_in_first_box in range(balls[color_index] + 1):
            # Calculate change in color difference
            if balls_in_first_box == balls[color_index]:
                # All balls of this color go to first box
                color_diff_change = 1
            elif balls_in_first_box == 0:
                # All balls of this color go to second box
                color_diff_change = -1
            else:
                # Balls of this color are split between both boxes
                color_diff_change = 0
            
            # Recursive call for next color with updated parameters
            ways = dfs(
                color_index + 1,
                remaining_balls - balls_in_first_box,
                color_difference + color_diff_change
            )
            
            # Multiply by combinations for this specific distribution
            total_ways += ways * comb(balls[color_index], balls_in_first_box)
        
        return total_ways
    
    # Calculate total number of balls and half of it (for equal distribution)
    total_balls = sum(balls)
    half_balls = total_balls >> 1  # Equivalent to total_balls // 2
    
    # Number of distinct colors
    num_colors = len(balls)
    
    # Calculate the number of valid distributions divided by total possible distributions
    valid_distributions = dfs(0, half_balls, 0)
    total_distributions = comb(half_balls << 1, half_balls)  # Equivalent to comb(total_balls, half_balls)
    
    return valid_distributions / total_distributions
    # Time: O(k * n * k * max(balls[i]))
    # Space: O(k²)


def main():
    result = get_probability(balls = [1,1])
    print(result) # 1.0

    result = get_probability(balls = [2,1,1])
    print(result) # 0.6666666666666666

    result = get_probability(balls = [1,2,1,2])
    print(result) # 0.6

if __name__ == "__main__":
    main()
