# --------------------
# 650. 2 Keys Keyboard
# --------------------

# Problem: https://leetcode.com/problems/2-keys-keyboard
#
# There is only one character 'A' on the screen of a notepad. You can perform one
# of two operations on this notepad for each step:
#         
#   * Copy All: You can copy all the characters present on the screen (a
#     partial copy is not allowed).
#   * Paste: You can paste the characters which are copied last time.
# 
# Given an integer n, return the minimum number of operations to get the character
# 'A' exactly n times on the screen.
# 
# Example 1:
# 
# Input: n = 3
# Output: 3
# 
# Explanation: Initially, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
# 
# Example 2:
# 
# Input: n = 1
# Output: 0
# 
# 
# Constraints:
#         1 <= n <= 1000


# Solution: https://youtu.be/jNfZH3mdjOA
# Credit: Navdeep Singh founder of NeetCode
def min_steps(n):
    cache = {}
    def helper(count, paste):
        if count == n:
            return 0
        if count > n:
            return 1000
        if (count, paste) in cache:
            return cache[(count, paste)]
        
        # Paste
        res1 = 1 + helper(count + paste, paste)
        # Copy & Paste
        res2 = 2 + helper(count + count, count)
        
        cache[(count, paste)] = min(res1, res2)
        return cache[(count, paste)]

    if n == 1:
        return 0
    return 1 + helper(1, 1)
    # Time: O(n²)
    # Space: O(n²)

def min_steps_alt(n):
    # Optimized Solution
    dp = [1000] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, 1 + (i // 2)):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = min_steps(3)
    print(result) # 3

    result = min_steps(1)
    print(result) # 0

if __name__ == "__main__":
    main()
