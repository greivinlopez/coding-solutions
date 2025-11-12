# -----------------
# 120. Triangle 🔺
# -----------------

# Problem: https://leetcode.com/problems/triangle/
# 
# Given a triangle array, return the minimum path sum from top to bottom.
# 
# For each step, you may move to an adjacent number of the row below. More 
# formally, if you are on index i on the current row, you may move to either 
# index i or index i + 1 on the next row.

# Solution: https://youtu.be/OM1MTokvxs4
# Credit: Navdeep Singh founder of NeetCode
def minimum_total(triangle):
    dp = triangle[-1]

    for row in range(len(triangle) - 2, -1, -1):
        for col in range(0, row + 1):
            dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

    return dp[0]


def main():
    result = minimum_total([[2],[3,4],[6,5,7],[4,1,8,3]])
    print(result) # 11

    result = minimum_total([[-10]])
    print(result) # -10

if __name__ == "__main__":
    main()