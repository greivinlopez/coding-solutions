# -----------------
# 38. Count and Say
# -----------------

# Problem: https://leetcode.com/problems/count-and-say
#
# The count-and-say sequence is a sequence of digit strings defined by the
# recursive formula:
# 
#         countAndSay(1) = "1"
#         countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# 
# Run-length encoding (RLE) is a string compression method that works by replacing
# consecutive identical characters (repeated 2 or more times) with the
# concatenation of the character and the number marking the count of the
# characters (length of the run). For example, to compress the string "3322251" we
# replace "33" with "23", replace "222" with "32", replace "5" with "15" and
# replace "1" with "11". Thus the compressed string becomes "23321511".
# 
# Given a positive integer n, return the nth element of the count-and-say
# sequence.
# 
# Example 1:
# 
# Input: n = 4
# Output: "1211"
# 
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"
# 
# Example 2:
# 
# Input: n = 1
# Output: "1"
# 
# Explanation:
# This is the base case.
# 
# 
# Constraints:
#         1 <= n <= 30
# 
# Follow up: Could you solve it iteratively?


# Credit: Jeel Gajera -> https://github.com/JeelGajera
def count_and_say(n):
    s = "1"
    while n > 1:
        count = 1
        tmp = []
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                tmp.append(str(count) + s[i])
                count = 1
        tmp.append(str(count) + s[-1])
        s = "".join(tmp)
        n -= 1
    return s
    # Time: O(cⁿ)
    # Space: O(cⁿ)
    # c = Conway's constant: https://en.wikipedia.org/wiki/Look-and-say_sequence


def main():
    result = count_and_say(4)
    print(result) # "1211"

    result = count_and_say(1)
    print(result) # "1"

if __name__ == "__main__":
    main()
