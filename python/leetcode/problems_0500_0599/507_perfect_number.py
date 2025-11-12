# -------------------
# 507. Perfect Number
# -------------------

# Problem: https://leetcode.com/problems/perfect-number
#
# A perfect number is a positive integer that is equal to the sum of its positive
# divisors, excluding the number itself. A divisor of an integer x is an integer
# that can divide x evenly.
# 
# Given an integer n, return true if n is a perfect number, otherwise return
# false.
# 
# Example 1:
# 
# Input: num = 28
# Output: true
# 
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
# 
# Example 2:
# 
# Input: num = 7
# Output: false
# 
# 
# Constraints:
#         1 <= num <= 10⁸

import math

# Solution: https://algo.monster/liteproblems/507
# Credit: AlgoMonster
def check_perfect_number_alt(num):
    # A perfect number is a positive integer equal to the sum of its positive divisors, excluding itself
    # Edge case: 1 is not a perfect number (has no proper divisors)
    if num == 1:
        return False
    
    # Initialize sum with 1 (since 1 is always a divisor)
    divisor_sum = 1
    
    # Start checking from 2 up to sqrt(num)
    i = 2
    
    # Iterate only up to sqrt(num) for efficiency
    while i * i <= num:
        # Check if i is a divisor of num
        if num % i == 0:
            # Add the divisor to sum
            divisor_sum += i
            
            # Add the corresponding pair divisor (num/i) if it's different from i
            # This avoids adding the same divisor twice when i = sqrt(num)
            if i != num // i:
                divisor_sum += num // i
        
        i += 1
    
    # Check if sum of all proper divisors equals the number itself
    return divisor_sum == num
    # Time: O(√n)
    # Space: O(1)

# Solution: https://leetcode.com/problems/perfect-number/solutions/5860628/simple-solution-beats-95-in-runtime-and-96-in-memory
# Credit: Manuchehr -> https://leetcode.com/u/saloydinov/
def check_perfect_number(num):
    if num < 5:
        return False

    sum = 1        
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            sum += i + num // i

    return sum == num 
    # Time: O(√n)
    # Space: O(1)


def main():
    result = check_perfect_number(28)
    print(result) # True

    result = check_perfect_number(7)
    print(result) # False

if __name__ == "__main__":
    main()
