# --------------------------------------------
# 1523. Count Odd Numbers In An Interval Range
# --------------------------------------------

# Problem: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range
#
# Given two non-negative integers low and high. Return the count of odd numbers
# between low and high (inclusive).
# 
# Example 1:
# 
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].
# 
# Example 2:
# 
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].
# 
# 
# Constraints:
#         0 <= low <= high <= 10^9


# Solution: https://youtu.be/wrIWye928JQ
# Credit: Navdeep Singh founder of NeetCode
def count_odds(low, high):
    if low % 2 != 0 or high % 2 != 0:
        return (high - low) // 2+1
    return (high - low) // 2


def main():
    result = count_odds(low = 3, high = 7)
    print(result) # 3

    result = count_odds(low = 8, high = 10)
    print(result) # 1

if __name__ == "__main__":
    main()
