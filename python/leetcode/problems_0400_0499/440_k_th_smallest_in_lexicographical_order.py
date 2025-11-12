# -------------------------------------------
# 440. K-th Smallest in Lexicographical Order
# -------------------------------------------

# Problem: https://leetcode.com/problems/k-th-smallest-in-lexicographical-order
#
# Given two integers n and k, return the kth lexicographically smallest integer in
# the range [1, n].
# 
# Example 1:
# 
# Input: n = 13, k = 2
# Output: 10
# 
# Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7,
# 8, 9], so the second smallest number is 10.
# 
# Example 2:
# 
# Input: n = 1, k = 1
# Output: 1
# 
# 
# Constraints:
# 
#         1 <= k <= n <= 10^9


# Solution: https://youtu.be/wRubz1zhVqk
# Credit: Navdeep Singh founder of NeetCode
def find_kth_number(n, k):
    cur = 1
    i = 1

    def count(cur):
        res = 0
        nei = cur + 1
        while cur <= n:
            res += min(nei, n + 1) - cur
            cur *= 10
            nei *= 10
        return res

    while i < k:
        steps = count(cur)
        if i + steps <= k:
            cur = cur + 1
            i += steps
        else:
            cur *= 10
            i += 1
    
    return cur
    # Time: O(log(n) ^ 2)

def main():
    result = find_kth_number(n = 13, k = 2)
    print(result) # 10

    result = find_kth_number(n = 1, k = 1)
    print(result) # 1

if __name__ == "__main__":
    main()
