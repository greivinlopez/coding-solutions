# -------------------------------------------------------
# 1276. Number of Burgers with No Waste of Ingredients 🍔
# -------------------------------------------------------

# Problem: https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients
#
# Given two integers tomatoSlices and cheeseSlices. The ingredients of different
# burgers are as follows:
#         
#   * Jumbo Burger: 4 tomato slices and 1 cheese slice.
#   * Small Burger: 2 Tomato slices and 1 cheese slice.
# 
# Return [total_jumbo, total_small] so that the number of remaining tomatoSlices
# equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not
# possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return
# [].
# 
# Example 1:
# 
# Input: tomatoSlices = 16, cheeseSlices = 7
# Output: [1,6]
# 
# Explantion: To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16
# tomato and 1 + 6 = 7 cheese.
# There will be no remaining ingredients.
# 
# Example 2:
# 
# Input: tomatoSlices = 17, cheeseSlices = 4
# Output: []
# 
# Explantion: There will be no way to use all ingredients to make small and jumbo
# burgers.
# 
# Example 3:
# 
# Input: tomatoSlices = 4, cheeseSlices = 17
# Output: []
# 
# Explantion: Making 1 jumbo burger there will be 16 cheese remaining and making 2
# small burgers there will be 15 cheese remaining.
# 
# 
# Constraints:
#         0 <= tomatoSlices, cheeseSlices <= 10⁷


# Solution: https://algo.monster/liteproblems/1276
# Credit: AlgoMonster
def num_of_burgers(tomatoSlices, cheeseSlices):
    # Calculate the difference to find Small burgers
    difference = 4 * cheeseSlices - tomatoSlices
    
    # Number of Small burgers (must be divisible by 2)
    num_small_burgers = difference // 2
    
    # Number of Jumbo burgers
    num_jumbo_burgers = cheeseSlices - num_small_burgers
    
    # Validation checks:
    # 1. difference must be even (divisible by 2)
    # 2. Both burger counts must be non-negative
    if difference % 2 != 0 or num_small_burgers < 0 or num_jumbo_burgers < 0:
        return []
    
    return [num_jumbo_burgers, num_small_burgers]
    # Time: O(1)
    # Space: O(1)

# Alternative Solution: https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/solutions/551868/math-python-using-2-variables-linear-alg-4g3w
# Credit: Suraj Regmi -> https://leetcode.com/u/suraj1127/
def num_of_burgers_alt(tomatoSlices, cheeseSlices):
    # on the basis of the matrix solution
    ans = [0.5 * tomatoSlices - cheeseSlices, -0.5 * tomatoSlices + 2 * cheeseSlices]
    
    # using the constraints to see if solution satisfies it
    if 0 <= int(ans[0]) == ans[0] and 0 <= int(ans[1]) == ans[1]:
        return [int(ans[0]), int(ans[1])]
    else:
        return []
    # Time: O(1)
    # Space: O(1)


def main():
    result = num_of_burgers(tomatoSlices = 16, cheeseSlices = 7)
    print(result) # [1, 6]

    result = num_of_burgers(tomatoSlices = 17, cheeseSlices = 4)
    print(result) # []

    result = num_of_burgers(tomatoSlices = 4, cheeseSlices = 17)
    print(result) # []

if __name__ == "__main__":
    main()
