# --------------------------------
# 1745. Palindrome Partitioning IV
# --------------------------------

# Problem: https://leetcode.com/problems/palindrome-partitioning-iv
#
# Given a string s, return true if it is possible to split the string s into three
# non-empty palindromic substrings. Otherwise, return false.​​​​​
# 
# A string is said to be palindrome if it the same string when reversed.
# 
# Example 1:
# 
# Input: s = "abcbdd"
# Output: true
# 
# Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are
# palindromes.
# 
# Example 2:
# 
# Input: s = "bcbddxy"
# Output: false
# 
# Explanation: s cannot be split into 3 palindromes.
# 
# 
# Constraints:
#         3 <= s.length <= 2000
#         s​​​​​​ consists only of lowercase English letters.


# Solution: https://algo.monster/liteproblems/1745
# Credit: AlgoMonster
def check_partitioning(s):
    n = len(s)
    
    # Build a 2D DP table where is_palindrome[i][j] indicates 
    # whether substring s[i:j+1] is a palindrome
    is_palindrome = [[True] * n for _ in range(n)]
    
    # Fill the palindrome table using bottom-up approach
    # Start from the end of string and work backwards
    for start in range(n - 1, -1, -1):
        for end in range(start + 1, n):
            # A substring is palindrome if:
            # 1. First and last characters match, AND
            # 2. Either it's a 2-character string OR the inner substring is also palindrome
            is_palindrome[start][end] = (
                s[start] == s[end] and 
                (end - start == 1 or is_palindrome[start + 1][end - 1])
            )
    
    # Try all possible ways to split the string into 3 parts
    # First cut after index i, second cut after index j
    for first_cut in range(n - 2):  # Leave room for at least 2 more characters
        for second_cut in range(first_cut + 1, n - 1):  # Leave room for last substring
            # Check if all three parts are palindromes:
            # Part 1: s[0:first_cut+1]
            # Part 2: s[first_cut+1:second_cut+1]  
            # Part 3: s[second_cut+1:n]
            if (is_palindrome[0][first_cut] and 
                is_palindrome[first_cut + 1][second_cut] and 
                is_palindrome[second_cut + 1][n - 1]):
                return True
    
    return False
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = check_partitioning(s = "abcbdd")
    print(result) # True

    result = check_partitioning(s = "bcbddxy")
    print(result) # False

if __name__ == "__main__":
    main()
