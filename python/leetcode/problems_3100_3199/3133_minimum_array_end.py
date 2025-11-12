# -----------------------
# 3133. Minimum Array End
# -----------------------

# Problem: https://leetcode.com/problems/minimum-array-end
#
# You are given two integers n and x. You have to construct an array of positive
# integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater
# than nums[i], and the result of the bitwise AND operation between all elements
# of nums is x.
# 
# Return the minimum possible value of nums[n - 1].
# 
# Example 1:
# 
# Input: n = 3, x = 4
# Output: 6
# 
# Explanation:
# nums can be [4,5,6] and its last element is 6.
# 
# Example 2:
# 
# Input: n = 2, x = 7
# Output: 15
# 
# Explanation:
# nums can be [7,15] and its last element is 15.
# 
# 
# Constraints:
#         1 <= n, x <= 10^8


# Solution: https://youtu.be/4pP-0UpEok4
# Credit: Navdeep Singh founder of NeetCode
def min_end(n, x):
    res = x
    i_x = 1
    i_n = 1  # for n-1

    while i_n <= n - 1:
        if i_x & x == 0:
            if i_n & (n - 1):
                res = res | i_x
            i_n = i_n << 1

        i_x = i_x << 1

    return res
    # Time: O(log(n))
    # Space: O(1)

def min_end_simplified(n, x):
    res = x
    for _ in range(n - 1):
        res += 1
    res = res | x
    return res
    # Time: O(n)
    # Space: O(1)


def main():
    result = min_end_simplified(n = 3, x = 4)
    print(result) # 6

    result = min_end_simplified(n = 2, x = 7)
    print(result) # 15

if __name__ == "__main__":
    main()
