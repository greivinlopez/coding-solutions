# --------------------------
# 633. Sum of Square Numbers
# --------------------------

# Problem: https://leetcode.com/problems/sum-of-square-numbers
#
# Given a non-negative integer c, decide whether there're two integers a and b
# such that a² + b² = c.
# 
# Example 1:
# 
# Input: c = 5
# Output: true
# 
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# Example 2:
# 
# Input: c = 3
# Output: false
# 
# 
# Constraints:
#         0 <= c <= 2³¹ - 1


# Solution: https://youtu.be/B0UrG_X2faA
# Credit: Navdeep Singh founder of NeetCode
def judge_square_sum(c):
    squareroot = set()

    for i in range(int(c**0.5) + 1):
        squareroot.add(i * i)

    a = 0
    while a * a <= c:
        target = c - a * a
        if target in squareroot:
            return True
        a += 1

    return False
    # Time: O(√c)
    # Space: O(√c)

def judge_square_sum_alt(c):
    # Space optimized solution
    left, right = 0, int(c**0.5)

    while left <= right:
        total = left * left + right * right
        if total > c:
            right -= 1
        elif total < c:
            left += 1
        else:
            return True

    return False
    # Time: O(√c)
    # Space: O(1)


def main():
    result = judge_square_sum(5)
    print(result) # True

    result = judge_square_sum(3)
    print(result) # False

if __name__ == "__main__":
    main()
