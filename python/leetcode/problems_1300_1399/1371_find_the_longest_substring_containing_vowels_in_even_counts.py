# -----------------------------------------------------------------
# 1371. Find the Longest Substring Containing Vowels in Even Counts
# -----------------------------------------------------------------

# Problem: https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts
#
# Given the string s, return the size of the longest substring containing each
# vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear
# an even number of times.
# 
# Example 1:
# 
# Input: s = "eleetminicoworoep"
# Output: 13
# 
# Explanation: The longest substring is "leetminicowor" which contains two each of
# the vowels: e, i and o and zero of the vowels: a and u.
# 
# Example 2:
# 
# Input: s = "leetcodeisgreat"
# Output: 5
# 
# Explanation: The longest substring is "leetc" which contains two e's.
# 
# Example 3:
# 
# Input: s = "bcbcbc"
# Output: 6
# 
# Explanation: In this case, the given string "bcbcbc" is the longest because all
# vowels: a, e, i, o and u appear zero times.
# 
# Constraints:
#         1 <= s.length <= 5 x 10^5
#         s contains only lowercase English letters.


# Solution: https://youtu.be/o17MBWparrI
# Credit: Navdeep Singh founder of NeetCode
def find_the_longest_substring(s):
    vowels = "aeiou"

    res = 0
    mask = 0
    mask_to_idx = {0: -1}

    for i, c in enumerate(s):
        if c in vowels:
            mask = mask ^ (1 << (ord(c) - ord('a')))

        if mask in mask_to_idx:
            length = i - mask_to_idx[mask]
            res = max(res, length)
        else:
            mask_to_idx[mask] = i

    return res
    # Time: O(1) 
    # Space: O(1)


def main():
    result = find_the_longest_substring("eleetminicoworoep")
    print(result) # 13

    result = find_the_longest_substring("leetcodeisgreat")
    print(result) # 5

    result = find_the_longest_substring("bcbcbc")
    print(result) # 6

if __name__ == "__main__":
    main()
