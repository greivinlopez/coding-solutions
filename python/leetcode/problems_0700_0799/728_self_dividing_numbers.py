# --------------------------
# 728. Self Dividing Numbers
# --------------------------

# Problem: https://leetcode.com/problems/self-dividing-numbers
#
# A self-dividing number is a number that is divisible by every digit it contains.
#         
#   * For example, 128 is a self-dividing number because 128 % 1 == 0, 
#     128 % 2 == 0, and 128 % 8 == 0.
# 
# A self-dividing number is not allowed to contain the digit zero.
# 
# Given two integers left and right, return a list of all the self-dividing
# numbers in the range [left, right] (both inclusive).
# 
# Example 1:
# 
# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
# 
# Example 2:
# 
# Input: left = 47, right = 85
# Output: [48,55,66,77]
# 
# 
# Constraints:
#         1 <= left <= right <= 10⁴


# Solution: https://algo.monster/liteproblems/728
# Credit: AlgoMonster
def self_dividing_numbers(left, right):
    def is_self_dividing(num: int) -> bool:
        temp = num
        
        # Check each digit of the number
        while temp > 0:
            digit = temp % 10
            
            # If digit is 0 or number is not divisible by digit, not self-dividing
            if digit == 0 or num % digit != 0:
                return False
            
            # Move to the next digit
            temp //= 10
        
        return True
    
    # Generate list of self-dividing numbers in the given range
    return [num for num in range(left, right + 1) if is_self_dividing(num)]
    # Time: O(n × log₁₀(m))
    # Space: O(1)
    # n = the number of integers in the interval [left, right]
    # m = right, the maximum value in the interval.


def main():
    result = self_dividing_numbers(left = 1, right = 22)
    print(result) # [1,2,3,4,5,6,7,8,9,11,12,15,22]

    result = self_dividing_numbers(left = 47, right = 85)
    print(result) # [48,55,66,77]

if __name__ == "__main__":
    main()
