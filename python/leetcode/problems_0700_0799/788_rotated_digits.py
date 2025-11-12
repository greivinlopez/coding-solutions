# -------------------
# 788. Rotated Digits
# -------------------

# Problem: https://leetcode.com/problems/rotated-digits
#
# An integer x is a good if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from x. Each digit must be rotated - we
# cannot choose to leave it alone.
# 
# A number is valid if each digit remains a digit after rotation. For example:
#         
#   * 0, 1, and 8 rotate to themselves,
#   * 2 and 5 rotate to each other (in this case they are rotated in a different 
#     direction, in other words, 2 or 5 gets mirrored),
#   * 6 and 9 rotate to each other, and the rest of the numbers do not rotate to 
#     any other number and become invalid.
# 
# Given an integer n, return the number of good integers in the range [1, n].
# 
# Example 1:
# 
# Input: n = 10
# Output: 4
# 
# Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after
# rotating.
# 
# Example 2:
# 
# Input: n = 1
# Output: 0
# 
# Example 3:
# 
# Input: n = 2
# Output: 1
# 
# 
# Constraints:
#         1 <= n <= 10⁴


# Solution: https://algo.monster/liteproblems/788
# Credit: AlgoMonster
def rotated_digits(n):
   
    def is_good_number(number):
        rotated_number = 0
        temp_number = number
        place_value = 1
        
        # Process each digit from right to left
        while temp_number:
            digit = temp_number % 10
            
            # If digit cannot be rotated (3, 4, 7), number is invalid
            if rotation_map[digit] == -1:
                return False
            
            # Build the rotated number digit by digit
            rotated_number = rotation_map[digit] * place_value + rotated_number
            place_value *= 10
            temp_number //= 10
        
        # Number is good if it changes after rotation
        return number != rotated_number
    
    # Mapping of each digit to its 180-degree rotation
    # -1 means the digit cannot be rotated to form a valid digit
    # Index represents the digit, value represents its rotation
    rotation_map = [0, 1, 5, -1, -1, 2, 9, -1, 8, 6]
    #               0  1  2   3   4   5  6   7   8  9
    
    # Count all good numbers from 1 to n
    return sum(is_good_number(i) for i in range(1, n + 1))
    # Time: O(n * log(n))
    # Space: O(1)


def main():
    result = rotated_digits(10)
    print(result) # 4

    result = rotated_digits(1)
    print(result) # 0

    result = rotated_digits(2)
    print(result) # 1

if __name__ == "__main__":
    main()
