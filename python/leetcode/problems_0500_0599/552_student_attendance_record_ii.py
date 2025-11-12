# ---------------------------------
# 552. Student Attendance Record II
# ---------------------------------

# Problem: https://leetcode.com/problems/student-attendance-record-ii
#
# An attendance record for a student can be represented as a string where each
# character signifies whether the student was absent, late, or present on that
# day. The record only contains the following three characters:
# 
#         'A': Absent.
#         'L': Late.
#         'P': Present.
# 
# Any student is eligible for an attendance award if they meet both of the
# following criteria:
# 
#         The student was absent ('A') for strictly fewer than 2 days total.
#         The student was never late ('L') for 3 or more consecutive days.
# 
# Given an integer n, return the number of possible attendance records of length n
# that make a student eligible for an attendance award. The answer may be very
# large, so return it modulo 10^9 + 7.
# 
# Example 1:
# 
# Input: n = 2
# Output: 8
# 
# Explanation: There are 8 records with length 2 that are eligible for an award:
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be fewer
# than 2).
# 
# Example 2:
# 
# Input: n = 1
# Output: 3
# 
# Example 3:
# 
# Input: n = 10101
# Output: 183236316
# 
# 
# Constraints:
#         1 <= n <= 10^5

from collections import defaultdict

# Solution: https://youtu.be/BPIJ5ROX0i4
# Credit: Navdeep Singh founder of NeetCode
def check_record(n):
    MOD = 10**9 + 7
    if n == 1:
        return 3
    
    tmp = {
        (0, 0): 1, (0, 1): 1, (0, 2): 0,
        (1, 0): 1, (1, 1): 0, (1, 2): 0
    }
    
    for i in range(n - 1):
        res = defaultdict(int)
        
        # Choose P
        res[(0, 0)] = ((tmp[(0, 0)] + tmp[(0, 1)]) % MOD + tmp[(0, 2)]) % MOD
        res[(1, 0)] = ((tmp[(1, 0)] + tmp[(1, 1)]) % MOD + tmp[(1, 2)]) % MOD
        
        # Choose L
        res[(0, 1)] = tmp[(0, 0)]
        res[(1, 1)] = tmp[(1, 0)]
        res[(0, 2)] = tmp[(0, 1)]
        res[(1, 2)] = tmp[(1, 1)]
        
        # Choose A
        res[(1, 0)] = (res[(1, 0)] + (((tmp[(0, 0)] + tmp[(0, 1)]) % MOD + tmp[(0, 2)]) % MOD)) % MOD
        
        tmp = res
    
    return sum(tmp.values()) % MOD
    # Time: O(n)
    # Space: O(1)


def main():
    result = check_record(2)
    print(result) # 8

    result = check_record(1)
    print(result) # 3

    result = check_record(10101)
    print(result) # 183236316

if __name__ == "__main__":
    main()
