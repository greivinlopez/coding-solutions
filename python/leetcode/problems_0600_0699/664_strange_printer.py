# --------------------
# 664. Strange Printer
# --------------------

# Problem: https://leetcode.com/problems/strange-printer
#
# There is a strange printer with the following two special properties:
#         
#   * The printer can only print a sequence of the same character each time.
#   * At each turn, the printer can print new characters starting from and
#     ending at any place and will cover the original existing characters.
# 
# Given a string s, return the minimum number of turns the printer needed to print
# it.
# 
# Example 1:
# 
# Input: s = "aaabbb"
# Output: 2
# 
# Explanation: Print "aaa" first and then print "bbb".
# 
# Example 2:
# 
# Input: s = "aba"
# Output: 2
# 
# Explanation: Print "aaa" first and then print "b" from the second place of the
# string, which will cover the existing character 'a'.
# 
# 
# Constraints:
#         1 <= s.length <= 100
#         s consists of lowercase English letters.


# Solution: https://algo.monster/liteproblems/664
# Credit: AlgoMonster
def strange_printer(s):
    n = len(s)
    
    # dp[i][j] represents minimum number of turns to print substring s[i:j+1]
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Iterate through all possible substrings from bottom-right to top-left
    for i in range(n - 1, -1, -1):
        # Single character needs only 1 turn to print
        dp[i][i] = 1
        
        # Check all substrings starting at position i
        for j in range(i + 1, n):
            if s[i] == s[j]:
                # If first and last characters are same,
                # we can print them together in the same turn
                # So the cost is same as printing s[i:j]
                dp[i][j] = dp[i][j - 1]
            else:
                # If first and last characters are different,
                # try splitting at each position k and find minimum
                for k in range(i, j):
                    # Split into s[i:k+1] and s[k+1:j+1]
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
    
    # Return minimum turns needed to print entire string
    return dp[0][n - 1]
    # Time: O(n³)
    # Space: O(n²)


def main():
    result = strange_printer("aaabbb")
    print(result) # 2

    result = strange_printer("aba")
    print(result) # 2

if __name__ == "__main__":
    main()
