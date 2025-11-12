# -----------
# 504. Base 7
# -----------

# Problem: https://leetcode.com/problems/base-7/
# 
# Given an integer num, return a string of its base 7 representation.
# 
#  
# Example 1:
# 
# Input: num = 100
# Output: "202"
# 
# Example 2:
# 
# Input: num = -7
# Output: "-10"
#  
# 
# Constraints:
# 
#   -10^7 <= num <= 10^7


# Solution: https://youtu.be/sbmq-efwOsA
# Credit: Greg Hogg
def convert_to_base_7(num):
    if num == 0:
        return '0'

    original_num = num
    num = abs(num)
    remainders = []
    
    while num > 0:
        remainder = num % 7
        remainders.append(str(remainder))
        num //= 7
    
    if original_num < 0:
        remainders.append('-')
    remainders.reverse()
    return ''.join(remainders)
    # Time: O(log_7(n))
    # Space: O(log_7(n))



def main():
    result = convert_to_base_7(100)
    print(result) # "202"

    result = convert_to_base_7(-7)
    print(result) # "-10"

if __name__ == "__main__":
    main()
