# --------------------
# 935. Knight Dialer ♟️
# --------------------

# Problem: https://leetcode.com/problems/knight-dialer
#
# The chess knight has a unique movement, it may move two squares vertically and
# one square horizontally, or two squares horizontally and one square vertically
# (with both forming the shape of an L). The possible movements of chess knight
# are shown in this diagram:
# 
# A chess knight can move as indicated in the chess diagram below:
# 
# https://assets.leetcode.com/uploads/2020/08/18/chess.jpg
# 
# We have a chess knight and a phone pad as shown below, the knight can only stand
# on a numeric cell (i.e. blue cell).
# 
# https://assets.leetcode.com/uploads/2020/08/18/phone.jpg
# 
# Given an integer n, return how many distinct phone numbers of length n we can
# dial.
# 
# You are allowed to place the knight on any numeric cell initially and then you
# should perform n - 1 jumps to dial a number of length n. All jumps should be
# valid knight jumps.
# 
# As the answer may be very large, return the answer modulo 10^9 + 7.
# 
# Example 1:
# 
# Input: n = 1
# Output: 10
# 
# Explanation: We need to dial a number of length 1, so placing the knight over
# any numeric cell of the 10 cells is sufficient.
# 
# Example 2:
# 
# Input: n = 2
# 
# Output: 20
# 
# Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34,
# 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
# 
# Example 3:
# 
# Input: n = 3131
# Output: 136006598
# 
# Explanation: Please take care of the mod.
# 
# 
# Constraints:
#         1 <= n <= 5000


# Solution: https://youtu.be/vlsUUm_qqsY
# Video Credit: Navdeep Singh founder of NeetCode
# Solution credit: Mark Solomon Philip -> https://leetcode.com/u/MarkSPhilip31/
# https://leetcode.com/problems/knight-dialer/solutions/4336024/c-java-python-javascript-6-approaches-explained/
def knight_dialer(n):
    if n == 1:
        return 10
    
    A = 4
    B = 2
    C = 2
    D = 1
    MOD = 10 ** 9 + 7
    
    for _ in range(n - 1):
        A, B, C, D = (2 * (B + C)) % MOD, A, (A + 2 * D) % MOD, C 
    
    return (A + B + C + D) % MOD
    # Time: O(n) 
    # Space: O(1)


def main():
    result = knight_dialer(1)
    print(result) # 10

    result = knight_dialer(2)
    print(result) # 20

    result = knight_dialer(3131)
    print(result) # 136006598

if __name__ == "__main__":
    main()
