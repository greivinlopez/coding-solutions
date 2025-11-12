# ----------------------------------------
# 842. Split Array into Fibonacci Sequence
# ----------------------------------------

# Problem: https://leetcode.com/problems/split-array-into-fibonacci-sequence
#
# You are given a string of digits num, such as "123456579". We can split it into
# a Fibonacci-like sequence [123, 456, 579].
# 
# Formally, a Fibonacci-like sequence is a list f of non-negative integers such
# that:
#         
#   * 0 <= f[i] < 231, (that is, each integer fits in a 32-bit signed integer type),
#   * f.length >= 3, and
#   * f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.
# 
# Note that when splitting the string into pieces, each piece must not have extra
# leading zeroes, except if the piece is the number 0 itself.
# 
# Return any Fibonacci-like sequence split from num, or return [] if it cannot be
# done.
# 
# Example 1:
# 
# Input: num = "1101111"
# Output: [11,0,11,11]
# 
# Explanation: The output [110, 1, 111] would also be accepted.
# 
# Example 2:
# 
# Input: num = "112358130"
# Output: []
# 
# Explanation: The task is impossible.
# 
# Example 3:
# 
# Input: num = "0123"
# Output: []
# 
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
# 
# 
# Constraints:
#         1 <= num.length <= 200
#         num contains only digits.


# Credit: Jeel Gajera -> https://github.com/JeelGajera
def split_into_fibonacci(num):
    max_int = 2**31 - 1
    arr = []
    
    def backtrack(cur, arr, num):
        if cur == len(num) and len(arr) >= 3:
            return arr
        for i in range(cur, len(num)):
            if num[cur] == '0' and i > cur:
                break  # leading 0 not allowed
            x = int(num[cur:i + 1])
            if x > max_int:
                break  # check for out of bounds
            if len(arr) <= 1 or x == arr[-1] + arr[-2]:
                arr.append(x)
                nxt = backtrack(i + 1, arr, num)
                if nxt:
                    return nxt
                arr.pop()

        return []

    return backtrack(0, arr, num)
    # Time: O(n²)
    # Space: O(1)


def main():
    result = split_into_fibonacci(num = "1101111")
    print(result) # [11,0,11,11]

    result = split_into_fibonacci(num = "112358130")
    print(result) # []

    result = split_into_fibonacci(num = "0123")
    print(result) # []

if __name__ == "__main__":
    main()
