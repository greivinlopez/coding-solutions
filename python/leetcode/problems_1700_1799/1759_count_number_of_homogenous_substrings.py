# -------------------------------------------
# 1759. Count Number of Homogenous Substrings
# -------------------------------------------

# Problem: https://leetcode.com/problems/count-number-of-homogenous-substrings
#
# Given a string s, return the number of homogenous substrings of s. Since the
# answer may be too large, return it modulo 10⁹ + 7.
# 
# A string is homogenous if all the characters of the string are the same.
# 
# A substring is a contiguous sequence of characters within a string.
# 
# Example 1:
# 
# Input: s = "abbcccaa"
# Output: 13
# 
# Explanation: The homogenous substrings are listed as below:
# "a"   appears 3 times.
# "aa"  appears 1 time.
# "b"   appears 2 times.
# "bb"  appears 1 time.
# "c"   appears 3 times.
# "cc"  appears 2 times.
# "ccc" appears 1 time.
# 3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
# 
# Example 2:
# 
# Input: s = "xy"
# Output: 2
# 
# Explanation: The homogenous substrings are "x" and "y".
# 
# Example 3:
# 
# Input: s = "zzzzz"
# Output: 15
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s consists of lowercase letters.


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def count_homogenous(s):
    ans = 0
    curr_streak = 0
    MOD = 10 ** 9 + 7
    
    for i in range(len(s)):
        
        if i == 0 or s[i] == s[i-1]:
            curr_streak += 1
        else:
            curr_streak = 1
        
        ans = (ans + curr_streak) % MOD
    
    return ans
    # Time: O(n)
    # Space: O(1)


def main():
    result = count_homogenous(s = "abbcccaa")
    print(result) # 13

    result = count_homogenous(s = "xy")
    print(result) # 2

    result = count_homogenous(s = "zzzzz")
    print(result) # 15

if __name__ == "__main__":
    main()
