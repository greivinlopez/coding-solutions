# ---------------------------------
# 1278. Palindrome Partitioning III
# ---------------------------------

# Problem: https://leetcode.com/problems/palindrome-partitioning-iii
#
# You are given a string s containing lowercase letters and an integer k. You need
# to :
#         
#   * First, change some characters of s to other lowercase English letters.
#   * Then divide s into k non-empty disjoint substrings such that each
#     substring is a palindrome.
# 
# Return the minimal number of characters that you need to change to divide the
# string.
# 
# Example 1:
# 
# Input: s = "abc", k = 2
# Output: 1
# 
# Explanation: You can split the string into "ab" and "c", and change 1 character
# in "ab" to make it palindrome.
# 
# Example 2:
# 
# Input: s = "aabbc", k = 3
# Output: 0
# 
# Explanation: You can split the string into "aa", "bb" and "c", all of them are
# palindrome.
# 
# Example 3:
# 
# Input: s = "leetcode", k = 8
# Output: 0
# 
# 
# Constraints:
#         1 <= k <= s.length <= 100.
#         s only contains lowercase English letters.


# Solution: https://algo.monster/liteproblems/1278
# Credit: AlgoMonster
def palindrome_partition(s, k):
    n = len(s)
    
    # cost[i][j] stores the minimum changes needed to make substring s[i:j+1] a palindrome
    cost = [[0] * n for _ in range(n)]
    
    # Build the cost table for all substrings
    # Iterate from right to left for start index
    for start in range(n - 1, -1, -1):
        # Iterate from left to right for end index (after start)
        for end in range(start + 1, n):
            # Check if characters at both ends match
            cost[start][end] = int(s[start] != s[end])
            
            # If substring has more than 2 characters, add cost of inner substring
            if start + 1 < end:
                cost[start][end] += cost[start + 1][end - 1]
    
    # dp[i][j] stores minimum changes to partition first i characters into j palindromes
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for length in range(1, n + 1):
        # Can't partition into more groups than characters available
        for groups in range(1, min(length, k) + 1):
            if groups == 1:
                # Single partition: cost to make entire substring a palindrome
                dp[length][groups] = cost[0][length - 1]
            else:
                # Multiple partitions: try all possible last partition points
                dp[length][groups] = float('inf')
                
                # Try splitting at position split_point
                # First split_point characters into (groups-1) partitions
                # Remaining characters form the last partition
                for split_point in range(groups - 1, length):
                    dp[length][groups] = min(
                        dp[length][groups], 
                        dp[split_point][groups - 1] + cost[split_point][length - 1]
                    )
    
    return dp[n][k]
    # Time: O(n² * k)
    # Space: O(n * (n + k))


def main():
    result = palindrome_partition(s = "abc", k = 2)
    print(result) # 1

    result = palindrome_partition(s = "aabbc", k = 3)
    print(result) # 0

    result = palindrome_partition(s = "leetcode", k = 8)
    print(result) # 0

if __name__ == "__main__":
    main()
