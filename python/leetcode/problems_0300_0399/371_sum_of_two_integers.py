# ------------------------
# 371. Sum Of Two Integers
# ------------------------

# Problem: https://leetcode.com/problems/sum-of-two-integers/
# 
# Given two integers a and b, return the sum of the two integers without using 
# the operators + and -.
# 
#  
# Example 1:
# 
# Input: a = 1, b = 2
# Output: 3
# 
# Example 2:
# 
# Input: a = 2, b = 3
# Output: 5
# 
#  
# Constraints:
# 
# 	-1000 <= a, b <= 1000


# Solution: https://youtu.be/gVUrDV4tZfY
# Credit: Navdeep Singh founder of NeetCode
def get_sum(a, b):
    def add(a, b):
        if not a or not b:
            return a or b
        return add(a ^ b, (a & b) << 1)

    if a * b < 0:  # assume a < 0, b > 0
        if a > 0:
            return self.getSum(b, a)
        if add(~a, 1) == b:  # -a == b
            return 0
        if add(~a, 1) < b:  # -a < b
            return add(~add(add(~a, 1), add(~b, 1)), 1)  # -add(-a, -b)

    return add(a, b)  # a*b >= 0 or (-a) > b > 0


def main():
    result = get_sum(1, 2)
    print(result) # 3

    result = get_sum(2, 3)
    print(result) # 5

if __name__ == "__main__":
    main()
