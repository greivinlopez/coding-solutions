# ---------------------
# 390. Elimination Game
# ---------------------

# Problem: https://leetcode.com/problems/elimination-game
#
# You have a list arr of all integers in the range [1, n] sorted in a strictly
# increasing order. Apply the following algorithm on arr:
#         
#   * Starting from left to right, remove the first number and every other
#     number afterward until you reach the end of the list.
#   * Repeat the previous step again, but this time from right to left, remove
#     the rightmost number and every other number from the remaining numbers.
#   * Keep repeating the steps again, alternating left to right and right to
#     left, until a single number remains.
# 
# Given the integer n, return the last number that remains in arr.
# 
# Example 1:
# 
# Input: n = 9
# Output: 6
# 
# Explanation:
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [2, 4, 6, 8]
# arr = [2, 6]
# arr = [6]
# 
# Example 2:
# 
# Input: n = 1
# Output: 1
# 
# 
# Constraints:
#         1 <= n <= 10⁹


# Solution: https://leetcode.com/problems/elimination-game/solutions/552326/python-95-time-o-logn-and-constant-memory-commented-and-explained
# Credit: https://leetcode.com/u/ddhnnng/
def last_remaining(n):
    N = n       # number of remaining numbers
    fwd = True  # flag for forward/backward elimination
    m = 2       # elimination step/interval
    s = 0       # elimination base

    while N > 1:
        if fwd or N % 2 == 1: 
            s += m // 2
        m *= 2
        N = N // 2
        fwd = not fwd   # reverse the pass direction
    return s+1
    # Time: O(log(n))
    # Space: O(1)


def main():
    result = last_remaining(9)
    print(result) # 6

    result = last_remaining(1)
    print(result) # 1

if __name__ == "__main__":
    main()
