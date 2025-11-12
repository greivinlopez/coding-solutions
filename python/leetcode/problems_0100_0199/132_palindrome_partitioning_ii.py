# -------------------------------
# 132. Palindrome Partitioning II
# -------------------------------

# Problem: https://leetcode.com/problems/palindrome-partitioning-ii
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# Example 1:
# 
# Input: s = "aab"
# Output: 1
# 
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
# 
# Example 2:
# 
# Input: s = "a"
# Output: 0
# 
# Example 3:
# 
# Input: s = "ab"
# Output: 1
# 
# 
# Constraints:
#         1 <= s.length <= 2000
#         s consists of lowercase English letters only.


# Solution: https://leetcode.com/problems/palindrome-partitioning-ii/solutions/2812683/python3-solution-dp-o-n-2
# Credit: Satyam -> https://leetcode.com/u/satyam2001/
def min_cut(s):
    N = len(s)
    dp = [-1] + [N] * N

    for i in range(2 * N - 1):
        l = i // 2
        r = l + (i & 1)
        while 0 <= l and r < N and s[l] == s[r]:
            dp[r + 1] = min(dp[r + 1], dp[l] + 1)
            l -= 1
            r += 1

    return dp[-1]
    # Time: O(n²)
    # Space: O(n)


def main():
    result = min_cut("aab")
    print(result) # 1

    result = min_cut("a")
    print(result) # 0

    result = min_cut("ab")
    print(result) # 1

if __name__ == "__main__":
    main()
