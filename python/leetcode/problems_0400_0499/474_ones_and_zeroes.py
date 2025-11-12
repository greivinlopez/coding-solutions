# --------------------
# 474. Ones And Zeroes
# --------------------

# Problem: https://leetcode.com/problems/ones-and-zeroes/
# 
# You are given an array of binary strings strs and two integers m and n.
# 
# Return the size of the largest subset of strs such that there are at most 
# m 0's and n 1's in the subset.
# 
# A set x is a subset of a set y if all elements of x are also elements of y.
# 
#  
# Example 1:
# 
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
# 
# 
# Example 2:
# 
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.
# 
# 
# Constraints:
# 
# 	1 <= strs.length <= 600
# 	1 <= strs[i].length <= 100
# 	strs[i] consists only of digits '0' and '1'.
# 	1 <= m, n <= 100


# Solution: https://youtu.be/miZ3qV04b1g
# Credit: Navdeep Singh founder of NeetCode
from collections import defaultdict

def find_max_form(strs, M, N):
    # Dynamic Programming
    dp = defaultdict(int)

    for s in strs:
        mCnt, nCnt = s.count("0"), s.count("1")
        for m in range(M, mCnt - 1, -1):
            for n in range(N, nCnt - 1, -1):
                dp[(m, n)] = max(
                    1 + dp[(m - mCnt, n - nCnt)],
                    dp[(m, n)])
    return dp[(M, N)]


def main():
    result = find_max_form(["10","0001","111001","1","0"], 5, 3)
    print(result) # 4

    result = find_max_form(["10","0","1"], 1, 1)
    print(result) # 2

if __name__ == "__main__":
    main()
