# ------------------------------
# 1220. Count Vowels Permutation
# ------------------------------

# Problem: https://leetcode.com/problems/count-vowels-permutation
#
# Given an integer n, your task is to count how many strings of length n can be
# formed under the following rules:
# 
#         Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
#         Each vowel 'a' may only be followed by an 'e'.
#         Each vowel 'e' may only be followed by an 'a' or an 'i'.
#         Each vowel 'i' may not be followed by another 'i'.
#         Each vowel 'o' may only be followed by an 'i' or a 'u'.
#         Each vowel 'u' may only be followed by an 'a'.
# 
# Since the answer may be too large, return it modulo 10^9 + 7.
# 
# Example 1:
# 
# Input: n = 1
# Output: 5
# Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
# 
# Example 2:
# 
# Input: n = 2
# Output: 10
# Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu",
# "oi", "ou" and "ua".
# 
# Example 3: 
# 
# Input: n = 5
# Output: 68
# 
# 
# Constraints:
#         1 <= n <= 2 * 10^4


# Solution: https://youtu.be/VUVpTZVa7Ls
# Credit: Navdeep Singh founder of NeetCode
Memo = {}    
def count_vowel_permutation(n, c = ''):        
    if (c, n) in Memo:            
        return Memo[(c, n)]
    if n == 1:
        if c == 'a':
            return 1 
        if c == 'e':
            return 2 
        if c == 'i':
            return 4 
        if c == 'o':
            return 2 
        if c == 'u':
            return 1            
        if c == '':                
            return 5
    else:
        if c == 'a':
            Memo[('a', n)] = count_vowel_permutation(n - 1, 'e')                
            return Memo[('a', n)]
        if c == 'e':
            Memo[('e', n)] = count_vowel_permutation(n - 1, 'a') + count_vowel_permutation(n - 1, 'i')                
            return Memo[('e', n)]
        if c == 'i':
            Memo[('i', n)] = count_vowel_permutation(n - 1, 'a') + count_vowel_permutation(n - 1, 'e') + count_vowel_permutation(n - 1, 'o') + count_vowel_permutation(n - 1, 'u')          
            return Memo[('i', n)]
        if c == 'o':
            Memo[('o', n)] = count_vowel_permutation(n - 1, 'i') + count_vowel_permutation(n - 1, 'u')                
            return Memo[('o', n)]
        if c == 'u':
            Memo[('u', n)] = count_vowel_permutation(n - 1, 'a')                
            return Memo[('u', n)]
        if c == '':
            Tot = 0
            for i in ['a', 'e', 'i', 'o', 'u']:
                Tot = Tot + count_vowel_permutation(n - 1, i);                    
            return Tot % 1000000007     


def main():
    result = count_vowel_permutation(1)
    print(result) # 5

    result = count_vowel_permutation(2)
    print(result) # 10

    result = count_vowel_permutation(5)
    print(result) # 68

if __name__ == "__main__":
    main()
