# ------------------------
# 60. Permutation Sequence
# ------------------------

# Problem: https://leetcode.com/problems/permutation-sequence
#
# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order, we get the following
# sequence for n = 3:
#         "123"
#         "132"
#         "213"
#         "231"
#         "312"
#         "321"
# 
# Given n and k, return the kth permutation sequence.
# 
# Example 1:
# 
# Input: n = 3, k = 3
# Output: "213"
# 
# Example 2:
# 
# Input: n = 4, k = 9
# Output: "2314"
# 
# Example 3:
# 
# Input: n = 3, k = 1
# Output: "123"
# 
# 
# Constraints:
#         1 <= n <= 9
#         1 <= k <= n!

# Solution: https://leetcode.com/problems/permutation-sequence/solutions/6843957/easy-to-understand-solution-using-math-no-recursion-backtracking-1-ms-time-complexity/
# Credit: Ishita Joshi -> https://leetcode.com/u/IshitaJoshi/
def get_permutation(n, k):
    from math import factorial

    numbers = list(range(1, n + 1))
    fact = factorial(n)
    k -= 1  # 0-based indexing
    result = []

    for i in range(n):
        fact //= (n - i)
        index = k // fact
        result.append(str(numbers[index]))
        numbers.pop(index)
        k %= fact

    return ''.join(result)
    # Time: O(n²)
    # Space: O(n)


def main():
    result = get_permutation(n = 3, k = 3)
    print(result) # "213"

    result = get_permutation(n = 4, k = 9)
    print(result) # "2314"

    result = get_permutation(n = 3, k = 1)
    print(result) # "123"

if __name__ == "__main__":
    main()
