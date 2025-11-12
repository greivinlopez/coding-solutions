# ------------------------
# 1017. Convert to Base -2
# ------------------------

# Problem: https://leetcode.com/problems/convert-to-base-2
#
# Given an integer n, return a binary string representing its representation in
# base -2.
# 
# Note that the returned string should not have leading zeros unless the string is
# "0".
# 
# Example 1:
# 
# Input: n = 2
# Output: "110"
# 
# Explantion: (-2)2 + (-2)1 = 2
# 
# Example 2:
# 
# Input: n = 3
# Output: "111"
# 
# Explantion: (-2)2 + (-2)1 + (-2)0 = 3
# 
# Example 3:
# 
# Input: n = 4
# Output: "100"
# 
# Explantion: (-2)2 = 4
# 
# 
# Constraints:
#         0 <= n <= 10⁹


# Solution: https://algo.monster/liteproblems/1017
# Credit: AlgoMonster
def base_neg_2(n):
    # Track the current power coefficient (alternates between 1 and -1)
    power_coefficient = 1
    
    # Store binary digits of the result (in reverse order initially)
    result_digits = []
    
    # Process the number until it becomes 0
    while n > 0:
        # Check if current bit position should be 1
        if n % 2 == 1:
            result_digits.append('1')
            # Subtract the value contributed by this position
            # (could be positive or negative based on power_coefficient)
            n -= power_coefficient
        else:
            result_digits.append('0')
        
        # Move to the next bit position
        n //= 2
        
        # Alternate the sign for the next power of -2
        power_coefficient *= -1
    
    # Reverse the digits and join them, or return '0' for input 0
    return ''.join(reversed(result_digits)) if result_digits else '0'
    # Time: O(log(n))
    # Space: O(log(n))


def main():
    result = base_neg_2(2)
    print(result) # "110"

    result = base_neg_2(3)
    print(result) # "111"

    result = base_neg_2(4)
    print(result) # "100"

if __name__ == "__main__":
    main()
