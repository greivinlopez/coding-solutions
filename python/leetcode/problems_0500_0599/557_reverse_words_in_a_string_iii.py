# ----------------------------------
# 557. Reverse Words in a String III
# ----------------------------------

# Problem: https://leetcode.com/problems/reverse-words-in-a-string-iii
#
# Given a string s, reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.
# 
# Example 1:
# 
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# 
# Example 2:
# 
# Input: s = "Mr Ding"
# Output: "rM gniD"
# 
# 
# Constraints:
#         1 <= s.length <= 5 * 10^4
#         s contains printable ASCII characters.
#         s does not contain any leading or trailing spaces.
#         There is at least one word in s.
#         All the words in s are separated by a single space.


# Solution: https://youtu.be/7kUEwiwwnlA
# Credit: Navdeep Singh founder of NeetCode
def reverse_words(s):
    s = list(s)
    l = 0
    for r in range(len(s)):
        if s[r] == " " or r == len(s) - 1:
            temp_l, temp_r = l, r - 1
            
            if r == len(s) - 1:
                temp_r = r
            
            while temp_l < temp_r:
                s[temp_l], s[temp_r] = s[temp_r], s[temp_l]
                temp_l += 1
                temp_r -= 1
            
            l = r + 1

    return "".join(s)
    # Time: O(n)
    # Space: O(1)

def main():
    result = reverse_words("Let's take LeetCode contest")
    print(result) # True

    result = reverse_words("Mr Ding")
    print(result) # True

if __name__ == "__main__":
    main()
