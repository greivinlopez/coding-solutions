# ---------------------------------------------------
# 600. Non-negative Integers without Consecutive Ones
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/non-negative-integers-without-consecutive-ones
#
# Given a positive integer n, return the number of the integers in the range [0,n] 
# whose binary representations do not contain consecutive ones.
# 
# Example 1:
# 
# Input: n = 5
# Output: 5
# 
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary
# representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the
# other 5 satisfy the rule.
# 
# Example 2:
# 
# Input: n = 1
# Output: 2
# 
# Example 3:
# 
# Input: n = 2
# Output: 3
# 
# 
# Constraints:
#         1 <= n <= 10⁹

from functools import cache

# Solution: https://algo.monster/liteproblems/600
# Credit: AlgoMonster
def find_integers(n):
    @cache
    def count_valid_numbers(bit_position, 
                            previous_bit, 
                            is_limit):
        # Base case: processed all bits successfully
        if bit_position < 0:
            return 1
        
        # Determine the upper bound for current bit
        # If we're at limit, we can only go up to the corresponding bit in n
        # Otherwise, we can use 0 or 1
        upper_bound = (n >> bit_position & 1) if is_limit else 1
        
        # Count valid numbers by trying each possible bit value
        total_count = 0
        for current_bit in range(upper_bound + 1):
            # Skip if we would have consecutive 1s (previous was 1 and current is 1)
            if previous_bit == 1 and current_bit == 1:
                continue
            
            # Recursively count valid numbers with:
            # - Next bit position (moving right)
            # - Current bit becomes the previous for next recursion
            # - Update limit flag (remains true only if we're at limit AND chose maximum bit)
            total_count += count_valid_numbers(
                bit_position - 1, 
                current_bit, 
                is_limit and (current_bit == upper_bound)
            )
        
        return total_count
    
    # Start from the most significant bit
    # Initial previous bit is 0 (no bit before MSB)
    # Initially we're bounded by n (is_limit = True)
    return count_valid_numbers(n.bit_length() - 1, 0, True)
    # Time: O(log(n))
    # Space: O(log(n))


def main():
    result = find_integers(5)
    print(result) # 5

    result = find_integers(1)
    print(result) # 2

    result = find_integers(2)
    print(result) # 3

if __name__ == "__main__":
    main()
