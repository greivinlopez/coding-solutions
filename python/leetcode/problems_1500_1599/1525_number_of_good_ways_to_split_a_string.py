# -------------------------------------------
# 1525. Number of Good Ways to Split a String
# -------------------------------------------

# Problem: https://leetcode.com/problems/number-of-good-ways-to-split-a-string
#
# You are given a string s.
# 
# A split is called good if you can split s into two non-empty strings sleft and
# sright where their concatenation is equal to s (i.e., sleft + sright = s) and
# the number of distinct letters in sleft and sright is the same.
# 
# Return the number of good splits you can make in s.
# 
# Example 1:
# 
# Input: s = "aacaba"
# Output: 2
# 
# Explanation: There are 5 ways to split "aacaba" and 2 of them are good.
# ("a", "acaba") Left string and right string contains 1 and 3 different letters
# respectively.
# ("aa", "caba") Left string and right string contains 1 and 3 different letters
# respectively.
# ("aac", "aba") Left string and right string contains 2 and 2 different letters
# respectively (good split).
# ("aaca", "ba") Left string and right string contains 2 and 2 different letters
# respectively (good split).
# ("aacab", "a") Left string and right string contains 3 and 1 different letters
# respectively.
# 
# Example 2:
# 
# Input: s = "abcd"
# Output: 1
# 
# Explanation: Split the string as follows ("ab", "cd").
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s consists of only lowercase English letters.

from collections import Counter

# Solution: https://algo.monster/liteproblems/1525
# Credit: AlgoMonster
def num_splits(s):
    # Count frequency of each character in the entire string
    right_counter = Counter(s)
    
    # Track unique characters in the left partition
    left_unique = set()
    
    # Initialize count of good splits
    good_splits = 0
    
    # Iterate through each character to simulate splitting
    for char in s:
        # Add current character to left partition
        left_unique.add(char)
        
        # Remove one occurrence from right partition
        right_counter[char] -= 1
        
        # If character count reaches 0, remove it from right partition
        if right_counter[char] == 0:
            right_counter.pop(char)
        
        # Check if both partitions have equal number of unique characters
        if len(left_unique) == len(right_counter):
            good_splits += 1
            
    return good_splits
    # Time: O(n)
    # Space: O(k)
    # k = the number of unique characters in the string


def main():
    result = num_splits(s = "aacaba")
    print(result) # 2

    result = num_splits(s = "abcd")
    print(result) # 1

if __name__ == "__main__":
    main()
