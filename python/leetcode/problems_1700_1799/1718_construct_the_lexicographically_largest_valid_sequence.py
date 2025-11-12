# ------------------------------------------------------------
# 1718. Construct the Lexicographically Largest Valid Sequence
# ------------------------------------------------------------

# Problem: https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence
#
# Given an integer n, find a sequence with elements in the range [1, n] that
# satisfies all of the following:
#         
#   * The integer 1 occurs once in the sequence.
#   * Each integer between 2 and n occurs twice in the sequence.
#   * For every integer i between 2 and n, the distance between the two
#     occurrences of i is exactly i.
# 
# The distance between two numbers on the sequence, a[i] and a[j], is the absolute
# difference of their indices, |j - i|.
# 
# Return the lexicographically largest sequence. It is guaranteed that under the
# given constraints, there is always a solution.
# 
# A sequence a is lexicographically larger than a sequence b (of the same length)
# if in the first position where a and b differ, sequence a has a number greater
# than the corresponding number in b. For example, [0,1,9,0] is lexicographically
# larger than [0,1,5,6] because the first position they differ is at the third
# number, and 9 is greater than 5.
# 
# Example 1:
# 
# Input: n = 3
# Output: [3,1,2,3,2]
# 
# Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the
# lexicographically largest valid sequence.
# 
# Example 2:
# 
# Input: n = 5
# Output: [5,3,1,4,3,5,2,4,2]
# 
# 
# Constraints:
#         1 <= n <= 20


# Solution: https://youtu.be/rNv0vgNc4Ww
# Credit: Navdeep Singh founder of NeetCode
def construct_distanced_sequence(n):
    res = [0] * (2 * n - 1)
    used = set()

    def backtrack(i):
        if i == len(res):
            return True

        if res[i]:
            return backtrack(i + 1)

        for num in reversed(range(1, n + 1)):
            if num in used:
                continue

            if num > 1 and (i + num >= len(res) or res[i + num]):
                continue

            used.add(num)
            res[i] = num
            if num > 1:
                res[i + num] = num

            if backtrack(i + 1):
                return True

            used.remove(num)
            res[i] = 0
            if num > 1:
                res[i + num] = 0

        return False

    backtrack(0)
    return res
    # Time: O(n)
    # Space: O(n)


def main():
    result = construct_distanced_sequence(3)
    print(result) # [3,1,2,3,2]

    result = construct_distanced_sequence(5)
    print(result) # [5,3,1,4,3,5,2,4,2]

if __name__ == "__main__":
    main()
