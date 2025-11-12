# ---------------------------
# 1137. N-Th Tribonacci Number
# ---------------------------

# Problem: https://leetcode.com/problems/n-th-tribonacci-number
#
# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# 
# Given n, return the value of Tn.
# 
# 
# Example 1:
# 
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# 
# Example 2:
# 
# Input: n = 25
# Output: 1389537
# 
# 
# Constraints:
# 
#         - 0 <= n <= 37
#         - The answer is guaranteed to fit within a 32-bit integer, ie. answer <=
#           2^31 - 1.


# Solution: https://youtu.be/3lpNp5Ojvrw
# Credit: Navdeep Singh founder of NeetCode
def tribonacci(n):
    t = [0, 1, 1]
    if n < 3:
        return t[n]
    for i in range(3, n+1):
        t[0], t[1], t[2] = t[1], t[2], sum(t)
    return t[2]

# Alt Solution
Memo = {}
def tribonacci_alt(n):
    if n in Memo:
        return Memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    Memo[n] = (
        tribonacci_alt(n - 1) + tribonacci_alt(n - 2) + tribonacci_alt(n - 3)
    )
    return Memo[n]


def main():
    result = tribonacci(4)
    print(result) # 4

    result = tribonacci(25)
    print(result) # 1389537

if __name__ == "__main__":
    main()
