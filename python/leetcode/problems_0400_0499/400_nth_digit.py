# --------------
# 400. Nth Digit
# --------------

# Problem: https://leetcode.com/problems/nth-digit
#
# Given an integer n, return the nth digit of the infinite integer sequence [1, 2,
# 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].
# 
# Example 1:
# 
# Input: n = 3
# Output: 3
# 
# Example 2:
# 
# Input: n = 11
# Output: 0
# 
# Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
# ... is a 0, which is part of the number 10.
# 
# Constraints:
#         1 <= n <= 2³¹ - 1


def find_nth_digit(n):
    digits = start = 1 
    count = 9

    while n > digits * count:
        n -= digits * count
        digits += 1
        count *= 10
        start *= 10
    
    num = start + (n - 1) // digits
    digit_index = (n - 1) % digits
    
    return int(str(num)[digit_index])
    # Time: O(log(n))
    # Space: O(1)


def main():
    result = find_nth_digit(3)
    print(result) # 3

    result = find_nth_digit(11)
    print(result) # 0

if __name__ == "__main__":
    main()
