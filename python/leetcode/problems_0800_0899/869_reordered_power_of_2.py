# -------------------------
# 869. Reordered Power of 2
# -------------------------

# Problem: https://leetcode.com/problems/reordered-power-of-2
#
# You are given an integer n. We reorder the digits in any order (including the
# original order) such that the leading digit is not zero.
# 
# Return true if and only if we can do this so that the resulting number is a
# power of two.
# 
# Example 1:
# 
# Input: n = 1
# Output: true
# 
# Example 2:
# 
# Input: n = 10
# Output: false
# 
# 
# Constraints:
#         1 <= n <= 10⁹


# Solution: https://algo.monster/liteproblems/869
# Credit: AlgoMonster
def reordered_power_of_2(n):

    def get_digit_frequency(number):
        digit_count = [0] * 10
        
        # Extract each digit and count its frequency
        while number > 0:
            number, remainder = divmod(number, 10)
            digit_count[remainder] += 1
            
        return digit_count
    
    # Get the digit frequency of the input number
    target_frequency = get_digit_frequency(n)
    
    # Check all powers of 2 up to 10^9
    power_of_two = 1
    while power_of_two <= 10**9:
        # Compare digit frequencies
        if get_digit_frequency(power_of_two) == target_frequency:
            return True
        
        # Move to next power of 2 using left shift
        power_of_two <<= 1
        
    return False
    # Time: O(log(m))
    # Space: O(log(m))
    # m = 10⁹ is the upper limit of the input range.


def main():
    result = reordered_power_of_2(1)
    print(result) # True

    result = reordered_power_of_2(10)
    print(result) # False

if __name__ == "__main__":
    main()
