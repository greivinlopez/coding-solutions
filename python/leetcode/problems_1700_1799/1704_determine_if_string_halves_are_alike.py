# ------------------------------------------
# 1704. Determine if String Halves Are Alike
# ------------------------------------------

# Problem: https://leetcode.com/problems/determine-if-string-halves-are-alike
#
# You are given a string s of even length. Split this string into two halves of
# equal lengths, and let a be the first half and b be the second half.
# 
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i',
# 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and
# lowercase letters.
# 
# Return true if a and b are alike. Otherwise, return false.
# 
# Example 1:
# 
# Input: s = "book"
# Output: true
# 
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore,
# they are alike.
# 
# Example 2:
# 
# Input: s = "textbook"
# Output: false
# 
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2.
# Therefore, they are not alike.
# Notice that the vowel o is counted twice.
# 
# 
# Constraints:
#         2 <= s.length <= 1000
#         s.length is even.
#         s consists of uppercase and lowercase letters.

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def halves_are_alike(s):
    cnt1, cnt2 = 0, 0
    n = len(s)
    a = s[:n//2]
    b = s[n//2:]
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(n//2):
        if a[i] in vowels:
            cnt1 += 1

        if b[i] in vowels:
            cnt2 += 1

    return cnt1 == cnt2
    # Time: O(n)
    # Space: O(n)


def main():
    result = halves_are_alike(s = "book")
    print(result) # True

    result = halves_are_alike(s = "textbook")
    print(result) # False

if __name__ == "__main__":
    main()
