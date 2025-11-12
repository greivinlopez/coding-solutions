# ------------------------------
# 172. Factorial Trailing Zeroes
# ------------------------------

# Problem: https://leetcode.com/problems/factorial-trailing-zeroes
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
# 
# Example 1:
# 
# Input: n = 3
# Output: 0
# 
# Explanation: 3! = 6, no trailing zero.
# 
# Example 2:
# 
# Input: n = 5
# Output: 1
# 
# Explanation: 5! = 120, one trailing zero.
# 
# Example 3:
# 
# Input: n = 0
# Output: 0
# 
# Constraints:
#         0 <= n <= 10⁴
# 
# 
# Follow up: Could you write a solution that works in logarithmic time complexity?


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def trailing_zeroes(n):
    if n == 0:
        return 0
    
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    
    count = 0
    while factorial > 0:
        rem = factorial % 10
        if rem != 0:
            break
        count += 1
        
        factorial //= 10
        
    return count
    # Time: O(n)
    # Space: O(1)


def main():
    result = trailing_zeroes(3)
    print(result) # 0

    result = trailing_zeroes(5)
    print(result) # 1

    result = trailing_zeroes(0)
    print(result) # 0

if __name__ == "__main__":
    main()
