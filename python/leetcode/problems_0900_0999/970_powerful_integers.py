# ----------------------
# 970. Powerful Integers
# ----------------------

# Problem: https://leetcode.com/problems/powerful-integers
#
# Given three integers x, y, and bound, return a list of all the powerful integers
# that have a value less than or equal to bound.
# 
# An integer is powerful if it can be represented as xᶦ + yʲ for some integers i >= 0 
# and j >= 0.
# 
# You may return the answer in any order. In your answer, each value should occur
# at most once.
# 
# Example 1:
# 
# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# 
# Explanation:
# 2 = 20 + 30
# 3 = 21 + 30
# 4 = 20 + 31
# 5 = 21 + 31
# 7 = 22 + 31
# 9 = 23 + 30
# 10 = 20 + 32
# 
# Example 2:
# 
# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]
# 
# 
# Constraints:
#         1 <= x, y <= 100
#         0 <= bound <= 10⁶


# Solution: https://algo.monster/liteproblems/970
# Credit: AlgoMonster
def powerful_integers(x, y, bound):
    # Use set to store unique powerful integers
    result_set = set()
    
    # Initialize x^i starting from x^0 = 1
    power_of_x = 1
    
    # Iterate through all possible values of x^i
    while power_of_x <= bound:
        # Initialize y^j starting from y^0 = 1
        power_of_y = 1
        
        # Iterate through all possible values of y^j for current x^i
        while power_of_x + power_of_y <= bound:
            # Add the powerful integer to the result set
            result_set.add(power_of_x + power_of_y)
            
            # Calculate next power of y
            power_of_y *= y
            
            # Handle edge case: if y = 1, y^j will always be 1
            # No need to continue inner loop
            if y == 1:
                break
        
        # Calculate next power of x
        power_of_x *= x
        
        # Handle edge case: if x = 1, x^i will always be 1
        # No need to continue outer loop
        if x == 1:
            break
    
    # Convert set to list and return
    return list(result_set)
    # Time: O(log²(bound))
    # Space: O(log²(bound))


def main():
    result = powerful_integers(x = 2, y = 3, bound = 10)
    print(result) # [2, 3, 4, 5, 7, 9, 10]

    result = powerful_integers(x = 3, y = 5, bound = 15)
    print(result) # [2, 4, 6, 8, 10, 14]

if __name__ == "__main__":
    main()
