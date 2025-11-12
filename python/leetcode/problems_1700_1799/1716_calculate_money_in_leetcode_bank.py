# -----------------------------------------
# 1716. Calculate Money in Leetcode Bank 🏦
# -----------------------------------------

# Problem: https://leetcode.com/problems/calculate-money-in-leetcode-bank
#
# Hercy wants to save money for his first car. He puts money in the Leetcode bank
# every day.
# 
# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to
# Sunday, he will put in $1 more than the day before. On every subsequent Monday,
# he will put in $1 more than the previous Monday.
# 
# Given n, return the total amount of money he will have in the Leetcode bank at
# the end of the nth day.
# 
# Example 1:
# 
# Input: n = 4
# Output: 10
# 
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
# 
# Example 2:
# 
# Input: n = 10
# Output: 37
# 
# xplanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 +
# 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
# 
# Example 3:
# 
# Input: n = 20
# Output: 96
# 
# Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 +
# 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
# 
# 
# Constraints:
#         1 <= n <= 1000


# Solution: https://youtu.be/tKK7gvPCQfs
# Credit: Navdeep Singh founder of NeetCode
def total_money(n):
    weeks = n // 7
    low = 28
    high = 28 + 7 * (weeks - 1)
    res = (weeks * (low + high) // 2)
    
    monday = weeks + 1
    for i in range(n % 7):
        res += i + monday
    
    return res
    # Time: O(1)
    # Space: O(1)


def main():
    result = total_money(n = 4)
    print(result) # 10

    result = total_money(n = 10)
    print(result) # 37

    result = total_money(n = 20)
    print(result) # 96

if __name__ == "__main__":
    main()
