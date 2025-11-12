# -------------------------
# 367. Valid Perfect Square
# -------------------------

# Problem: https://leetcode.com/problems/valid-perfect-square/
# 
# Given a positive integer num, return true if num is a perfect square or false 
# otherwise.
# 
# A perfect square is an integer that is the square of an integer. In other 
# words, it is the product of some integer with itself.
# 
# You must not use any built-in library function, such as sqrt.
#  
# Example 1:
# 
# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
# 
# 
# Example 2:
# 
# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
# 
# 
# Constraints:
# 
# 	1 <= num <= 2^31 - 1


# Solution: https://youtu.be/Cg_wWPHJ2Sk
# Credit: Navdeep Singh founder of NeetCode
def is_perfect_square(num):
    for i in range(1, num+1):
        if i * i == num:
            return True
        if i* i > num:
            return False

def is_perfect_square_alt(num):
    l ,r = 1, num
    while l <= r:
        mid = (l +r) // 2
        if mid * mid > num:
            r = mid - 1
        elif mid * mid < num:
            l = mid + 1
        else:
            return True
    return False

# Solution: https://youtu.be/iqD5Fp2E5dM
# Credit: Greg Hogg
def is_perfect_square_alt_2(num):
    l = 1
    r = num

    while l <= r:
        m = (l+r) // 2
        m_squared = m * m

        if num == m_squared:
            return True
        elif m_squared < num:
            l = m + 1
        else:
            r = m - 1
    
    return False 
    # Time: O(log n)
    # Space: O(1)

def main():
    result = is_perfect_square(16)
    print(result) # True

    result = is_perfect_square(14)
    print(result) # False

if __name__ == "__main__":
    main()
