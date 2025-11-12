# --------------
# 372. Super Pow
# --------------

# Problem: https://leetcode.com/problems/super-pow
#
# Your task is to calculate ab mod 1337 where a is a positive integer and b is an
# extremely large positive integer given in the form of an array.
# 
# Example 1:
# 
# Input: a = 2, b = [3]
# Output: 8
# 
# Example 2:
# 
# Input: a = 2, b = [1,0]
# Output: 1024
# 
# Example 3:
# 
# Input: a = 1, b = [4,3,3,8,5,2]
# Output: 1
# 
# 
# Constraints:
#         1 <= a <= 2³¹ - 1
#         1 <= b.length <= 2000
#         0 <= b[i] <= 9
#         b does not contain leading zeros.


# Solution: https://leetcode.com/problems/super-pow/solutions/400893/python-3-with-explanation-handles-all-test-cases-one-line-beats-97
# Credit: Junaid Mansuri -> https://leetcode.com/u/junaidmansuri/
# This is based on Euler's theorem -> https://en.wikipedia.org/wiki/Euler%27s_theorem
def super_pow_alt(a, b):
    return (a % 1337)**(1140 + int(''.join(map(str, b))) % 1140) % 1337
    # Time: O(n)
    # Space: O(n)
    # n = length of array b

# My Solution also based on Euler's theorem optimized space
def super_pow(a, b):
    b_mod = 0
    for digit in b:
        b_mod = (b_mod * 10 + digit) % 1140

    return pow(a % 1337, 1140 + b_mod, 1337)
    # Time: O(n)
    # Space: O(1)
    # n = length of array b


def main():
    result = super_pow(a = 2, b = [3])
    print(result) # 8

    result = super_pow(a = 2, b = [1,0])
    print(result) # 1024

    result = super_pow(a = 1, b = [4,3,3,8,5,2])
    print(result) # 1

if __name__ == "__main__":
    main()
