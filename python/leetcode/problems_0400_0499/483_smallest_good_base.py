# -----------------------
# 483. Smallest Good Base
# -----------------------

# Problem: https://leetcode.com/problems/smallest-good-base
#
# Given an integer n represented as a string, return the smallest good base of n.
# 
# We call k >= 2 a good base of n, if all digits of n base k are 1's.
# 
# Example 1:
# 
# Input: n = "13"
# Output: "3"
# 
# Explanation: 13 base 3 is 111.
# 
# Example 2:
# 
# Input: n = "4681"
# Output: "8"
# 
# Explanation: 4681 base 8 is 11111.
# 
# Example 3:
# 
# Input: n = "1000000000000000000"
# Output: "999999999999999999"
# 
# Explanation: 1000000000000000000 base 999999999999999999 is 11.
# 
# 
# Constraints:
#         n is an integer in the range [3, 10¹⁸].
#         n does not contain any leading zeros.


# Solution: https://algo.monster/liteproblems/483
# Credit: AlgoMonster
def smallest_good_base(n):
    def calculate_sum_of_powers(base, num_terms):
        power = 1  # Current power of base
        total_sum = 1  # Initialize with the first term (base^0 = 1)
        
        # Add base^1, base^2, ..., base^num_terms
        for i in range(num_terms):
            power *= base
            total_sum += power
        
        return total_sum
    
    # Convert string input to integer
    target_number = int(n)
    
    # Try different values of m (number of terms - 1) from largest to smallest
    # Maximum m is 63 because 2^64 > 10^18 (max value for n)
    for num_additional_terms in range(63, 1, -1):
        # Binary search for the base k that gives us exactly target_number
        # For m terms, minimum base is 2, maximum is target_number - 1
        left, right = 2, target_number - 1
        
        while left < right:
            mid = (left + right) >> 1  # Equivalent to // 2
            
            # Check if current base gives a sum >= target
            if calculate_sum_of_powers(mid, num_additional_terms) >= target_number:
                right = mid  # Try smaller bases
            else:
                left = mid + 1  # Try larger bases
        
        # Check if we found an exact match
        if calculate_sum_of_powers(left, num_additional_terms) == target_number:
            return str(left)
    
    # If no valid base found for m >= 2, return target_number - 1
    # This corresponds to m = 1 case: n = 1 + (n-1)
    return str(target_number - 1)
    # Time: O(log³(n))
    # Space: O(1)


def main():
    result = smallest_good_base("13")
    print(result) # "3"

    result = smallest_good_base("4681")
    print(result) # "8"

    result = smallest_good_base("1000000000000000000")
    print(result) # "999999999999999999"

if __name__ == "__main__":
    main()
