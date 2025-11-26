# --------------------------------
# 1641. Count Sorted Vowel Strings
# --------------------------------

# Problem: https://leetcode.com/problems/count-sorted-vowel-strings
#
# Given an integer n, return the number of strings of length n that consist only
# of vowels (a, e, i, o, u) and are lexicographically sorted.
# 
# A string s is lexicographically sorted if for all valid i, s[i] is the same as
# or comes before s[i+1] in the alphabet.
# 
# Example 1:
# 
# Input: n = 1
# Output: 5
# 
# Explanation: The 5 sorted strings that consist of vowels only are
# ["a","e","i","o","u"].
# 
# Example 2:
# 
# Input: n = 2
# Output: 15
# 
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
# 
# Example 3:
# 
# Input: n = 33
# Output: 66045
# 
# 
# Constraints:
#         1 <= n <= 50


# Solution: https://algo.monster/liteproblems/1641
# Credit: AlgoMonster
def count_vowel_strings(n):
    from functools import cache
    
    @cache
    def dfs(current_position, start_vowel_index):
        # Base case: reached the required string length
        if current_position >= n:
            return 1
        
        # Recursive case: try all vowels from current vowel index to 'u' (index 4)
        # This ensures lexicographical order is maintained
        total_count = 0
        for next_vowel_index in range(start_vowel_index, 5):
            total_count += dfs(current_position + 1, next_vowel_index)
        
        return total_count
    
    # Start building strings from position 0, allowing all vowels initially
    return dfs(0, 0)
    # Time: O(n)
    # Space: O(n)


def main():
    result = count_vowel_strings(n = 1)
    print(result) # 5

    result = count_vowel_strings(n = 2)
    print(result) # 15

    result = count_vowel_strings(n = 33)
    print(result) # 66045

if __name__ == "__main__":
    main()
