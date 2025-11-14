# -----------------------------------------------------------------------
# 1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits
# -----------------------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits
#
# You are given a string num representing the digits of a very large integer and
# an integer k. You are allowed to swap any two adjacent digits of the integer at
# most k times.
# 
# Return the minimum integer you can obtain also as a string.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/06/17/q4_1.jpg
# 
# Input: num = "4321", k = 4
# Output: "1342"
# 
# Explanation: The steps to obtain the minimum integer from 4321 with 4 adjacent
# swaps are shown.
# 
# Example 2:
# 
# Input: num = "100", k = 1
# Output: "010"
# 
# Explanation: It's ok for the output to have leading zeros, but the input is
# guaranteed not to have any leading zeros.
# 
# Example 3:
# 
# Input: num = "36789", k = 1000
# Output: "36789"
# 
# Explanation: We can keep the number without any swaps.
# 
# 
# Constraints:
#         1 <= num.length <= 3 * 10⁴
#         num consists of only digits and does not contain leading zeros.
#         1 <= k <= 10⁹


# Solution: https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/solutions/6458701/py3-82beats-by-fareedbaba-xhke
# Credit: Fareed Baba -> https://leetcode.com/u/fareedbaba/
def min_integer(num, k):
    if k <= 0: return num
    n = len(num)
    if k >= n*(n-1)//2: 
        return "".join(sorted(list(num)))

    # for each number, find the first index
    for i in range(10):
        ind = num.find(str(i))
        if 0 <= ind <= k:
            return str(num[ind]) + min_integer(num[0:ind] + num[ind+1:], k-ind)
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = min_integer(num = "4321", k = 4)
    print(result) # "1342"

    result = min_integer(num = "100", k = 1)
    print(result) # "010"

    result = min_integer(num = "36789", k = 1000)
    print(result) # "36789"

if __name__ == "__main__":
    main()
