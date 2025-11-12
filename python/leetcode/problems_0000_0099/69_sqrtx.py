# ------------
# 69. Sqrt(x)
# ------------

# Problem: https://leetcode.com/problems/sqrtx/
# 
# Given a non-negative integer x, return the square root of x rounded down to 
# the nearest integer. The returned integer should be non-negative as well.
# 
# You must not use any built-in exponent function or operator.
# 
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


# Solution: https://youtu.be/zdMhGxRWutQ
# Credit: Navdeep Singh founder of NeetCode 
def my_sqrt(x):
    l, r = 0, x
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            l = mid + 1
        else:
            r = mid - 1
    return r


def main():
    result = my_sqrt(4) 
    # Expected Output: 2
    print(result)
    result = my_sqrt(8)
    # Expected Output: 2
    print(result)

if __name__ == "__main__":
    main()