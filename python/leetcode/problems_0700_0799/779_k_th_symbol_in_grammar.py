# ---------------------------
# 779. K-th Symbol in Grammar
# ---------------------------

# Problem: https://leetcode.com/problems/k-th-symbol-in-grammar
#
# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row.
# Now in every subsequent row, we look at the previous row and replace each
# occurrence of 0 with 01, and each occurrence of 1 with 10.
# 
#   For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd
#   row is 0110.
# 
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a
# table of n rows.
# 
# Example 1:
# 
# Input: n = 1, k = 1
# Output: 0
# Explanation: row 1: 0
# 
# Example 2:
# 
# Input: n = 2, k = 1
# Output: 0
# Explanation:
# row 1: 0
# row 2: 01
# 
# Example 3:
# 
# Input: n = 2, k = 2
# Output: 1
# Explanation:
# row 1: 0
# row 2: 01
# 
# 
# Constraints:
#         1 <= n <= 30
#         1 <= k <= 2n - 1


# Solution: https://youtu.be/pmD2HCKaqRQ
# Credit: Navdeep Singh founder of NeetCode
def kth_grammar(n, k):
    cur = 0
    left, right = 1, 2**(n - 1)

    for _ in range(n - 1):
        mid = (left + right) // 2
        if k <= mid:
            right = mid
        else:
            left = mid + 1
            cur = 0 if cur else 1

    return cur

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def kth_grammar_alt(n, k):
    if n == 1:
        return 0
    if k % 2 == 0:
        return 1 if kth_grammar_alt(n-1, k // 2) == 0 else 0
    else:
        return 0 if kth_grammar_alt(n-1, (k+2)//2) == 0 else 1


def main():
    result = kth_grammar(n = 1, k = 1)
    print(result) # 0

    result = kth_grammar(n = 2, k = 1)
    print(result) # 0

    result = kth_grammar(n = 2, k = 2)
    print(result) # 1

if __name__ == "__main__":
    main()
