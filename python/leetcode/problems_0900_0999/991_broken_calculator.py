# -------------------------
# 991. Broken Calculator 🧮
# -------------------------

# Problem: https://leetcode.com/problems/broken-calculator
#
# There is a broken calculator that has the integer startValue on its display
# initially. In one operation, you can:
#         
#   * multiply the number on display by 2, or
#   * subtract 1 from the number on display.
# 
# Given two integers startValue and target, return the minimum number of
# operations needed to display target on the calculator.
# 
# Example 1:
# 
# Input: startValue = 2, target = 3
# Output: 2
# 
# Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
# 
# Example 2:
# 
# Input: startValue = 5, target = 8
# Output: 2
# 
# Explanation: Use decrement and then double {5 -> 4 -> 8}.
# 
# Example 3:
# 
# Input: startValue = 3, target = 10
# Output: 3
# 
# Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.
# 
# 
# Constraints:
#         1 <= startValue, target <= 10⁹


# Solution: https://algo.monster/liteproblems/991
# Credit: AlgoMonster
def broken_calc(startValue, target):
    # Initialize operation counter
    operations = 0
    
    # Work backwards from target to startValue
    # While target is greater than startValue, reduce target
    while startValue < target:
        # Check if target is odd using bitwise AND
        if target & 1:  # Equivalent to: if target % 2 == 1
            # If target is odd, we must have reached it by subtracting 1
            # So add 1 to reverse that operation
            target += 1
        else:
            # If target is even, we could have reached it by multiplying by 2
            # So divide by 2 (using right shift for efficiency)
            target >>= 1  # Equivalent to: target //= 2
        
        # Increment operation count
        operations += 1
    
    # After the loop, target <= startValue
    # We need (startValue - target) subtractions to reach target
    operations += startValue - target
    
    return operations
    # Time: O(log(target))
    # Space: O(1)


def main():
    result = broken_calc(startValue = 2, target = 3)
    print(result) # 2

    result = broken_calc(startValue = 5, target = 8)
    print(result) # 2

    result = broken_calc(startValue = 3, target = 10)
    print(result) # 3

if __name__ == "__main__":
    main()
