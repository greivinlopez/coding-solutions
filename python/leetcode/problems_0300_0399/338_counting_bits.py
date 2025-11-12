# ------------------
# 338. Counting Bits
# ------------------

# Problem: https://leetcode.com/problems/counting-bits/
# 
# Given an integer n, return an array ans of length n + 1 such that for each 
# i (0 <= i <= n), ans[i] is the number of 1's in the binary representation 
# of i.
# 
#  
# Example 1:
# 
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 
# 
# Example 2:
# 
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# 
# 
# Constraints:
# 
# 	0 <= n <= 10^5
# 
# Follow up:
# 
# 	It is very easy to come up with a solution with a runtime of O(n log n). 
#   Can you do it in linear time O(n) and possibly in a single pass?
# 	Can you do it without using any built-in function 
#   (i.e., like __builtin_popcount in C++)?


# Solution: https://youtu.be/RyBM56RIWrM
# Credit: Navdeep Singh founder of NeetCode
def count_bits(n):
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp

# Credit: ginger1058 -> https://leetcode.com/u/ginger1058/ 
# Solution: https://leetcode.com/problems/counting-bits/solutions/4411054/odd-and-even-numbers-a-easier-to-understanding-way-of-dp/
def count_bits_alt(n):
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        if i % 2 == 1:
            res[i] = res[i - 1] + 1
        else:
            res[i] = res[i // 2]
    return res
    # Time: O(n)
    # Space: O(n)


def main():
    result = count_bits_alt(2)
    print(result) # [0,1,1]

    result = count_bits_alt(5)
    print(result) # [0,1,1,2,1,2]

if __name__ == "__main__":
    main()
