# ----------------------
# 906. Super Palindromes
# ----------------------

# Problem: https://leetcode.com/problems/super-palindromes
#
# Let's say a positive integer is a super-palindrome if it is a palindrome, and it
# is also the square of a palindrome.
# 
# Given two positive integers left and right represented as strings, return the
# number of super-palindromes integers in the inclusive range [left, right].
# 
# Example 1:
# 
# Input: left = "4", right = "1000"
# Output: 4
# 
# Explanation: 4, 9, 121, and 484 are superpalindromes.
# Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a
# palindrome.
# 
# Example 2:
# 
# Input: left = "1", right = "2"
# Output: 1
# 
# 
# Constraints:
#         1 <= left.length, right.length <= 18
#         left and right consist of only digits.
#         left and right cannot have leading zeros.
#         left and right represent integers in the range [1, 10¹⁸ - 1].
#         left is less than or equal to right.


# Solution: https://algo.monster/liteproblems/906
# Credit: AlgoMonster
def super_palindromes_in_range(left, right):
    
    def is_palindrome(number):
        reversed_number = 0
        temp = number
        
        # Reverse the digits of the number
        while temp > 0:
            reversed_number = reversed_number * 10 + temp % 10
            temp //= 10
            
        return number == reversed_number
    
    # Pre-generate all possible palindrome roots up to 10^5
    # Since we're looking for palindromes whose squares are also palindromes,
    # we only need to check palindrome numbers as potential roots
    palindrome_roots = []
    for num in range(1, 10**5 + 1):
        num_str = str(num)
    
        # Create odd-length palindrome: "123" -> "123321"
        reversed_str = num_str[::-1]
        odd_palindrome = int(num_str + reversed_str)
        palindrome_roots.append(odd_palindrome)
    
        # Create even-length palindrome: "123" -> "12321" (excluding last digit before reversing)
        reversed_without_last = num_str[:-1][::-1]
        even_palindrome = int(num_str + reversed_without_last)
        palindrome_roots.append(even_palindrome)
    
    # Convert string bounds to integers
    left_bound = int(left)
    right_bound = int(right)
    
    # Count super palindromes: check if square of each palindrome root
    # is within range and is also a palindrome
    count = 0
    for root in palindrome_roots:
        square = root * root
        if left_bound <= square <= right_bound and is_palindrome(square):
            count += 1
            
    return count
    # Time: O(n)
    # Space: O(n)
    # n = 10⁵


def main():
    result = super_palindromes_in_range(left = "4", right = "1000")
    print(result) # 4

    result = super_palindromes_in_range(left = "1", right = "2")
    print(result) # 1

if __name__ == "__main__":
    main()
