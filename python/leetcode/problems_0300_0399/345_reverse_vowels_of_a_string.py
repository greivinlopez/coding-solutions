# -------------------------------
# 345. Reverse Vowels of a String
# -------------------------------

# Problem: https://leetcode.com/problems/reverse-vowels-of-a-string
#
# Given a string s, reverse only all the vowels in the string and return it.
# 
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
# and upper cases, more than once.
# 
# Example 1:
# 
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# 
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes
# "AceCreIm".
# 
# Example 2:
# 
# Input: s = "leetcode"
# Output: "leotcede"
# 
# 
# Constraints:
#         1 <= s.length <= 3 * 10⁵
#         s consist of printable ASCII characters.


# Credit: Jeel Gajera -> https://github.com/JeelGajera
def reverse_vowels(s):
    res = []
    idx = []

    for i in range(len(s)):
        if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            idx.append(i)
            res.append(ord(s[i]))
    
    res = res[::-1]
    tmp = list(s)

    for i in range(len(res)):
        tmp[idx[i]] = chr(res[i])
    
    str_sort = "".join(tmp)
    
    return str_sort
    # Time: O(n)
    # Space: O(n)


def main():
    result = reverse_vowels(s = "IceCreAm")
    print(result) # "AceCreIm"

    result = reverse_vowels("leetcode")
    print(result) # "leotcede"

if __name__ == "__main__":
    main()
