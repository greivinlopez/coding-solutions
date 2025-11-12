# -----------------------------------------------------------------
# 1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
# -----------------------------------------------------------------

# Problem: https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k
#
# Given an integer k, return the minimum number of Fibonacci numbers whose sum is
# equal to k. The same Fibonacci number can be used multiple times.
# 
# The Fibonacci numbers are defined as:
# 
#         F1 = 1
#         F2 = 1
#         Fn = Fn-1 + Fn-2 for n > 2.
# 
# It is guaranteed that for the given constraints we can always find such
# Fibonacci numbers that sum up to k.
# 
# Example 1:
# 
# Input: k = 7
# Output: 2
# 
# Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ...
# For k = 7 we can use 2 + 5 = 7.
# 
# Example 2:
# 
# Input: k = 10
# Output: 2
# 
# Explanation: For k = 10 we can use 2 + 8 = 10.
# 
# Example 3:
# 
# Input: k = 19
# Output: 3
# 
# Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
# 
# 
# Constraints:
#         1 <= k <= 10⁹


# Solution: https://algo.monster/liteproblems/1414
# Credit: AlgoMonster
def find_min_fibonacci_numbers(k):
    # Generate Fibonacci numbers up to k
    # Start with the first two Fibonacci numbers
    prev, curr = 1, 1
    
    # Build Fibonacci sequence until we exceed k
    while curr <= k:
        prev, curr = curr, prev + curr
    
    # curr is now the smallest Fibonacci number greater than k
    # We'll work backwards from here
    
    # Count minimum Fibonacci numbers needed
    count = 0
    
    # Greedily subtract largest possible Fibonacci numbers
    while k > 0:
        # If current Fibonacci number fits in remaining k
        if k >= curr:
            k -= curr
            count += 1
        
        # Move to previous Fibonacci number
        # curr becomes prev, and prev becomes curr - prev
        prev, curr = curr - prev, prev
    
    return count
    # Time: O(log k)
    # Space: O(1)


def main():
    result = find_min_fibonacci_numbers(k = 7)
    print(result) # 2

    result = find_min_fibonacci_numbers(k = 10)
    print(result) # 2

    result = find_min_fibonacci_numbers(k = 19)
    print(result) # 3

if __name__ == "__main__":
    main()
